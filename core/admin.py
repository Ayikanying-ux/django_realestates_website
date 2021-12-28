from django.contrib import admin

from core.models import Agent, Comment, House

# Register your models here.

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display=('name', 'description', 'price')

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display=('name', 'contact')

@admin.register(Comment)
class CommentAdim(admin.ModelAdmin):
    list_display=('user', 'house', 'comment', 'date_added')
