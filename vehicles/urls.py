from django.urls import path
from .views import VehicleList,VehicleDetail,VehicleCreate,VehicleUpdate,VehicleDelete

urlpatterns=[
    path('',VehicleList.as_view(),name='vehicles'),
    path('vehicle/<int:pk>/',VehicleDetail.as_view(),name='details'),
    path('add-vehicle/',VehicleCreate.as_view(),name='add-vehicle'),
    path('update-vehicle/<int:pk>/',VehicleUpdate.as_view(),name='update-vehicle'),
    path('delete-vehicle/<int:pk>/',VehicleDelete.as_view(),name='delete-vehicle'),
]