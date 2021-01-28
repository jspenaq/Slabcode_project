from django.urls import include, path
from django.views.generic.base import View
from . import views
from .views import UserCreate

urlpatterns = [
    path('api/', views.apiOverview, name='api'),
    path('register/', UserCreate.as_view(), name='user_register'),
    path('api/project-list/', views.projectList, name='project_list'),
    path('api/project-create/', views.projectCreate, name='project_create'),
    path('api/project-detail/<str:pk>/', views.projectDetail, name='project_detail'),
    path('api/project-update/<str:pk>/', views.projectUpdate, name='project_update'),
    path('api/project-delete/<str:pk>/', views.projectDelete, name='project_delete'),
]