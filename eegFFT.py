import numpy as np
import pandas as pd 
import mne
import matplotlib.pyplot as plt
from matplotlib.pyplot import specgram
#data = np.random.rand(256)




data = pd.read_csv("AURA_FFT___2023-09-11___11;42;36.csv",usecols=[*range(1, 42)],  skiprows=2, sep=',', index_col=0) 
data = data.transpose().to_numpy()

ch_names = [
'Delta_FP1 eeg', 'Delta_FP2 eeg', 'Delta_F3 eeg', 'Delta_F7 eeg','Delta_F4 eeg', 'Delta_F8 eeg', 'Delta_T7 eeg', 'Delta_T8 eeg', 
'Theta_FP1 eeg', 'Theta_FP2 eeg', 'Theta_F3 eeg', 'Theta_F7 eeg', 'Theta_F4 eeg', 'Theta_F8 eeg', 'Theta_T7 eeg', 'Theta_T8 eeg', 
'Alpha_FP1 eeg', 'Alpha_FP2 eeg', 'Alpha_F3 eeg', 'Alpha_F7 eeg', 'Alpha_F4 eeg', 'Alpha_F8 eeg', 'Alpha_T7 eeg', 'Alpha_T8 eeg', 
'Beta_FP1 eeg', 'Beta_FP2 eeg', 'Beta_F3 eeg', 'Beta_F7 eeg', 'Beta_F4 eeg', 'Beta_F8 eeg', 'Beta_T7 eeg', 'Beta_T8 eeg', 
'Gamma_FP1 eeg', 'Gamma_FP2 eeg', 'Gamma_F3 eeg', 'Gamma_F7 eeg', 'Gamma_F4 eeg', 'Gamma_F8 eeg', 'Gamma_T7 eeg', 'Gamma_T8 eeg', 
]


sfreq = 256  # in Hertz
info = mne.create_info(ch_names = ch_names, sfreq = sfreq)
raw = mne.io.RawArray(data, info)
raw.plot()
plt.show()
"""
specgram(data.flatten(), NFFT=256, Fs=256)
plt.show()"""