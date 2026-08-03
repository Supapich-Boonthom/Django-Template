from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('st_id', 'prefix_name', 'fname', 'lname')

admin.site.register(Student, StudentAdmin)
