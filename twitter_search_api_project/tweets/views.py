from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import (
	status,
	filters
)

from .models import Tweet
from .serializers import TweetSerializer

# Create your views here.
class TweetFetchView(APIView):

	def get(self, request):
		tweets_queryset = Tweet.fetch_all()
		serailizer = TweetSerializer(tweets_queryset, many=True)
		return Response(serailizer.data, status=status.HTTP_200_OK)

class TweetSearchView(generics.ListAPIView):
	search_fields = ['text']
	filter_backends = (filters.SearchFilter,)
	queryset = Tweet.fetch_all()
	serializer_class = TweetSerializer