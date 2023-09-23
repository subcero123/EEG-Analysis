import numpy as np
import pandas as pd 
import mne
import matplotlib.pyplot as plt
from matplotlib.pyplot import specgram
#data = np.random.rand(256)

# Intervalo de muestreo en segundos
sampling_interval = 0.002e-3  # 0.002 ms en segundos

# Calcula la frecuencia de muestreo (Fs) en Hz
Fs = 1 / sampling_interval



data = pd.read_csv("AURA_RAW___2023-09-11___11;31;44.csv",usecols=[*range(1, 9)],  skiprows=1, sep=',') 
data = data.to_numpy()
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
#specgram(data.flatten(), Fs=256)
#plt.show()

# Duración total en segundos
duracion_total_segundos = 4 * 60  # 4 minutos

# Intervalo de muestreo en segundos
intervalo_muestreo = 0.002  # 0.002 segundos

# Cantidad total de puntos de datos
total_puntos_datos = int(duracion_total_segundos / intervalo_muestreo)

# Vector de tiempo en segundos
tiempo = np.arange(0, duracion_total_segundos, intervalo_muestreo)

# Grafica el espectrograma con el eje X representando el tiempo
plt.specgram(data.flatten(), NFFT=256, Fs=256)
plt.xlabel('Tiempo (s)')
plt.ylabel('Frecuencia (Hz)')
plt.show()