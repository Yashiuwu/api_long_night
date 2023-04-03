import sys, os
p = os.path.abspath('.')
sys.path.insert(1, p)

from models.base.base_model import base_model
from models.code import numbers

class recover_password_request(base_model):

    email: str
    user: str
    code: numbers
    date: str
    time: str
    status: str
