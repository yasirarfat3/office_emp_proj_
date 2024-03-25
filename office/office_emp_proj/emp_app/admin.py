from django.contrib import admin
from .models import Employe, Role, Department
# Register your models here.
admin.site.register(Employe)
admin.site.register(Role)
admin.site.register(Department)
