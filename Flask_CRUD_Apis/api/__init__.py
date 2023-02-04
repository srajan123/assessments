from app import app
from .contacts import *
from flask_restful import Api


apis = Api(app)

apis.add_resource(Items, '/')
apis.add_resource(Item, '/<int:pk>')