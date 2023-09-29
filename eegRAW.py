import numpy as np
import pandas as pd 
import mne
import matplotlib.pyplot as plt
from matplotlib.pyplot import specgram


data = pd.read_csv("NoEstimulo/AURA_RAW___2023-09-26___11;02;14.csv",usecols=[*range(1, 9)],  skiprows=2, sep=',') 
data = data.transpose().to_numpy()

ch_names = [
'EEG1', 'EEG2', 'EEG3', 'EEG4','EEG5', 'EEG6', 'EEG7', 'EEG8',]
ch_types = ['eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg',]

sfreq = 256  # in Hertz
info = mne.create_info(ch_names = ch_names, sfreq = sfreq)
raw = mne.io.RawArray(data, info)
raw.plot()
plt.show()
"""
plt.show()
Grafica el espectrograma con el eje X representando el tiempo
plt.specgram(data.flatten(), NFFT=256, Fs=256)
plt.show()
"""