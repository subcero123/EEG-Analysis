import pandas as pd
import numpy as np
import mne
from mne.time_frequency import psd_multitaper
import matplotlib.pyplot as plt
from transfreq import compute_transfreq_klimesch, compute_transfreq, compute_transfreq_minimum
from transfreq.viz import (plot_transfreq, plot_transfreq_klimesch, 
                           plot_clusters, plot_channels)
from transfreq.utils import read_sample_datapath

def cargar_datos(file_path, eeg_channels):
    df = pd.read_csv(file_path)

    data = df[eeg_channels].values.T
    sfreq = 256
    info = mne.create_info(ch_names=eeg_channels, sfreq=sfreq, ch_types='eeg')
    raw = mne.io.RawArray(data, info)

    return raw

def calcular_psd(raw, fmin, fmax, n_fft, n_tapers, tmin, tmax):
    psds, freqs = psd_multitaper(raw,tmin=tmin, tmax=tmax,fmin=fmin, fmax=fmax, n_jobs=1)
    return psds, freqs

def calcular_transfreq(psds, freqs, method, iterative=True):
    return compute_transfreq(psds, freqs, method=method, iterative=iterative)

def calcular_transfreq_klimesch(psds_activo, psds_pasivo, freqs):
    return compute_transfreq_klimesch(psds_activo, psds_pasivo, freqs)

def calcular_transfreq_minimum(psds, freqs):
    return compute_transfreq_minimum(psds, freqs)

def visualizar_resultados(psds, freqs, tfbox, title):
    fig = plt.figure(constrained_layout=True, figsize=(15, 10))
    subfigs = fig.subfigures(2, 1, wspace=0.1)

    ax1 = subfigs[0].subplots(1, 2)
    plot_transfreq(psds, freqs, tfbox, ax=ax1[0])
    plot_clusters(tfbox, ax=ax1[1])
    plt.suptitle(title)
    plt.show()

# Análisis activo
file_path_activo = '../../E2023-09-26___11;15;10/AURA_RAW___2023-09-26___11;15;10.csv'
eeg_channels_activo = ['Fp1', 'Fp2', 'F3', 'F7', 'F4', 'F8', 'T7', 'T8']

raw_activo = cargar_datos(file_path_activo, eeg_channels_activo)

# Análisis pasivo
file_path_pasivo = '../../NE2023-09-26___11;02;14/AURA_RAW___2023-09-26___11;02;14.csv'
eeg_channels_pasivo = ['Fp1', 'Fp2', 'F3', 'F7', 'F4', 'F8', 'T7', 'T8']

raw_pasivo = cargar_datos(file_path_pasivo, eeg_channels_pasivo)

# Define time range. The length of both recordings is set equal to the length of
# the shortest one. In this way we obtain the same frequency resolution when
# computing the corresponding power spectra by using the multitaper method.
# This is required for applying the Klimesch's method
tmin = 0
tmax = min(raw_activo.times[-1], raw_pasivo.times[-1])

psds_activo, freqs_activo = calcular_psd(raw_activo, tmin=tmin, tmax=tmax, fmin=1, fmax=50, n_fft=256, n_tapers=4)
psds_pasivo, freqs_pasivo = calcular_psd(raw_pasivo, tmin=tmin, tmax=tmax, fmin=1, fmax=50, n_fft=256, n_tapers=4)


# Calcular y visualizar resultados para todos los métodos
methods = [1, 2, 3, 4]

# Calcular y visualizar resultados para compute_transfreq_klimesch
tfbox_klimesch = calcular_transfreq_klimesch(psds_activo, psds_pasivo, freqs_activo)

# Inicializar listas para almacenar las diferencias
diferencias_activo = []
diferencias_pasivo = []


# Calcular las diferencias para cada método
for meth in methods:
    # Calcular la diferencia para el análisis activo
    tfbox_activo = calcular_transfreq(psds_activo, freqs_activo, method=meth)
    diff_activo = tfbox_activo["tf"] - tfbox_klimesch
    diferencias_activo.append(diff_activo)

    # Calcular la diferencia para el análisis pasivo
    tfbox_pasivo = calcular_transfreq(psds_pasivo, freqs_pasivo, method=meth)
    diff_pasivo = tfbox_pasivo["tf"] - tfbox_klimesch
    diferencias_pasivo.append(diff_pasivo)

# Convertir listas a matrices numpy
diferencias_activo = np.array(diferencias_activo)
diferencias_pasivo = np.array(diferencias_pasivo)


print(diferencias_activo)
# Crear un boxplot para el análisis activo
plt.figure(figsize=(10, 6))
plt.boxplot(diferencias_activo)
plt.title('Diferencia entre Métodos y Klimesch - Análisis Activo')
plt.ylabel('Diferencia')
plt.xlabel('Métodos')
plt.show()

# Calcular y visualizar resultados para compute_transfreq_minimum
tfbox_minimum_activo = calcular_transfreq_minimum(psds_activo, freqs_activo)
tfbox_minimum_pasivo = calcular_transfreq_minimum(psds_pasivo, freqs_pasivo)
