from django.contrib import admin
from django.urls import path
from .views import CarApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/car/', CarApiView.as_view(), name='car')
]