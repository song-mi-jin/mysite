#from django.contrib import admin

# Register your models here.

from django.contrib import admin
from school.models import Student, Subject

admin.site.register(Student)
admin.site.register(Subject)
