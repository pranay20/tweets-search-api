from django.urls import path
from .views import (
	TweetFetchView,
	TweetSearchView
)

urlpatterns = [
	path('', TweetSearchView.as_view(), name="search_tweets"),
	path('fetch', TweetFetchView.as_view(), name="fetch_tweets"),
]