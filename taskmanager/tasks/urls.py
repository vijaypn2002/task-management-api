from django.urls import path
from .views import RegisterView, MyTokenObtainPairView, UserTaskListView, UpdateTaskView, TaskReportView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tasks/', UserTaskListView.as_view(), name='user-tasks'),
    path('tasks/<int:pk>/', UpdateTaskView.as_view(), name='update-task'),
    path('tasks/<int:pk>/report/', TaskReportView.as_view(), name='task-report'),
]
