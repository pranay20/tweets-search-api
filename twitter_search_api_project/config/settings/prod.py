from .base import *
from decouple import Csv

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

REST_FRAMEWORK = {
	'DEFAULT_RENDERER_CLASSES': [
		'rest_framework.renderers.JSONRenderer',
	]
}

print("Prod settings")

