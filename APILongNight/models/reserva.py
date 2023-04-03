import sys, os
p = os.path.abspath('.')
sys.path.insert(1, p)

#imports de modelos
from models.base.base_model import base_model
from models.establecimientos.local import local
from models.recursos.usuarios import usuarios
from models.recursos.horarios import horarios

#clase reserva para genera el json
class reserva(base_model):

    cliente: usuarios
    local: local
    numero_personas: int
    horario_reserva: horarios
    peticiones_: str
