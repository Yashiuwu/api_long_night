import sys, os
p = os.path.abspath('.')
sys.path.insert(1, p)

#imports de modelos
from models.base.base_model import base_model
#importar clases del menu
from models.menu.platillos import platillos
from models.menu.snacks import snacks
from models.menu.combos import combos
from models.menu.refrescos import refrescos
from models.menu.naturales import naturales
from models.menu.cervezas import cervezas
from models.menu.licores import licores
from models.menu.vinos import vinos
from models.menu.coteles import cocteles

class menu(base_model):

    platillos: list[platillos]
    snacks: list[snacks]
    combos: list[combos]
    refrescos: list[refrescos]
    naturales: list[naturales]
    cervezas: list[cervezas]
    licores: list[licores]
    cocteles: list[cocteles]
    vinos: list[vinos]