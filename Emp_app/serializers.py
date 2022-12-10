from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import *



class Employeserializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'

        def create(self,validated_data):
            emp=Employee.objects.create(**validated_data)
            return emp

        def update(self,validated_data):
            instance.first_name=validated_data.get('first_name',instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.author)  
            instance.salary = validated_data.get('salary', instance.edition)  
            instance.bonus = validated_data.get('bonus', instance.available)  
            instance.phone = validated_data.get('phone', instance.price)

            return instance    
           


        


class Departmentserializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields='__all__'

        def create(self, validated_data):
            dept = Department.objects.create(**validated_data)
            return dept


        def update(self,validated_data):
            instance.name=validated_data.get('name',instance.name)
            instance.location = validated_data.get('location', instance.location)  

            return instance
    




class Roleserializer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields='__all__'


        def create(self, validated_data):
            role = Role.objects.create(**validated_data)
            return role


        def update(self,validated_data):
            instance.name=validated_data.get('name',instance.name)
            return instance
    
