import mne  # If this line returns an error, uncomment the following line
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import chart_studio.plotly as py

User_frame = pd.read_csv("/home/thor/Descargas/Uni/10moSemestre/Investigacion/AURA_RAW___2023-09-11___11;31;44.csv",usecols=[*range(1, 9)], skiprows=0 , sep=',') 
data = User_frame.transpose().to_numpy()

ch_names = [
'EEG1', 'EEG2', 'EEG3', 'EEG4','EEG5', 'EEG6', 'EEG7', 'EEG8',]
ch_types = ['eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg',]

sampling_freq = 256  # in Hertz
info = mne.create_info(ch_names= ch_names, ch_types= ch_types, sfreq= sampling_freq)
raw = mne.io.RawArray(data, info)
print(info)
raw.plot()
plt.show()