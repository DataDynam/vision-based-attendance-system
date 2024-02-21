import numpy as np
import cv2
import re
import progressbar
import pickle
from PIL import Image
from os import listdir
from os.path import isdir
from pandas import DataFrame
from numpy import asarray
from numpy import savez_compressed
from numpy import expand_dims
from numpy import load
from .Variables import EMBEDDINGS_PATH,detector,model,SVM_MODEL_PATH,PATH_TO_OUTPUT_VIDEOS_DIRECTORY,PATH_T