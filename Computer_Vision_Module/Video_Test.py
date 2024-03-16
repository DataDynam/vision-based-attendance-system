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
from .Variables import EMBEDDINGS_PATH,detector,model,SVM_MODEL_PATH,PATH_TO_OUTPUT_VIDEOS_DIRECTORY,PATH_TO_OUTPUT_LOGFILE_DIRECTORY,PATH_TO_VIDEO_DIRECTORY,DETECTOR_CONFIDENCE,SVM_CONFIDENCE
from sklearn.preprocessing import LabelEncoder
from .Get_Embeddings import get_embedding


def video_test(video_path, svm_model):
  name = video_path[video_path.find("CAMERA"):]
  CAMERA_ID = int(re.search(r'\d+', name).group())
  data = load(EMBEDDINGS_PATH + '/Embeddings-dataset.npz')
  trainy = data['arr_1']
  out_encoder = LabelEncoder()
  out_encoder.fit(trainy)
  trainy = out_encoder.transform(trainy)
  
  
  entries = {'camera_id': [],
          'timestamp': [],
          'employee_name':[],
          'confidence':[],
          'x':[],
          'y':[],
          'width':[],
          'height':[]
          }
  df = DataFrame(entries)
  vidcap = cv2.VideoCapture(video_path)
  fps = int(vidcap.get(5))
  success = True
  fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
  out = cv2.VideoWriter(PATH_TO_OUTPUT_VIDEOS_DIRECT