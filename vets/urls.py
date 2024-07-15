from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from vets import views

router = routers.DefaultRouter()
router.register(r'vets', views.VetView, 'vets')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs/", include_docs_urls(title= "Vets API"))
]

## Generate our GET, POST, DELETE and PUT