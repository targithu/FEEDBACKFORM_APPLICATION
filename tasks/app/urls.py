from django.urls import path
from . import views
from .views import FeedListView
urlpatterns = [
    path('',views.feedback,name='feedback'),
    path('feed/',FeedListView.as_view(),name='feed'),
]