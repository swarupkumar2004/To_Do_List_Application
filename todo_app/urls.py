# todo_app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, task_list_view, mark_complete, delete_task

router = DefaultRouter()
router.register(r'tasks-api', TaskViewSet, basename='task')

urlpatterns = [
    # Web views
    path('', task_list_view, name='task_list'),
    path('complete/<int:task_id>/', mark_complete, name='mark_complete'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),

    # API views (under /api/ to avoid conflict)
    path('api/', include(router.urls)),

    #path('tasks/', include('todo_app.urls')),
]
