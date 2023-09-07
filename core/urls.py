from django.urls import path
from core import api



# app_name = 'core'
#API URLs
urlpatterns = [
    path('search',api.SearchAPIView.as_view(),name='search'),
]