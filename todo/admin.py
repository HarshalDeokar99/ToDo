from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display=('task','is_completed','updated_at')
    # You’re customizing how the Task model appears in the admin interface by creating a new class TaskAdmin that inherits from admin.ModelAdmin.
    # list_display = ('task', 'is_completed', 'updated_at')
    # This tells Django to show these fields as columns in the admin list view of the Task model.
    search_fields=('task',)
    #this provides a search box in admin panel


# Register your models here.
admin.site.register(Task,TaskAdmin)
