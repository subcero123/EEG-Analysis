import numpy as np
import pandas as pd 
import mne
import matplotlib.pyplot as plt
from matplotlib.pyplot import specgram

data = pd.read_csv("AURA_FFT___2023-09-11___11;42;36.csv",usecols=[*range(1, 42)],  skiprows=2, sep=',', index_col=0) 
data = data.transpose().to_numpy()

# 1. Valor entero con incremento de 0.04
columna_1 = np.arange(1, 5601) * 0.04

# 2. Una columna llena de 0's
columna_2 = np.zeros(5600)

# 3. ID del 1 al 5600
columna_3 = np.ones(5600)

# Crear un arreglo 2D con las tres columnas
arreglo = np.column_stack((columna_1, columna_2, columna_3))
arreglo = arreglo.astype(int)

# Verificar las dimensiones del arreglo
print(arreglo.shape)  # Debe ser (5600, 3)

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
#raw.plot()
#plt.show()
"""
specgram(data.flatten(), NFFT=256, Fs=256)
plt.show()"""

epochs = mne.Epochs(raw, arreglo, event_repeated='merge')

# Asegúrate de que 'data' contiene tus datos y 'info' está definido correctamente desde el código anterior
power = mne.time_frequency.tfr_morlet(
    epochs, n_cycles=2, return_itc=False, freqs=256, decim=3
)

power.plot(["Gamma_FP1 eeg"])  # Cambia el canal a tu canal de interés
