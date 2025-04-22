from .serializers import RegisterSerializer
from .models import CustomUser
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsUser, IsAdmin, IsSuperAdmin

from django.shortcuts import get_object_or_404


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['role'] = user.role
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserTaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsUser]

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)


class UpdateTaskView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsUser]

    def put(self, request, pk):
        task = get_object_or_404(Task, pk=pk, assigned_to=request.user)

        if task.status != 'completed':
            serializer = TaskSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                if request.data.get('status') == 'completed':
                    if not request.data.get('completion_report') or not request.data.get('worked_hours'):
                        return Response({"error": "Completion Report and Worked Hours are required."}, status=400)
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        return Response({"message": "Task is already completed."})


class TaskReportView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)

        if request.user.role in ['admin', 'superadmin']:
            if task.status == 'completed':
                data = {
                    "completion_report": task.completion_report,
                    "worked_hours": task.worked_hours
                }
                return Response(data)
            return Response({"error": "Task is not completed yet."}, status=400)
        return Response({"error": "You do not have permission to view reports."}, status=403)
