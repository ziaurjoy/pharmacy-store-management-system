

from django.urls import path

from medicine_app.views import MedicineViewSet, MedicineDetailViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'medicine', MedicineViewSet, basename='medicine')
router.register(r'medicine-details', MedicineDetailViewSet, basename='medicine-details')

urlpatterns = router.urls

