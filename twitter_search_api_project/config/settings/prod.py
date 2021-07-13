from .base import *
from decouple import Csv

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

print("Prod settings")

