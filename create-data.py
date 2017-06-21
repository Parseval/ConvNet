# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 20:22:49 2017

@author: Steven
"""
import numpy as np
import os

starting_value = 0

samplerate = 16000; #init global sample rate var
dir_path = os.path.dirname(os.path.realpath(__file__))
type_raw = '*.raw';
test_path = os.path.join(dir_path, "DATA", "TEST")
train_path = os.path.join(dir_path, "DATA", "TRAIN")
interval = 200

#Consider harvesting youtube videos to increase training data. Words arent 
#really important so long as I can label the independent speakers.

#This script will roll through /DATA/TRAIN and process files for use.
#File structure should be: /DATA/TRAIN/XXXX/YYYY WHERE:
#XXXX = a single source (person)
#YYYY = individual sample sources

#The resulting training data files will consist of a Numpy array of size 10
#Each index will represent an individual and will contain another array
#This second level array will contain the various sources for that individual

#load raw file
def load_raw(file):
    file_data = []
    file_data = np.fromfile(file)
    return file_data
    
def main():
    training_data = []
    dir_data = []
    starting_value = 0
    file_name = './DATA/PROCESSED/TRAINING_DATA-{}.npy'.format(starting_value)
    print("Initialize; finding files")
    print(dir_path)
    print(test_path)
    print(train_path)
    
    for root, dirs, files in os.walk(train_path):
        for index, file in enumerate(files):
            if file.endswith('.raw'):
                if index == 0:
                    print('----NEW DIRECTORY-----')
                    training_data.append(dir_data)
                    dir_data = []
                                        
                    if len(training_data) == 10:
                        np.save(file_name, training_data)
                        print('SAVED {}'.format(starting_value))
                        #print(training_data)
                        training_data = []
                        starting_value += 1
                        file_name = './DATA/PROCESSED/TRAINING_DATA-{}.npy'.format(starting_value)
               
                
                dir_data.append(load_raw(os.path.join(os.path.join(root, file))))
                
                
    training_data.append(dir_data)
    np.save(file_name, training_data)
    print('SAVED {}'.format(starting_value))
    print('Done. Closing.')
                           
main()