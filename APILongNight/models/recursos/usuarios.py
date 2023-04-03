import sys, os
p = os.path.abspath('.')
sys.path.insert(1, p)

from models.recursos.cliente import cliente
from models.base.base_model import base_model

class usuarios(base_model):

    nombre_usuario: str
    password: str
    cliente: cliente