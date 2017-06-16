# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 20:22:49 2017

@author: Steven
"""
import soundfile as sf
import numpy as np
import glob
import os
import path

data = []; #init global data var
samplerate = 0;#init global sample rate var
type_raw = '*.raw';
test_path = './DATA/TEST'

#Smoke Ganja

#load raw file
def load_raw(file):
    data, sampleRate = sf.read(file)
 
#Chop, Chop (chop, chop)
#20 second clips
def chop_block(file, interval):
    return chunks = [file[i:i+interval] for i in range(0, len(file), interval)]
    
def main(file_name, starting_value):
    file_name = file_name
    starting_value = starting_value
    training_data = []
    
    for filename in glob.glob(os.path.join(path, type_raw)):
        #iterates through directory "path" for files of type raw
        load_raw(os.path.join(os.path.join(path, filename)))
        
        if len(training_data) == 500:
                        np.save(file_name,training_data)
                        print('SAVED')
                        #print(training_data)
                        training_data = []
                        starting_value += 1
                        file_name = './DATA/PROCESSED/TRAINING_DATA-{}.npy'.format(starting_value)
    