# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 20:22:49 2017

@author: Steven
"""
import soundfile as sf

data = []; #init global data var
sampleRate = 0;#inite global sample rate var

#load raw file
def load_raw(file):
    data, sampleRate = sf.read(file)
    

    