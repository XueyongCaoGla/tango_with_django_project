from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    #new path mapping to the about() view
    path('about/', views.about, name='about'),
]
