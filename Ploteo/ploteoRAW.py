import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Lee el archivo CSV
data = pd.read_csv('Sadya/AURA_RAW___2023-06-30___13;02;27.csv', usecols=['Time and date', 'Fp1', 'F3', 'F4', 'Fz', 'Cz', 'Pz', 'P3', 'P4'])

# Extrae los minutos y segundos del campo 'Time and date'
data['Time and date'] = pd.to_datetime(data['Time and date'], format='[%H:%M:%S.%f %d/%m/%Y]')
data['Minutes'] = data['Time and date'].dt.minute
data['Seconds'] = data['Time and date'].dt.second
# Extrae los campos de interés
channels = ['Fp1', 'F3', 'F4', 'Fz', 'Cz', 'Pz', 'P3', 'P4']

# Crea una figura para los gráficos
plt.figure(figsize=(12, 8))

# Itera a través de los canales y crea un gráfico para cada uno
for channel in channels:
    plt.plot(data['Minutes'] * 60 + data['Seconds'], data[channel], label=channel)

# Configura el título y las etiquetas de los ejes
plt.title('Gráfico EEG de Canales')
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Amplitud')
plt.legend()

# Muestra el gráfico
plt.show()