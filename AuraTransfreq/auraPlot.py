# -*- coding: utf-8 -*-
"""
Authomatic computation of the transition frequency
==================================================
This example shows how to use transfreq for computing the alpha-to-theta
transition frequency when only resting-state data are available.
The result is compared with that obtained by using the classical
Klimesch's method.
"""

import mne
from transfreq import compute_transfreq_klimesch, compute_transfreq
from transfreq.viz import (plot_transfreq, plot_transfreq_klimesch, 
                           plot_clusters, plot_channels)
from transfreq.utils import read_sample_datapath
import os.path as op
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def cargar_datos(file_path, eeg_channels):
    df = pd.read_csv(file_path)

    data = df[eeg_channels].values.T
    sfreq = 256
    info = mne.create_info(ch_names=eeg_channels, sfreq=sfreq, ch_types='eeg')
    raw = mne.io.RawArray(data, info)

    return raw


def calcular_psd(raw, fmin, fmax, n_fft, n_tapers):
    psds, freqs = mne.time_frequency.psd_multitaper(raw,fmin=fmin, fmax=fmax, n_jobs=1)
    return psds, freqs



# Define path to the data
subj = 'transfreq_sample'
data_folder = read_sample_datapath()
f_name_rest = op.join(data_folder, '{}_resting.fif'.format(subj))
f_name_task = op.join(data_folder, '{}_evoked.fif'.format(subj))

# Load resting state data
raw_rest = mne.io.read_raw_fif(f_name_rest)
raw_rest = raw_rest.pick_types(eeg=True, exclude=raw_rest.info['bads'] + ['TP9', 'TP10', 'FT9', 'FT10'])

# Load data recorded during task execution
raw_task = mne.io.read_raw_fif(f_name_task)
raw_task = raw_task.pick_types(eeg=True, exclude=raw_task.info['bads'] + ['TP9', 'TP10', 'FT9', 'FT10'])

# List of good channels
tmp_idx = mne.pick_types(raw_rest.info, eeg=True, exclude='bads')
ch_names_rest = [raw_rest.ch_names[ch_idx] for ch_idx in tmp_idx]

tmp_idx = mne.pick_types(raw_task.info, eeg=True, exclude='bads')
ch_names_task = [raw_task.ch_names[ch_idx] for ch_idx in tmp_idx]

# Define time range. The length of both recordings is set equal to the length of
# the shortest one. In this way we obtain the same frequency resolution when
# computing the corresponding power spectra by using the multitaper method.
# This is required for applying the Klimesch's method
tmin = 0
tmax = min(raw_rest.times[-1], raw_task.times[-1])

# Compute power spectra
n_fft = 512*2
bandwidth = 1
fmin = 2
fmax = 30

sfreq = raw_rest.info['sfreq']
n_per_seg = int(sfreq*2)


# Análisis activo
file_path_activo = '../../E2023-09-26___11;15;10/AURA_RAW___2023-09-26___11;15;10.csv'
eeg_channels_activo = ['Fp1', 'Fp2', 'F3', 'F7', 'F4', 'F8', 'T7', 'T8']

raw_activo = cargar_datos(file_path_activo, eeg_channels_activo)
psds_activo, freqs_activo = calcular_psd(raw_activo, fmin=1, fmax=50, n_fft=256, n_tapers=4)


# Define channel positions
ch_locs_rest = np.zeros((len(eeg_channels_activo), 3))
print(raw_rest.info['chs'])

# Obtener la información de los canales del objeto raw_rest
chs_info = raw_rest.info['chs']
# Iterar sobre los canales activos
for ii, ch_name in enumerate(eeg_channels_activo):
    # Buscar el canal en la información de canales
    for ch_info in chs_info:
        if ch_info['ch_name'] == ch_name:
            # Asignar la ubicación al arreglo
            print(ch_info['ch_name'])
            print(ch_info['loc'][:3])
            ch_locs_rest[ii, :] = ch_info['loc'][:3]
            break  # Salir del bucle interno si se encuentra el canal

###########################################################################
# Compute the transition frequency with the default clustering method
tfbox = compute_transfreq(psds_activo, freqs_activo, ch_names=eeg_channels_activo, method=3)

###########################################################################
# Plot results

fig = plt.figure(constrained_layout=True, figsize=(15, 10))
subfigs = fig.subfigures(2, 1, wspace=0.1)

ax1 = subfigs[0].subplots(1, 2)
# Plot estimated transition frequency
plot_transfreq(psds_activo, freqs_activo, tfbox, ax=ax1[0])
# Plot results of the clustering approach
plot_clusters(tfbox, ax=ax1[1])
# Plot locations of the two channels groups
plot_channels(tfbox, ch_locs_rest, subfig=subfigs[1])
plt.show()