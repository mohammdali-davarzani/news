from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
#url patterns for news and sources
    path('news/sources/', NewsSources_ListView.as_view(), name="news_sources"),
    path('news/contents/', NewsContents_ListView.as_view(), name="news_contents"),
    path('add/source/', csrf_exempt(NewsSources_CreateView.as_view()), name="add_source"),
    path('add/news/', csrf_exempt(NewsContents_CreateView.as_view()), name='add_news'),
    path('delete/source/<int:pk>/', csrf_exempt(NewsSources_DeleteView.as_view()), name='delete_source'),
    path('delete/content/<int:pk>/', csrf_exempt(NewsContents_DeleteView.as_view()), name='delete_content'),
    path('upadate/source/<int:pk>/', csrf_exempt(NewsSources_UpdateView.as_view()), name='update_source'),
    path('update/content/<int:pk>/', csrf_exempt(NewsContents_UpdateView.as_view()), name='update_content'),

# url patterns for users
    path('users/', AuthUser_ListView.as_view(), name='users'),
    path('add/user/', csrf_exempt(AuthUser_CreateView.as_view()), name='add_user'),
    path('update/user/<int:pk>/', csrf_exempt(AuthUser_UpdateView.as_view()), name='update_user'),
]
