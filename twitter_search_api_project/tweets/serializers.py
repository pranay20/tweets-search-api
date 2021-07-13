from rest_framework import serializers
from .models import Tweet

class TweetSerializer(serializers.ModelSerializer):

	class Meta:
		model = Tweet
		fields = ('id', 'text', 'username', 'created_at')
		read_only_fields = ('id', 'text', 'username', 'created_at')