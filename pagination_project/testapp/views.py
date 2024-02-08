from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import generics
from .pagination import MyPagination,MyPagination2,MyPagination3
class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    #pagination_class = MyPagination3
    # def get_queryset(self):
    #     qs = Employee.objects.all()
    #     name = self.request.GET.get('ename')
    #     if name is not None:
    #         qs = qs.filter(ename__icontains=name)
    #     return qs
    search_fields = ('eno','esal')
    ordering_fields = ('eno','esal')
