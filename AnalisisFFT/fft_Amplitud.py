import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Leer los datos desde el archivo CSV
file_path = "RAWNoEstimulo-2023-09-11-11:31:44.csv"
data = pd.read_csv(file_path, usecols=[*range(1, 9)], skiprows=1, sep=',')
data = data.transpose().to_numpy()

# Frecuencia de muestreo
sfreq = 256  # en Hertz

# Eliminación de ruido (puedes utilizar diferentes técnicas de filtrado)
# Ejemplo de filtrado paso bajo:
from scipy.signal import butter, lfilter

def butter_lowpass(cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

def butter_highpass(cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y


# Aplicar el filtro paso bajo
cutoff_frequency = 30  # Frecuencia de corte en Hz
filtered_data = butter_lowpass_filter(data, cutoff_frequency, sfreq)


# Calcular la FFT y visualizar cada canal en la misma ventana
n = len(filtered_data[0])
frequencies = np.fft.fftfreq(n, 1/sfreq)
fft_values = np.fft.fft(filtered_data)



# Visualizar la FFT de cada canal en una sola figura con zoom independiente
fig, axs = plt.subplots(4, 2, figsize=(12, 8))
axs = axs.ravel()

for i in range(len(filtered_data)):
    magnitude = np.abs(fft_values[i])
    axs[i].plot(frequencies, magnitude)
    axs[i].set_title(f'Canal {i+1}')
    axs[i].set_xlabel('Frecuencia (Hz)')
    axs[i].set_ylabel('Magnitud')
    axs[i].grid()
    axs[i].set_xlim(-5, 5)
    #axs[i].set_ylim(0, 1000)# Establece un rango de visualización por defecto (puedes ajustar esto)

plt.tight_layout()
plt.show()

"""
# Obtener el tiempo de la primera columna del archivo original
tiempo = pd.read_csv(file_path, skiprows=1, sep=',')
tiempo = tiempo.iloc[:, 0]

# Crear un DataFrame con los datos de la FFT
fft_data = pd.DataFrame({'TIEMPO': tiempo})
for i in range(len(filtered_data)):
    magnitude = np.abs(fft_values[i])
    amplitud_tiempo = (2 / n) * magnitude
    fft_data_amplitud[f'Canal {i+1} (Amplitud)'] = amplitud_tiempo


# Guardar el DataFrame como un archivo CSV
output_file = os.path.splitext(os.path.basename(file_path))[0] + "_FFT.csv"
fft_data.to_csv(output_file, index=False)"""