from flask import Blueprint, request

api = Blueprint('api', __name__)

from . import authentication, users, audiobooks


