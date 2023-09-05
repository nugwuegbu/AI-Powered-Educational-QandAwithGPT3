from django.urls import path
from account import api

#initialize router to  register viewsets


#Determine API URLs
urlpatterns = [
    path('signup',api.CreateListUser.as_view(),name='user'),
    # path('signin',api.SignInUser.as_view(),name='signin'),
]