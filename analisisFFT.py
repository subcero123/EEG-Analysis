#Analisis de FFT y representación de cada canal  

import mne
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data= np.genfromtxt("AURA_FFT___2023-09-11___11;42;36.csv",  skip_header=3, delimiter=',') 

print(data)
# Extraer el tiempo y los valores EEG
tiempo = data[:, 0]

print(tiempo)
valores_eeg = data[:, 1:]

# Parámetros de la transformada de Fourier
n = len(valores_eeg)  # Número de puntos
sample_rate = 1  # Tasa de muestreo (ajusta según tus datos)

# Calcula la transformada de Fourier para cada canal
espectros = []
for canal in range(0,8):
    fft_result = np.fft.fft(valores_eeg[:, canal])
    freqs = np.fft.fftfreq(n, 1/sample_rate)
    espectros.append((freqs, np.abs(fft_result)))

# Graficar los espectros de frecuencia de los 8 canales en una sola figura
plt.figure(figsize=(12, 8))
for canal, (freqs, espectro) in enumerate(espectros):
    plt.subplot(4, 2, canal + 1)  # Crear 4x2 subplots para los 8 canales
    plt.plot(freqs, espectro)
    plt.title(f'Canal {canal + 1}')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Amplitud')

plt.tight_layout()
plt.show()

