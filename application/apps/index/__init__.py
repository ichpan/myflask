from flask import Blueprint

index_blueprint = Blueprint("index_blueprint", __name__)

from application.apps.index.view import *
