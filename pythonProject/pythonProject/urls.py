"""pythonProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# from interface.views import interfaceAPIView
from interface.views import index, monitor, info, \
     AgentAddData, AgentDeleteData, AgentEditData, \
     GroupAddData, GroupDeleteData, GroupEditData, \
     SendRequestDjango, GraphApiData, syncAgentData

urlpatterns = [
    path('', index),
    path('monitor/', monitor),
    path('info/', info),
    path('admin/', admin.site.urls),
    path('api/addAgentData', AgentAddData.as_view()),
    path('api/editAgentData/<int:pk>/', AgentEditData.as_view(), name='Agents-edit'),
    path('api/deleteAgentData/<int:pk>/', AgentDeleteData.as_view(), name='Agents-delete'),
    path('api/addGroupData', GroupAddData.as_view()),
    path('api/editGroupData/<int:pk>/', GroupEditData.as_view(), name='Agents-edit'),
    path('api/deleteGroupData/<int:pk>/', GroupDeleteData.as_view(), name='Agents-delete'),
    path('api/graphData/', GraphApiData.as_view(), name='graph-data'),
    path('api/sendRequestDjango', SendRequestDjango.as_view()),
    path('api/syncAgentData', syncAgentData, name='agent-sync'),
]
