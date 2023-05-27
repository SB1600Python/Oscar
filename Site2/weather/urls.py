from django.urls import path
from weather.views import search_wether


urlpatterns = [
    path('', search_wether, name='weather')
]
