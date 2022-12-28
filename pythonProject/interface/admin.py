# Регистрация моделей
from django.contrib import admin

# Register your models here.
from .models import AgentTypes
from .models import AgentGroups
from .models import Agents
from .models import AgentErrors

admin.site.register(AgentTypes)
admin.site.register(AgentGroups)
admin.site.register(Agents)
admin.site.register(AgentErrors)
