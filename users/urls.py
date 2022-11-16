from django.urls import path
from .views import RegisterApiView


urlpatterns = [path("signup/", RegisterApiView.as_view(), name="register_api")]
