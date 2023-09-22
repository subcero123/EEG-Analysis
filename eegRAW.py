import numpy as np
import pandas as pd 
import mne
import matplotlib.pyplot as plt
from matplotlib.pyplot import specgram
#data = np.random.rand(256)




data = pd.read_csv("AURA_RAW___2023-09-11___11;31;44.csv",usecols=[*range(1, 9)],  skiprows=1, sep=',', index_col=0) 
data = data.transpose().to_numpy()
"""
ch_names = [
'EEG1', 'EEG2', 'EEG3', 'EEG4','EEG5', 'EEG6', 'EEG7', 'EEG8',]
ch_types = ['eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg',]

sfreq = 256  # in Hertz
info = mne.create_info(ch_names = ch_names, sfreq = sfreq)
raw = mne.io.RawArray(data, info)
#raw.plot()
#plt.show()
"""
specgram(data.flatten(), NFFT=256, Fs=256)
plt.show()