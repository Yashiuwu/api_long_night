import sys, os
p = os.path.abspath('.')
sys.path.insert(1, p)

from models.base.base_model import base_model

class fotos(base_model):

    file_name: str
    location: str