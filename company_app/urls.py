

from django.urls import path

from company_app.views import CompanyViewSet, CompanyBankViewSet, CompanyAccounViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('company', CompanyViewSet, basename='company')
router.register('company-bank', CompanyBankViewSet, basename='company-bank')
router.register('company-account', CompanyAccounViewSet, basename='company-account')

urlpatterns = router.urls

