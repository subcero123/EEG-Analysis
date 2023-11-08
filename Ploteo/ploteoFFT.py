import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Lee el archivo CSV
df = pd.read_csv('Sadya/AURA_FFT_Subject1_Filtered.csv')

# Extrae los minutos y segundos del campo 'Time and date'
df['Time and date'] = pd.to_datetime(df['Time and date'], format='[%H:%M:%S.%f %d/%m/%Y]')
df['Minutes'] = df['Time and date'].dt.minute
df['Seconds'] = df['Time and date'].dt.second

# Define los grupos de columnas a graficar
column_groups = [
    ["Fp1_Delta", "Fp1_Theta", "Fp1_Alpha", "Fp1_Beta", "Fp1_Gamma"],
    ["F3_Delta", "F3_Theta", "F3_Alpha", "F3_Beta", "F3_Gamma"],
    ["F4_Delta", "F4_Theta", "F4_Alpha", "F4_Beta", "F4_Gamma"],
    ["Fz_Delta", "Fz_Theta", "Fz_Alpha", "Fz_Beta", "Fz_Gamma"],
    ["Cz_Delta", "Cz_Theta", "Cz_Alpha", "Cz_Beta", "Cz_Gamma"],
    ["Pz_Delta", "Pz_Theta", "Pz_Alpha", "Pz_Beta", "Pz_Gamma"],
    ["P3_Delta", "P3_Theta", "P3_Alpha", "P3_Beta", "P3_Gamma"],
    ["P4_Delta", "P4_Theta", "P4_Alpha", "P4_Beta", "P4_Gamma"]
]

# Crea 8 subplots (4 en el lado izquierdo y 4 en el lado derecho)
fig, axs = plt.subplots(4, 2, figsize=(12, 8))

# Configura los títulos
titles = ["Fp1", "F3", "F4", "Fz", "Cz", "Pz", "P3", "P4"]

# Genera las gráficas para cada grupo de columnas
for i in range(8):
    row = i // 2
    col = i % 2
    ax = axs[row, col]
    for column in column_groups[i]:
        ax.plot(df['Minutes'] + df['Seconds'] / 60, df[column], label=column)
    ax.set_title(titles[i])
    ax.legend(loc='best')
    ax.set_xlabel("Tiempo (minutos)")
    ax.set_ylabel("Valor")
    ax.grid(True)

# Ajusta la distribución de los subplots
plt.tight_layout()

# Muestra las gráficas
plt.show()