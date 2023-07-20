"""NeuralInterface URL Configuration

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
     SendRequestToAgent, GraphApiData, SyncAgentData, \
     GraphAgentDataAdd, AgentErrorsDeleteData, DownloadNeuralNetworkStateData

urlpatterns = [
    # Главная страница
    path('', index),
    # Страница мониторинга
    path('monitor/', monitor),
    # Страница информации
    path('info/', info),
    # Страница администратора
    path('admin/', admin.site.urls),
    # API для добавления данных агента
    path('api/addAgentData', AgentAddData.as_view(), name='agent-add'),
    # API для редактирования данных агента с использованием его идентификатора (pk)
    path('api/editAgentData/<int:pk>/', AgentEditData.as_view(), name='agent-edit'),
    # API для удаления данных агента с использованием его идентификатора (pk)
    path('api/deleteAgentData/<int:pk>/', AgentDeleteData.as_view(), name='agent-delete'),
    # API для добавления данных группы
    path('api/addGroupData', GroupAddData.as_view(), name='group-add'),
    # API для редактирования данных группы с использованием ее идентификатора (pk)
    path('api/editGroupData/<int:pk>/', GroupEditData.as_view(), name='group-edit'),
    # API для удаления данных группы с использованием ее идентификатора (pk)
    path('api/deleteGroupData/<int:pk>/', GroupDeleteData.as_view(), name='group-delete'),
    # API для удаления данных об ошибках агента с использованием его идентификатора (agent_id)
    path('monitor/api/deleteAgentErrorsData/<int:agent_id>/', AgentErrorsDeleteData.as_view(),
         name='agents-errors-delete'),
    # API для получения данных для графика
    path('api/graphData/', GraphApiData.as_view(), name='graph-data'),
    # API для отправки запроса агенту
    path('api/SendRequestToAgent', SendRequestToAgent.as_view(), name='graph-data'),
    # API для синхронизации данных агента
    path('api/syncAgentData', SyncAgentData.as_view(), name='agent-sync'),
    # API для добавления данных агента для графика
    path('api/graphAgentDataAdd', GraphAgentDataAdd.as_view(), name='graph-add-data'),
    # API для добавления данных состояний агента
    path('api/downloadNeuralNetworkStateData', DownloadNeuralNetworkStateData.as_view(), name='download-state-data'),
]
