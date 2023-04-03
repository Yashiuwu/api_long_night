import sys, os
p = os.path.abspath('.')
sys.path.insert(1, p)

#imports de modelos
from models.base.base_model import base_model
from models.recursos.horarios import horarios
from models.establecimientos.mesa import mesa

class mesero(base_model):

    nombre: str
    edad: int
    disponibilidad: bool
    fecha_contratacion: str
    numero_trabajador: int
    horarios: list[horarios]
    mesas: list[mesa]
