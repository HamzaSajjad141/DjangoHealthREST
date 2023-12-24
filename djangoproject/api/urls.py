from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path('', views.index, name='index'),
    path('api/getalldata/', views.GetAllData.as_view(), name='GetAllData'),
    path('api/smokers/<str:region>/', views.GetSmokersByRegion.as_view(), name='GetSmokersByRegion'),
    path('api/getbyid/<int:id>/', views.GetDataById.as_view(), name='GetDataById'),
    path('api/create/', views.CreateData.as_view(), name='CreateData'),
    path('api/updatebyid/<int:id>/', views.UpdateDataById.as_view(), name='UpdateDataById'),
    path('api/deletebyid/<int:id>/', views.DeleteDataById.as_view(), name='DeleteDataById'),
    path('api/getbyagerange/<int:min_age>/<int:max_age>/', views.GetDataByAgeRange.as_view(), name='GetDataByAgeRange'),
    path('api/getbygender/<str:gender>/', views.GetDataByGender.as_view(), name='GetDataByGender'),
    path('api/getfiltereddatabycriteria/<int:min_age>/<int:max_age>/<path:min_bmi>/<path:max_bmi>/<str:smoking_status>/', views.GetFilteredDataByCriteria.as_view(), name='GetFilteredDataByCriteria'),
    path('api/getaveragecharges/<str:region>/', views.RetrieveAverageChargesByRegion.as_view(), name='RetrieveAverageChargesByRegion'),
]
