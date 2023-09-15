import mne  # If this line returns an error, uncomment the following line
# !easy_install mne --upgrade
import numpy as np
from mne.datasets import sample
import matplotlib.pyplot as plt
import chart_studio.plotly as py

data_path = sample.data_path()

raw_fname = '/home/thor/mne_data/MNE-sample-data/MEG/sample/sample_audvis_filt-0-40_raw.fif'
raw = mne.io.Raw(raw_fname, preload=False)
print(raw)
print(raw.info)
start, stop = raw.time_as_index([100, 115])  # 100 s to 115 s data segment
data, times = raw[:306, start:stop]
print(data.shape)
print(times.shape)
print(times.min(), times.max())
picks = mne.pick_types(raw.info, meg='mag', exclude=[])
print(picks)
picks = mne.pick_types(raw.info, meg='mag', exclude=[])
data, times = raw[picks[:10], start:stop]

raw.plot()
plt.show()