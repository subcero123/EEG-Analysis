import numpy as np
import pandas as pd

# Leer los datos desde el archivo original omitiendo la primera columna
file_path = "../NE2023-09-11___11;31;44/AURA_FFT___2023-09-11___11;31;44.csv"
data = pd.read_csv(file_path, skiprows=2, sep=',', usecols=range(1, 41))

# Dividir el archivo original en grupos de 500 registros
group_size = 500
groups = [data[i:i + group_size] for i in range(0, len(data), group_size)]

# Crear una lista para almacenar los DataFrames de resultados
result_data_list = []
# Calcular las estadísticas para cada grupo y agregarlas al DataFrame de resultados
for group in groups:
    group_stats = pd.DataFrame({
        'Promedio': group.mean().mean(),
        'Desviacion Estandar': group.mean().std(),
        'Mediana': group.mean().median(),
        'Rango Intercuartil': group.mean().quantile(0.75) - group.mean().quantile(0.25),
        'Min': group.mean().min(),
        'Max': group.mean().max()
    }, index=[0])
    result_data_list.append(group_stats)

# Concatenar los DataFrames de resultados en un solo DataFrame
result_data = pd.concat(result_data_list)
result_data = result_data.round(3)

# Guardar el DataFrame de resultados como un archivo CSV
output_file = file_path.split(".")[0] + "_Promedios.csv"
result_data.to_csv(output_file, index=False)
