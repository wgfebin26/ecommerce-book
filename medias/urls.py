from django.urls import path
from .views import media_get, create_media

urlpatterns=[
    path('get_img',media_get,name='image'),
    path('media_create',create_media,name='create')
]