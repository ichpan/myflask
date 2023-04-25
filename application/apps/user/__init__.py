from flask import Blueprint

user_blueprint = Blueprint("user_blue", __name__)

from application.apps.user.view import *
