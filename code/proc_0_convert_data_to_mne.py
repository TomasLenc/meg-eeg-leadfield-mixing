import os
import mne
import pandas as pd
import numpy as np
import re
import glob

os.makedirs('working', exist_ok=True)
data_folder = 'data/preprocessed'
file_list = os.listdir(data_folder)
subjects = [re.match('^sub-\d+', file).group() for file in file_list]

df = pd.read_csv('csv/name_match.csv')
print(len(df[df.INDI_ID.isin(subjects)])/len(df))
df[~df.INDI_ID.isin(subjects)].INDI_ID[:50]

missing = df[~df.INDI_ID.isin(subjects)].INDI_ID.to_list()

for subject in subjects:

    ec_file = 'working/%s_ec-raw.fif' % subject
    if not(os.path.exists(ec_file)):
        f_name = '%s/%s_EC.set' % (data_folder, subject)
        # if os.path.exists(f_name):
        raw = mne.io.read_raw_eeglab(f_name)
        raw.save(ec_file, overwrite=True)

    eo_file = 'working/%s_eo-raw.fif'
    if not(os.path.exists(eo_file)):
        f_name = '%s/%s_EO.set' % (data_folder, subject)
        raw = mne.io.read_raw_eeglab(f_name)
        raw.save(eo_file % subject, overwrite=True)