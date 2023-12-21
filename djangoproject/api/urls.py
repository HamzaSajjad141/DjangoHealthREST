from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetAllData.as_view()),
    path('smokers/<region>/', views.GetSmokersByRegion.as_view()),
    path('getbyid/<int:id>/', views.GetDataById.as_view()),
    path('create/', views.CreateData.as_view()),
    path('updatebyid/<int:id>/', views.UpdateDataById.as_view()),
    path('deletebyid/<int:id>/', views.DeleteDataById.as_view()),
    path('getbyagerange/<int:min_age>/<int:max_age>/', views.GetDataByAgeRange.as_view(),),
    path('getbygender/<str:gender>/', views.GetDataByGender.as_view()),
]
