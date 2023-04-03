import sys, os
p = os.path.abspath('.')
sys.path.insert(1, p)

#imports de modelos
from models.establecimientos.mesa import mesa
from models.recursos.mesero import mesero
from models.recursos.horarios import horarios
from models.recursos.fotos import fotos
#from models.menu.menu import menu
from models.base.base_model import base_model

class local(base_model):

    tipo: str
    nombre: str
    direccion: str
    latitud: str
    longitud: str
    telefono: str
    email: str
    descripcion: str
    mesas: list[mesa]
    #menu: menu
    meseros: list[mesero]
    horarios: list[horarios]
    fotos_establecimiento: fotos