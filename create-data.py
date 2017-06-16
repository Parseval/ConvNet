# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 20:22:49 2017

@author: Steven
"""
import numpy as np
import os

data = []; #init global data var
samplerate = 16000; #init global sample rate var
dir_path = os.path.dirname(os.path.realpath(__file__))
type_raw = '*.raw';
test_path = os.path.join(dir_path, "DATA", "TEST")
train_path = os.path.join(dir_path, "DATA", "TRAIN")
interval = 200

#Smoke Ganja

#load raw file
def load_raw(file):
    data = []
    print("File: " + file + " loading")
    data = np.fromfile(file)
    print("File: " + file + " loaded")
    print(len(data))
 
#Chop, Chop (chop, chop)
#20 second clips
def chop_block():
    
    chunks = np.array_split(data, interval)
    print(len(chunks))
    
    i = 0
    for chunk in chunks:
        print(chunk)
        i+=1
    return chunks
    
def main():
    #file_name = file_name
    #starting_value = starting_value
    #training_data = []
    print("Initialize; finding files")
    print(dir_path)
    print(test_path)
    print(train_path)
    
    for root, dirs, files in os.walk(train_path):
        for file in files:
            if file.endswith('.raw'):
                #print("files:")
                #print (root + "\\" +  file)
                load_raw(os.path.join(os.path.join(root, file)))
                chunks = chop_block()

    #print("File search complete.")
    
        #if len(training_data) >= 10000:
         #               np.save(file_name,training_data)
          #              print('SAVED')
           #             #print(training_data)
            #            training_data = []
             #           starting_value += 1
              #          file_name = './DATA/PROCESSED/TRAINING_DATA-{}.npy'.format(starting_value)
              
              
main()