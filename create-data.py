# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 20:22:49 2017

@author: Steven
"""
import numpy as np
import os
from matplotlib import pyplot as plt
from numpy.lib import stride_tricks
import wave as wav
from matplotlib.pyplot import specgram

starting_value = 0

dir_path = os.path.dirname(os.path.realpath(__file__))
type_raw = '*.raw';
test_path = os.path.join(dir_path, "DATA", "TEST")
train_path = os.path.join(dir_path, "DATA", "TRAIN")
chunk_size = 1024
samplerate = 16000; #init global sample rate var
cliptime = 5
bitspersample = 16
fft_size = 512
overlap_fac = 0


#Consider harvesting youtube videos to increase training data. Words arent 
#really important so long as I can label the independent speakers.

#This script will roll through /DATA/TRAIN and process files for use.
#File structure should be: /DATA/TRAIN/XXXX/YYYY WHERE:
#XXXX = a single source (person)
#YYYY = individual sample sources

#The resulting training data files will consist of a Numpy array of size 10
#Each index will represent an individual and will contain another array
#This second level array will contain the various sources for that individual
#Seperated into chunk_size chunks

def raw_to_wav(file, name, index):
    sep = '.'
    rest = name.split(sep, 1)[0]
    file_data = np.fromfile(file, dtype='uint8')
    #print(file_data)
    with wav.open('wav_{}_{}.wav'.format(rest, index), 'wb') as wavfile:
        print('{}'.format(index))
        wavfile.setparams((1, 2, samplerate, 0, 'NONE', 'NONE'))
        wavfile.writeframes(file_data)
    #return wavfile

#load raw file
def load_raw(file):
    file_data = []
    chunk_data = np.random.rand(chunk_size)
    #file_data = np.float32(file_data)
    file_data = np.fromfile(file, dtype='uint8')
    chunk_data = [file_data[x:x+chunk_size] for x in range(0, len(file_data), chunk_size)]
    #print(chunk_data)
    #print(file)
    return chunk_data

def load_wav(file):
    with wav.open(file, 'rb') as wavfile:
        return wavfile
    
def main():
    training_data = []
    dir_data = []
    specs = []
    #starting_value = 0
    #file_name = './DATA/PROCESSED/TRAINING_DATA-{}.npy'.format(starting_value)
    np.set_printoptions(threshold=np.inf)
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
                    """
                    if len(training_data) == 10:
                        np.save(file_name, training_data)
                        print('SAVED {}'.format(starting_value))
                        #print(training_data)
                        training_data = []
                        starting_value += 1
                        file_name = './DATA/PROCESSED/TRAINING_DATA-{}.npy'.format(starting_value)
                        """
                
                chunks = load_raw(os.path.join(os.path.join(root, file)))
                for chunk in chunks:
                    spec = chunk.specgram( NFFT=128, Fs=samplerate, noverlap=64)
                    show()
                    plot = spec.plot()
                    #print(spec)
                    for s in spec:
                        print(s)
                        s.plot()
                        input("Enter...........")
                #plotstft(wavy)
                #dir_data.append(load_raw(os.path.join(os.path.join(root, file))))
            
    #training_data.append(dir_data)
    #np.save(file_name, training_data)
    #print('SAVED {}'.format(starting_value))
    print('Done. Closing.')
                           
main()