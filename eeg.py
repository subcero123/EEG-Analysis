import mne  # If this line returns an error, uncomment the following line
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import chart_studio.plotly as py

User_frame = pd.read_csv("/home/thor/Descargas/Uni/10moSemestre/Investigacion/AURA_FFT___2023-09-11___11;31;44.csv", sep=',', index_col=0) 
data= pd.DataFrame.to_numpy(User_frame, dtype= np.float64)

# assigning the channel type when initializing the Info object
ch_names = [ 
'Delta_FP1 eeg', 'Delta_FP2 eeg', 'Delta_F3 eeg', 'Delta_F7 eeg','Delta_F4 eeg', 'Delta_F8 eeg', 'Delta_T7 eeg', 'Delta_T8 eeg', 
'Theta_FP1 eeg', 'Theta_FP2 eeg', 'Theta_F3 eeg', 'Theta_F7 eeg', 'Theta_F4 eeg', 'Theta_F8 eeg', 'Theta_T7 eeg', 'Theta_T8 eeg', 
'Alpha_FP1 eeg', 'Alpha_FP2 eeg', 'Alpha_F3 eeg', 'Alpha_F7 eeg', 'Alpha_F4 eeg', 'Alpha_F8 eeg', 'Alpha_T7 eeg', 'Alpha_T8 eeg', 
'Beta_FP1 eeg', 'Beta_FP2 eeg', 'Beta_F3 eeg', 'Beta_F7 eeg', 'Beta_F4 eeg', 'Beta_F8 eeg', 'Beta_T7 eeg', 'Beta_T8 eeg', 
'Gamma_FP1 eeg', 'Gamma_FP2 eeg', 'Gamma_F3 eeg', 'Gamma_F7 eeg', 'Gamma_F4 eeg', 'Gamma_F8 eeg', 'Gamma_T7 eeg', 'Gamma_T8 eeg', 
'Event']

ch_types = ['eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg',
            'eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg',
            'eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg',
            'eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg',
            'eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg', 'eeg',
            'misc']

sampling_freq = 256  # in Hertz
data = User_frame.transpose().to_numpy()
info = mne.create_info(ch_names= ch_names, ch_types= ch_types, sfreq= sampling_freq)
User_raw = mne.io.RawArray(data, info)

print(User_raw)
print(User_raw.info)
start, stop = User_raw.time_as_index([100, 115])  # 100 s to 115 s data segment
picks = mne.pick_types(User_raw.info, meg='mag', exclude=[])
data, times = User_raw[picks[:10], start:stop]

plt.plot(times, data.T)
plt.xlabel('time (s)')
plt.ylabel('MEG data (T)')

update = dict(layout=dict(showlegend=True), data=[dict(name=User_raw.info['ch_names'][p]) for p in picks[:10]])
py.iplot_mpl(plt.gcf(), update=update)