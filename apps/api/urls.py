from django.urls import path, include
from rest_framework import routers
from apps.api.views import AnimalViewSet, AnimalweightViewSet, GetEstimatedTotalAnimalWeight
router = routers.DefaultRouter()
router.register('animal', AnimalViewSet, base_name='animal')

urlpatterns = [ 
    path('',  include(router.urls)),
    path('animal-weight/<int:unique_id>/', AnimalweightViewSet.as_view(), name='AnimalView'),
    path('animal-total-weight/', GetEstimatedTotalAnimalWeight.as_view(), name='AnimalTotalWeightView')


]