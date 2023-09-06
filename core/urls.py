from django.urls import path
from core import api




#API URLs
urlpatterns = [
    path('search',api.SearchAPIView.as_view(),name='search'),
]