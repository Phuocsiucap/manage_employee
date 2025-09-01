from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from .models import Employee
from .serializers import UserSerializer
class EmployeePagination(PageNumberPagination):
    page_size = 2                 # số bản ghi mặc định mỗi trang
    page_size_query_param = 'page_size'  # cho phép client tự chỉnh ?page_size=20
    max_page_size = 100            # giới hạn tối đa
    
# Create your views here.
class createEmployeeView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": 200, 
                "message": "Employy created successfully", 
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        
        response = {
            "status": 400, 
            "message": "Employee creation failed", 
            "errors": serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
class getEmployeeView(APIView):
    def get(self, request):
        department = request.query_params.get('department', None)
        start_date = request.query_params.get('start_date', None)

        queryset = Employee.objects.all()

        if department:
            queryset = queryset.filter(department__icontains=department)

        if start_date:
            queryset = queryset.filter(start_date__gte=start_date)

        paginator = EmployeePagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = UserSerializer(result_page, many=True)

        return paginator.get_paginated_response({
            "status": 200,
            "message": "Employees retrieved successfully",
            "data": serializer.data
        })