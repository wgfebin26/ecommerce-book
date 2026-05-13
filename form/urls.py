from django.urls import path
from .views import get_details, enter_details, login_det, get_id

urlpatterns=[

    path('all',get_details,name='all'),
    path('enter',enter_details,name='enter'),
    path('login',login_det,name='login'),
    path('getbyid/<int:pk>',get_id,name='get'),
]