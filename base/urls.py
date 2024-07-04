from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

# URL patterns for the application
urlpatterns = [
    # Account-related URLs
    path('account/login/', views.CustomLoginView.as_view(), name='login'),
    path('account/logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('account/register/', views.RegisterUser.as_view(), name='register'),

    # Task-related URLs
    path('', views.TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task'),
    path('task-create/', views.TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', views.TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', views.TaskDelete.as_view(), name='task-delete'),
]
