from django.contrib import admin
from .models import Note

# Register your models here.
class NoteInput(admin.ModelAdmin):
    list_display = ("user", "id", "content", "status", "created_at")

admin.site.register(Note, NoteInput)