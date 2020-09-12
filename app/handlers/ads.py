import logging
import random
import json

from flask_restful import Resource
from flask import request, jsonify, abort, redirect

from app.models.adslist import *

from app import flask_app

logger = logging.getLogger(__name__)

class Adsapi(Resource):

	def get(self):
		with open('app/models/adslist.py') as json_file:
			ADS_LIST = json.load(json_file)

		list_of_random_items = random.sample(ADS_LIST, 5)

		return jsonify(status=200, data=list_of_random_items)


	def post(self):

		try:
			request_data = request.get_json()
			ads_id = request_data['ads_id']
			count = request_data['count']

			with open('app/models/adslist.py') as json_file:
				ADS_LIST = json.load(json_file)

			for ads in ADS_LIST:
				if ads['ads_id'] == ads_id:
					ads['count'] += count
					data = ads
					break

			with open('app/models/adslist.py', 'w') as outfile:
				json.dump(ADS_LIST, outfile)
			return jsonify(status=200, msg="Count updated sucessfully ", data=data)
		except Exception as e:
			print(e)
			return jsonify(status=400, msg="error")


		