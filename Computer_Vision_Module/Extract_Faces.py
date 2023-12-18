from PIL import Image
import mtcnn
from mtcnn.mtcnn import MTCNN
from numpy import asarray
from numpy import load
from .Variables import detector


def extract_face(filename, required_size=(160, 160)):
  '''
  THIS FUNCTION TAKES (ONE) IMAGE AS INPUT
  DETECT AND RETURN (ONE) FACE ARRAY RESIZED --> Using the MTCNN Detector
  '''
  image = Image.open(fil