

from django.urls import path

from company_app.views import CompanyViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api', CompanyViewSet, basename='company')
urlpatterns = router.urls

CompanyViewSet.as_view({'get': 'list'})
CompanyViewSet.as_view({'get': 'retrieve'})
CompanyViewSet.as_view({'post': 'create'})
CompanyViewSet.as_view({'put': 'update'})
CompanyViewSet.as_view({'delete': 'destroy'})

