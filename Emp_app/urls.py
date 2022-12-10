from django.contrib import admin
from django.urls import path,include
from .views import *
from . import views
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("update/<int:id>",updateemployee.as_view()),    #Update employee url
    path("employee/",Employeview.as_view()),             #employee Url
    path("department/",Departmentview.as_view()),        #department Url
    path("role/",Roleview.as_view()),                    #Role Url
   # path('api-token-auth/', views.obtain_auth_token)    #Token-maker 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),   #Token-maker-jwt
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  #Token-maker-jwt
]