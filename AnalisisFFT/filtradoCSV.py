import pandas as pd
from datetime import datetime

# Leer el archivo CSV
df = pd.read_csv('../Estimulo/AURA_RAW___2023-09-26___11;15;10.csv')
print(df)

# Extraer la parte de fecha y hora del formato existente
df['Time and date'] = df['Time and date'].str.extract(r'\[(.*?)\]')[0]

# Convierte la primera columna a un formato de fecha y hora
df['Time and date'] = pd.to_datetime(df['Time and date'], format="%H:%M:%S.%f %d/%m/%Y")

# Calcula la diferencia entre cada Time and date y el Time and date inicial
df['Time and date'] = (df['Time and date'] - df['Time and date'].iloc[0]).dt.total_seconds()

# Guarda el DataFrame modificado de vuelta en un nuevo archivo CSV
df.to_csv('RAWEstimulo-2023-09-11-11:15:10.csv', index=False)
