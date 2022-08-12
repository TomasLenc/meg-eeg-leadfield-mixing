import pandas as pd
import os
import re

subjects = pd.read_csv("csv/name_match.csv")

input_path = 'working'
output_path = 'working2'

all_files = os.listdir(input_path)

filename_map = dict([(series.Initial_ID, series.INDI_ID) for idx, series in subjects.iterrows()])

import numpy as np


for file in all_files:
        
    idx, = np.where([pat in file for pat in subjects.Initial_ID.to_list()])
    
    new_file = file.replace(subjects.Initial_ID.iloc[idx].values.item(), 
                            subjects.INDI_ID.iloc[idx].values.item())

    cmd = f'cp working/{file} working2/{new_file}'
    print(cmd)
    os.system(cmd)