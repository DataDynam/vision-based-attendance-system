from .Variables import EMBEDDINGS_PATH, SVM_MODEL_PATH,SVM_CONFIDENCE, model
from .Get_Embeddings import get_embedding
import pickle
import cv2
import numpy as np
from numpy import asarray
from numpy import savez_compressed
from numpy import load
from numpy import expand_dims
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Normalizer
from PIL import Image
import mtcnn
from mtcnn.mtcnn import MTCNN


detector = MTCNN() # Creating instance from the class MTCNN

def multiple_faces(filename, required_size=(160, 160)):
  data = load( EMBEDDINGS_PATH + '/Embeddings-dataset.npz')
  trainy = data['arr_1']
  out_encoder = LabelEncoder()
  out_encoder.fit(trainy)
  trainy = out_encoder.transform(trainy)
  
  # LOAD THE MODEL
  print("TESTING ON AN IMAGE")
  print("LOADING THE MODEL...")
  svm_model = pickle.load(open(SVM_MODEL_PATH +  '/svm_model.sav', 'rb'))
  print("DONE LOADING THE MODEL!")
  print("LOADING THE IMAGE...")
  image = Image.open(filename) # load image from file
  print("DONE LOADING THE IMAGE!")
  image = image.convert('RGB') # convert to RGB, if needed
  pixels = asarray(image) # convert to array
  results = detector.detect_faces(pixels) # detect faces in the image
  
  if(len(results) == 0):
    return False
  
  
  # LOOP OVER ALL FOUND FACE AND ANNOTATE THEM
  for i in r