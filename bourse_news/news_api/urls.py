from django.urls import path

from .views import NewsList


urlpatterns = [
    path('news/', NewsList.as_view(), name='news_list')
]
