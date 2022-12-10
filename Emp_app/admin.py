from django.contrib import admin
from .models import *

# Register your models here.


class Employeadmin(admin.ModelAdmin):
    model = Employee
    list_display = ['first_name','last_name','phone','role','salary','hire_date','dept','bonus'] 


class Departmentadmin(admin.ModelAdmin):
    model = Department
    list_display = ["name","location"] 


class Roleadmin(admin.ModelAdmin):
    model = Role
    list_display = ["name"] 



admin.site.register(Employee,Employeadmin)
admin.site.register(Department,Departmentadmin)
admin.site.register(Role,Roleadmin)