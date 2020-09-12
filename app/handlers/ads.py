import logging
import random
import string

from flask_restful import Resource
from flask import request, jsonify, abort, redirect

from app.models.adslist import *

from app import flask_app

logger = logging.getLogger(__name__)

class Adsapi(Resource):

	def get(self):

		list_of_random_items = random.sample(ADS_LIST, 5)

		return jsonify(status=200, data=list_of_random_items)

		