from django.db import models
from django.db import connection

# Create your models here.
class Tweet(models.Model):
	text = models.CharField(max_length=300)
	username = models.CharField(max_length=50)
	created_at = models.DateTimeField()

	@classmethod
	def create(cls, tweet_data):
		tweet = cls.objects.create(**tweet_data)

	@classmethod
	def fetch_all(cls):
		tweet_queryset = cls.objects.all()
		return tweet_queryset

	@classmethod
	def delete_all(cls):
		pass
		# cls.objects.all().delete()
		# cursor = connection.cursor()
		# cursor.execute("DELETE FROM  `tweets_tweet`;")

	def get_text(self):
		return self.text

	def __str__(self):
		return self.get_text()
