from django.contrib import admin

from core.models import Agent, House

# Register your models here.

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display=('name', 'description', 'price')

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display=('name', 'contact')
