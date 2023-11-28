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

print(raw_rest)
print(raw_rest.info["chs"])

# Obtener algunos datos de muestra
data, times = raw_rest[:, :100]  # Obtener los primeros 100 puntos de datos

# Imprimir los primeros 5 canales y sus valores de muestra
for i in range(5):
    print(f"Channel {i + 1} ({raw_rest.ch_names[i]}): {data[i]}")

# Imprimir información sobre las unidades de medida
print("Unidades de medida:")
for ch_info in raw_rest.info['chs']:
    print(f"Canal {ch_info['ch_name']}: {ch_info['unit']}")

# También puedes imprimir la unidad de medida de un canal específico, por ejemplo, el primer canal
primer_canal_info = raw_rest.info['chs'][0]
print("\nUnidad de medida del primer canal:", primer_canal_info['unit'])
