from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path('', views.index, name='index'),
    path('getalldata/', views.GetAllData.as_view(), name='GetAllData'),
    path('smokers/<str:region>/', views.GetSmokersByRegion.as_view(), name='GetSmokersByRegion'),
    path('getbyid/<int:id>/', views.GetDataById.as_view(), name='GetDataById'),
    path('create/', views.CreateData.as_view(), name='CreateData'),
    path('updatebyid/<int:id>/', views.UpdateDataById.as_view(), name='UpdateDataById'),
    path('deletebyid/<int:id>/', views.DeleteDataById.as_view(), name='DeleteDataById'),
    path('getbyagerange/<int:min_age>/<int:max_age>/', views.GetDataByAgeRange.as_view(), name='GetDataByAgeRange'),
    path('getbygender/<str:gender>/', views.GetDataByGender.as_view(), name='GetDataByGender'),
    path('getfiltereddatabycriteria/<int:min_age>/<int:max_age>/<path:min_bmi>/<path:max_bmi>/<str:smoking_status>/', views.GetFilteredDataByCriteria.as_view(), name='GetFilteredDataByCriteria'),
    path('getaveragecharges/<str:region>/', views.RetrieveAverageChargesByRegion.as_view(), name='RetrieveAverageChargesByRegion'),
]
