from .Load_Faces import load_faces
from .Variables import EMPLOYEES_NAMES,EMBEDDINGS_PATH

import os
import numpy as np
from numpy import savez_compressed
from numpy import asarray
from numpy import load
from numpy import expand_dims
from numpy import asarray
from numpy import savez_compressed
from numpy import load
from os.path import isdir
from os import listdir



# load a dataset that contains one subdir for each class that in turn contains images
def load_dataset(directory):
  '''
  THIS FUNCTION TAKE DATABASE DIRECTORY WITH PERSONS' NAMES AS SUBDIRECTORY
  RETURNS LABELS AND NUMPY ARRAYS
  '''
  flag = None
  X, y = list(), list()
  # savez_compressed( EMBEDDINGS_PATH + '/Embeddings-dataset.npz', newTrainX,trainy)  # save arrays to one file in compressed format WILL BE USED WHEN WE ADD NEW PERSON TO THE DATABASE WE'LL LOAD THIS AND APPEND
  # data = load( EMBEDDINGS_PATH + '/Embeddings-dataset.np