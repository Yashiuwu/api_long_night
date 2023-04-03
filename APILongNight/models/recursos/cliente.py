import sys, os
p = os.path.abspath('.')
sys.path.insert(1, p)

#imports de modelos
from models.base.base_model import base_model
from models.recursos.fotos import fotos

class cliente(base_model):

    tipo: str
    nombre: str
    telefono: str
    email: str
    foto_perfil: fotos
    num_doc_identificacion: str
    pic_doc_iden: fotos
    fecha_nacimiento: str
    genero: str