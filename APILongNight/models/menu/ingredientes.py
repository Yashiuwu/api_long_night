import sys, os
p = os.path.abspath('.')
sys.path.insert(1, p)

#importacion modelo base
from models.base.base_model import base_model


class ingredientes(base_model):

    nombre: str
    
