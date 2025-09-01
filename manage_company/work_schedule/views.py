from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import work_schedule
from .serializers import work_scheduleSerializer

# Create your views here.
class createWork_scheduleView(APIView):
    def post(self, request):
        employee_id = request.data.get('employee_id')
        work_day = request.data.get('work_day')
        shift = request.data.get('shift')
        
        if not all([employee_id, work_day, shift]):
            return Response({
                "status": 400,
                "message": "Missing required fields",
                "data": None
            }, status=status.HTTP_400_BAD_REQUEST)
            
        queryset = work_schedule.objects.filter(employee_id=employee_id, work_day=work_day)   
        
        if queryset.exists():
            shedule = queryset.first()
            shedule.shift = shift
            shedule.save()
            
            serializer = work_scheduleSerializer(shedule)
            response = {
                "status": 200,
                "message": "Work schedule updated successfully",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            serializer = work_scheduleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                response = {
                    "status": 201,
                    "message": "New work schedule created successfully",
                    "data": serializer.data
                }
                return Response(response, status=status.HTTP_201_CREATED)
            
            response = {
                "status": 400,
                "message": "Work schedule creation failed",
                "errors": serializer.errors
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
            