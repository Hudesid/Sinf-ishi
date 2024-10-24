from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('create/task/', views.create_task_view, name='create'),
    path('upload/task/<int:pk>/', views.update_view, name='update'),
    path('delete/task/<int:pk>/', views.delete_view, name='delete'),
    path('logout/', views.logout_view, name='logout')
]