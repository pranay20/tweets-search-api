# Standard application imports


# Django core imports
from django.core.management.base import (
	BaseCommand,
	CommandError
)

# Third party imports


# Local application imports
from tweets import utils


class Command(BaseCommand):
	help = "Fetches new tweets & stores in database"

	def handle(self, *args, **kwargs):
		print("Fetching new tweets...")
		utils.fetch_tweets()
		print("Saved tweets in database...")

