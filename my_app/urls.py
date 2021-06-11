from django.urls import path

from . import views

app_name="my_app" #this is for enabling the : option
urlpatterns = [
    path('home/', views.home, name='home'),
    path('predict/', views.predict, name='predict'),
]



