# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetAllData.as_view()),
    path('smokers/<region>/', views.GetSmokersByRegion.as_view()),
    path('getbyid/<int:id>/', views.GetDataById.as_view()),
]
