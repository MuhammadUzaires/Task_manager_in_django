from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Task)

class TaskAdmin(admin.ModelAdmin):
    list_display=('title','status','user','created_at')
    list_filter=('status','created_at')