from decouple import config

DEBUG = config('DEBUG', True)

if not DEBUG:
	from .prod import *

else:
	from .dev import *