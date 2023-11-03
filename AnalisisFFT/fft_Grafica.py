import csv
import statistics
import matplotlib.pyplot as plt

def calcular_promedios_por_registro(nombre_archivo):
    try:
        promedios_por_registro = []

        with open(nombre_archivo, 'r', newline='') as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)
            encabezados = lector_csv.fieldnames

            for fila in lector_csv:
                valores = [float(fila[encabezado]) for encabezado in encabezados[1:]]  # Excluimos la primera columna
                suma_valores = sum(valores)
                promedio_registro = suma_valores / (len(encabezados)-1)
                promedios_por_registro.append(promedio_registro)

        return promedios_por_registro
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encontró.")
        return None

def calcular_promedios_por_grupo(promedios_registros, tamano_grupo):
    promedios_por_grupo = []
    grupo_actual = []

    for i, promedio in enumerate(promedios_registros, 1):
        grupo_actual.append(promedio)
        if i % tamano_grupo == 0:
            promedio_grupo = sum(grupo_actual) / len(grupo_actual)
            promedios_por_grupo.append(promedio_grupo)
            grupo_actual = []

    if grupo_actual:  # Para el último grupo si no es un múltiplo exacto de tamano_grupo
        promedio_grupo = sum(grupo_actual) / len(grupo_actual)
        promedios_por_grupo.append(promedio_grupo)

    return promedios_por_grupo



def graficar_promedios(promedios1, promedios2):
    # Crear un rango de índices para los puntos en los ejes x
    indices = range(1, len(promedios1) + 1)

    # Graficar los promedios de la primera lista en una gráfica separada (azul)
    plt.figure(1)
    plt.plot(indices, promedios1, 'bo', markersize=5)
    plt.xlabel('Grupo')
    plt.ylabel('Promedio')
    plt.title('Gráfico de Promedios - Lista 1')

    # Graficar los promedios de la segunda lista en otra gráfica separada (rojo)
    indices = range(1, len(promedios2) + 1)
    plt.figure(2)
    plt.plot(indices, promedios2, 'ro', markersize=5)
    plt.xlabel('Grupo')
    plt.ylabel('Promedio')
    plt.title('Gráfico de Promedios - Lista 2')

    # Mostrar ambas gráficas
    plt.show()



nombre_archivo = 'RAWNoEstimulo-2023-09-11-11:31:44_FFT_bands.csv'
promedios_registros1 = calcular_promedios_por_registro(nombre_archivo)
promedios_registros1 = calcular_promedios_por_grupo(promedios_registros1, tamano_grupo=200)

nombre_archivo = '../NE2023-09-11___11;31;44/AURA_FFT___2023-09-11___11;31;44.csv'
promedios_registros2 = calcular_promedios_por_registro(nombre_archivo)
promedios_registros2 = calcular_promedios_por_grupo(promedios_registros2, tamano_grupo=200)

# Graficar los promedios
graficar_promedios(promedios_registros1, promedios_registros2)

for i, promedio_grupo in enumerate(promedios_por_grupo, 1):
    print(f'Promedio del grupo {i}: {promedio_grupo}')

