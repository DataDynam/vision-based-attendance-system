from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Normalizer
from sklearn.svm import SVC
import pickle
import os
from .Variables import SVM_MODEL_PATH


def svm_train(newTrainX, trainy ):  
  in_encoder = Normalizer(norm='l2')
  newTrainX = in_encoder.transform(newTrainX)
  out_encoder = Labe