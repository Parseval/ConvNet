# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 20:22:49 2017

@author: Steven
"""
import numpy as np
import sys
import os
import cntk as C

abs_path   = os.path.dirname(os.path.abspath(__file__))
data_path  = os.path.join(abs_path, "Data")
features_file = os.path.join(data_path, 'glob_0000.scp')
labels_file = os.path.join(data_path, 'glob_0000.mlf')
label_mapping_file = os.path.join(data_path, 'state.list')
outputdir = os.path.join(abs_path, "OUTPUT")
logdir = os.path.join(abs_path, "LOGS")
num_output_classes = 5

C.device.try_set_default_device(C.device.cpu())

# Ensure we always get the same amount of randomness
np.random.seed(0)

# Define the data dimensions
input_dim_model = (1, 200, 1)    # images are 28 x 28 with 1 channel of color (gray)
input_dim = 200*1                # used by readers to treat input data as a vector
num_output_classes = 5


# Define the reader for both training and evaluation action.
def create_reader(path, is_training, input_dim, label_dim):
    return C.io.MinibatchSource(C.io.CTFDeserializer(path, C.io.StreamDefs(
        features=C.io.StreamDef(field='features', shape=input_dim),
        labels=C.io.StreamDef(field='labels',   shape=label_dim)
    )), randomize=is_training, max_sweeps=C.io.INFINITELY_REPEAT if is_training else 1)


def main():
    print("test")
    # Load test data
    reader_test = create_reader(os.path.join(data_path, 'Test-28x28_cntk_text.txt'), False, input_dim, num_output_classes)
   
main()    