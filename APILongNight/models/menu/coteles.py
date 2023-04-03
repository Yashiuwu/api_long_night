import sys, os
p = os.path.abspath('.')
sys.path.insert(1, p)

from models.base.base_model import base_model
from models.menu.licores import licores
from models.menu.ingredientes import ingredientes
from models.menu.refrescos import refrescos
from models.menu.naturales import naturales

class cocteles(base_model):

    nombre: str
    licores: list[licores]
    ingredientes: list[ingredientes]
    bebidas: list[refrescos, naturales]
    