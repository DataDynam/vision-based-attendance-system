from .Load_Dataset import load_dataset
from .Get_Embeddings import get_embedding
from .SVM_Classifier import svm_train
from .Variables import model,TRAINING_IMAGES_PATH,EMBEDDINGS_PATH
import sys
import os
from os import listdir
from os.path import isdir
import numpy as np
from numpy import asarray
from numpy import savez_compressed
from numpy import load
import keras




def trainModel():
  # load train dataset
  print("STARTING THE TRAINING PROCESS...")
  print("DATA PATH IS:",TRAINING_IMAGES_PATH)
  
  if no