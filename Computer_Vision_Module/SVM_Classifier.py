from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Normalizer
from sklearn.svm import SVC
import pickle
import os
from .Variables import SVM_MODEL_PATH


def svm_train(newTrainX, trainy )