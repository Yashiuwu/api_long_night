import sys, os
p = os.path.abspath('.')
sys.path.insert(1, p)

from models.base.base_model import base_model
from models.menu.snacks import snacks

class combos(base_model):

    nombre: str
    incluidos: list[snacks]
    precio: float