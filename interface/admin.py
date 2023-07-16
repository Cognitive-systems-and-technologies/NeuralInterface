# Регистрация моделей
from django.contrib import admin

# Register your models here.
from .models import AgentTypes, AgentGroups, Agents, AgentErrors, AgentFiles, NeuralAlgorithms
from .models import AgentsView, AgentErrorsView, AgentFilesView

admin.site.register(AgentTypes)
admin.site.register(AgentGroups)
admin.site.register(Agents)
admin.site.register(AgentErrors)
admin.site.register(AgentFiles)
admin.site.register(NeuralAlgorithms)

admin.site.register(AgentsView)
admin.site.register(AgentErrorsView)
admin.site.register(AgentFilesView)




