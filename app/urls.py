from app.handlers.test import Hello
from app.handlers.ads import Adsapi
from app import api


api.add_resource(Hello, '/hello')
api.add_resource(Adsapi, '/ads')
