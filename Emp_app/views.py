from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Departmentserializer,Employeserializer,Roleserializer
from rest_framework.views import APIView
from Emp_app import serializers
from rest_framework import status
from .models import Employee,Role,Department
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


#Update Employee class--------------------------------------------------------------------------------------------------------------------
class updateemployee(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated ]
    def put(self,request,id):
        employee_obj=Employee.objects.get(id=id)
        data=request.data
        serializer=Employeserializer(employee_obj,data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "response": "Data updated succesfully"},
            status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"status": False, "response": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def patch(self,request,id):
        emp_obj=Employee.objects.get(id=id)
        serializer=Employeserializer(emp_obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "response": "Data updated succesfully"},
        status=status.HTTP_201_CREATED,
        )
        else:
            return Response(
                {"status": False, "response": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )


    def delete(self,request,id):
        try:
            employee=Employee.objects.get(id=id)
            employee.delete()
            return Response("Employee Deleted succesfully.")
        except:
            return Response("Employee does not exist.")

    
    def get(self,request,id):
        try:
            employee_obj=Employee.objects.get(id=id)
            serializer=Employeserializer(employee_obj)
        except:
            if id :
                return Response("EMPTY DATA!!")
            else:
                return Response("Enter the valid id!")

        return Response(serializer.data)




#Employee class--------------------------------------------------------------------------------------------------------------------
class Employeview(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated ]


    def get(self,request):
        emp_obj=Employee.objects.all()
        serializer=Employeserializer(emp_obj,many=True)
        return Response({"Status":True,"response": serializer.data},status=status.HTTP_200_OK
        )

    def post(self,request):
        serializer=Employeserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": True, "response": "Employee created successfully."},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"status": False, "response": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )



#Role class--------------------------------------------------------------------------------------------------------------------
class Roleview(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated ]

    def get(self,request):
        emp_obj=Role.objects.all()
        serializer=Roleserializer(emp_obj,many=True)
        return Response({"Status":True,"response": serializer.data},status=status.HTTP_200_OK
        )

    def post(self,request):
        serializer=Roleserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": True, "response": "Employee created successfully."},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"status": False, "response": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )



#Department class--------------------------------------------------------------------------------------------------------------------
class Departmentview(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated ]


    def get(self,request):
        dept_obj=Department.objects.all()
        serializer=Departmentserializer(dept_obj,many=True)
        return Response({"Status":True,"response": serializer.data},status=status.HTTP_200_OK
        )

    def post(self,request):
        serializer=Departmentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": True, "response": "Employee created successfully."},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"status": False, "response": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )






