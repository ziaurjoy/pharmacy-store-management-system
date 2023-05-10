

from django.urls import path

from company_app.views import CompanyViewSet, CompanyBankViewSet, CompanyAccounViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/viewset', CompanyViewSet, basename='company')
router.register(r'api/bank/viewset', CompanyBankViewSet, basename='company-bank')
router.register(r'api/account/viewset', CompanyAccounViewSet, basename='company-account')

urlpatterns = router.urls

