from django.urls import path
from .views import get_contacts, create_contacts

urlpatterns=[
    path('cont_get',get_contacts,name='cont'),
    path('create_cont',create_contacts,name='create'),

]