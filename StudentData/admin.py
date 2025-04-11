from django.contrib import admin
from .models import StudentData

class StudentDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email')  

admin.site.register(StudentData, StudentDataAdmin)
