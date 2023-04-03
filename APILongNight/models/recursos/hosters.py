import sys, os
p = os.path.abspath('.')
sys.path.insert(1, p)

from models.establecimientos.local import local
from models.base.base_model import base_model

class hosters(base_model):

    nombre_usuario: str
    password: str
    hoster: local