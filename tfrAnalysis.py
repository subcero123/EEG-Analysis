import mne
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos EEG desde el archivo CSV
data= np.genfromtxt("AURA_FFT___2023-09-11___11;42;36.csv", usecols=[*range(1,9)], skip_header=3, delimiter=',') 

# Crear un objeto RawArray a partir de los datos
info = mne.create_info(ch_names=['Canal1', 'Canal2', 'Canal3', 'Canal4', 'Canal5', 'Canal6', 'Canal7', 'Canal8'],
                       sfreq=256, ch_types='eeg')  # Ajusta sfreq según tu tasa de muestreo
raw = mne.io.RawArray(data[:, 1:].T, info)

# Configurar parámetros para el análisis de TFR
freqs = np.arange(4, 40, 2)  # Frecuencias a analizar
n_cycles = freqs / 2  # Ciclos de onda por frecuencia

# Realizar el análisis de TFR
tfr_multitaper = mne.time_frequency.tfr_multitaper(raw, freqs=freqs, n_cycles=n_cycles, time_bandwidth=2.0)

# Graficar el análisis de TFR para los 8 canales
tfr_multitaper.plot([0], baseline=(None, 0), mode='logratio', title='TFR Multitaper')
plt.show()
