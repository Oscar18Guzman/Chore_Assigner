from django.contrib import admin
from app.models import Student, Chore, ChoreAssignment

# Register your models here.

admin.site.register(Student)
admin.site.register(Chore)
admin.site.register(ChoreAssignment)
