# quiz/urls.py
from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home_view, name='home'), 
    path('quiz/', views.quiz_view, name='quiz_view'),  
    path('results/', views.results_view, name='results_view'),  
]
