from django.urls import include, path
from django.views.generic.base import View
from django.views.generic import TemplateView
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
    path('api/task-list/', views.taskList, name='task_create'),
    path('api/task-create/', views.taskCreate, name='project_create'),
    path('api/task-detail/<str:pk>/', views.taskDetail, name='project_detail'),
    path('api/task-update/<str:pk>/', views.taskUpdate, name='project_update'),
    path('api/task-delete/<str:pk>/', views.taskDelete, name='project_delete'),
    path('docs/', TemplateView.as_view(template_name='documentation.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]