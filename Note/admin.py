# Register your models here.
from django.contrib import admin
from .models import Note

# @admin.register(Note)
# class NoteAdmin(admin.ModelAdmin):
#     list_display = ('title', 'created_at','content','user')  # Ensure fields match your model

admin.site.register(Note)