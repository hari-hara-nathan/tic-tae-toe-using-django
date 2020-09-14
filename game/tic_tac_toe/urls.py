from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('playgame/<int:pk>',views.playgame,name='playgame'),
    path('playagain',views.playagain,name='playagain')
]