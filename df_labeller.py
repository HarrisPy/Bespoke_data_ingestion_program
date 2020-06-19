# -*- coding: utf-8 -*-
"""
PROGRAM TO INGEST AND LABEL ALL .CSV IN DIRECTORY TO DATARAMES
    
Created on Wed Jun 17 16:12:46 2020 @author: charris
"""

import pandas as pd
import glob
import os
import numpy as np

def autosetup(path):

    #path = 'C:/Users/charris/Desktop/datasets/world_bank_data/' # change as appropriate
    filenames = glob.glob(path + '/*.csv')

    # get filenames and clean
    names = [os.path.basename(x) for x in glob.glob(path + '/*.csv')]
    names = np.char.replace(names, '.csv', '')
    names = list(names) 

    dataframes = []

    for filename in filenames:   
        dataframes.append(pd.read_csv(filename))
  
    zip_object = zip(names, dataframes)
    data_dict = dict(zip_object)

    print('{} .csv files have been ingested:'.format(len(names)))
    print('{} datframes have been created and stored in dictionary: data_dict'\
          .format(len(names)))
    print('Dictionary_keys:')
    print(*names, sep = '\n')


# rename printed dictionary key as df1 ,df2 ...dfx for easy applciation
#assign a function to be called when needing reminder


