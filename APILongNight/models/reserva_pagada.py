import os, sys
from bson import ObjectId
p = os.path.abspath('.')
sys.path.insert(1, p)

from models.base.base_model import base_model

class reserva_pagada(base_model):

    id_cliente: str
    id_reserva: str
    pay_date: str
    total_paid: float
