from django.contrib import admin
from .models import Student, Major


class StudentAdmin(admin.ModelAdmin):
    list_display = ("st_id", "prefix_name", "fname", "lname", "major")


class MajorAdmin(admin.ModelAdmin):
    list_display = ("mj_name",)


admin.site.register(Student, StudentAdmin)
admin.site.register(Major, MajorAdmin)
