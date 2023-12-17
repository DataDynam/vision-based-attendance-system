from PIL import Image
import mtcnn
from mtcnn.mtcnn import MTCNN
from numpy import asarray
from numpy import load
from .Variables import detector


def extract_face(filename, required_size=(160, 160)):
  '''
  THIS FUNCTION TAKES (