from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentDataSerializer
from .models import StudentData
from rest_framework.views import APIView


class StudentViewsData(ListCreateAPIView):
    queryset = StudentData.objects.all()
    serializer_class = StudentDataSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
