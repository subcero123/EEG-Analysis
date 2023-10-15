import numpy as np
import pandas as pd
import mne
import matplotlib.pyplot as plt
from mne.time_frequency import tfr_multitaper

# Cargar los datos desde el archivo CSV
data = pd.read_csv("AURA_FFT___2023-09-11___11;42;36.csv", usecols=[*range(1, 42)], skiprows=2, sep=',', index_col=0)
data = data.transpose().to_numpy()

ch_names = [
    'Delta_FP1 eeg', 'Delta_FP2 eeg', 'Delta_F3 eeg', 'Delta_F7 eeg', 'Delta_F4 eeg', 'Delta_F8 eeg', 'Delta_T7 eeg',
    'Delta_T8 eeg', 'Theta_FP1 eeg', 'Theta_FP2 eeg', 'Theta_F3 eeg', 'Theta_F7 eeg', 'Theta_F4 eeg', 'Theta_F8 eeg',
    'Theta_T7 eeg', 'Theta_T8 eeg', 'Alpha_FP1 eeg', 'Alpha_FP2 eeg', 'Alpha_F3 eeg', 'Alpha_F7 eeg', 'Alpha_F4 eeg',
    'Alpha_F8 eeg', 'Alpha_T7 eeg', 'Alpha_T8 eeg', 'Beta_FP1 eeg', 'Beta_FP2 eeg', 'Beta_F3 eeg', 'Beta_F7 eeg',
    'Beta_F4 eeg', 'Beta_F8 eeg', 'Beta_T7 eeg', 'Beta_T8 eeg', 'Gamma_FP1 eeg', 'Gamma_FP2 eeg', 'Gamma_F3 eeg',
    'Gamma_F7 eeg', 'Gamma_F4 eeg', 'Gamma_F8 eeg', 'Gamma_T7 eeg', 'Gamma_T8 eeg',
]

sfreq = 256  # en Hertz
info = mne.create_info(ch_names=ch_names, sfreq=sfreq)
raw = mne.io.RawArray(data, info)

# Definir épocas
# Calcular la duración de las épocas en segundos
n_samples = data.shape[1]  # Número de puntos de datos en tus registros EEG
sfreq = 256  # Frecuencia de muestreo en Hertz
tmin = 0  # Tiempo de inicio en segundos
epoch_duration = n_samples / sfreq  # Duración total de tus datos en segundos
event_id = None  # Puedes configurar esto para etiquetar las épocas si es necesario
# Crear un objeto Epochs utilizando la duración calculada
epochs = mne.EpochsArray(data[np.newaxis], info, tmin=tmin, event_id=event_id, duration=epoch_duration)

# Resto del código para calcular la TFR

# Crear un objeto TFR usando wavelets de Morlet
fmin = 1  # Frecuencia mínima
fmax = 30  # Frecuencia máxima
freqs = np.logspace(np.log10(fmin), np.log10(fmax), 20)  # Frecuencias de interés
n_cycles = freqs / 2  # Número de ciclos de la wavelet

tfr = tfr_multitaper(epochs, freqs=freqs, n_cycles=n_cycles, time_bandwidth=2.0, return_itc=False, n_jobs=1)

# Visualizar la TFR
tfr.plot([0], baseline=(None, 0), mode='logratio', title='TFR', show=False)

plt.show()
