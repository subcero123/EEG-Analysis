import numpy as np
import pandas as pd
from scipy.signal import butter, lfilter
import os

# Leer los datos desde el archivo CSV
file_path = "RAWNoEstimulo-2023-09-11-11:31:44.csv"
data = pd.read_csv(file_path, usecols=[*range(1, 9)], skiprows=1, sep=',')
data = data.transpose().to_numpy()

# Frecuencia de muestreo
sfreq = 256  # en Hertz

# Eliminación de ruido (puedes utilizar diferentes técnicas de filtrado)

# Definir las bandas de frecuencia de interés
bands = {
    'delta': (1, 4),
    'theta': (4, 8),
    'alpha': (8, 13),
    'beta': (13, 30),
    'gamma': (30, 50)
}

# Definir los nombres de los canales
channel_names = ['Fp1', 'Fp2', 'F3', 'F7', 'F4', 'F8', 'T7', 'T8']

def apply_bandpass_filter(data, lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    y = lfilter(b, a, data)
    return y

# Crear un DataFrame para los resultados
result_data = pd.DataFrame()

# Obtener el tiempo de la primera columna del archivo original
tiempo = pd.read_csv(file_path, skiprows=1, sep=',')
tiempo = tiempo.iloc[:, 0]

# Agregar el tiempo al DataFrame
result_data['TIEMPO'] = tiempo

# Calcular y guardar las amplitudes de las bandas para cada canal
for band_name, (lowcut, highcut) in bands.items():
    for channel_idx, channel_data in enumerate(data):
        # Aplicar filtro de banda
        filtered_data = apply_bandpass_filter(channel_data, lowcut, highcut, sfreq)
        
        # Calcular la FFT
        n = len(filtered_data)
        frequencies = np.fft.fftfreq(n, 1/sfreq)
        fft_values = np.fft.fft(filtered_data)

        # Calcular la magnitud de la FFT
        magnitude = np.abs(fft_values)
        
        # Calcular la amplitud en la banda de interés
        amplitud_tiempo = (2 / n) * magnitude

        # Redondear los valores a 3 decimales
        amplitud_tiempo = np.round(amplitud_tiempo, 3)

        # Crear una columna en el DataFrame para los resultados
        result_data[f'{band_name} ({channel_names[channel_idx]} Amplitud)'] = amplitud_tiempo



# Guardar el DataFrame como un archivo CSV
output_file = os.path.splitext(os.path.basename(file_path))[0] + "_FFT_bands.csv"
result_data.to_csv(output_file, index=False)
