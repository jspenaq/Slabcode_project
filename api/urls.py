from django.urls import include, path
from . import views

urlpatterns = [
    path('api/', views.apiOverview, name='api'),
]