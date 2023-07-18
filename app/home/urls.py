from django.urls import path
from .views import *

app_name = 'home'


urlpatterns = [
    path('', home_page, name='home_page'),
    path('about/', about_page, name='sobre'),
    path('contact/', contact_page, name='contato'),
]