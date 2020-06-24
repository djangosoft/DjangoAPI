from django.contrib import admin
from .models import Emp, Active, Member

admin.site.register(Member)
admin.site.register(Emp)
admin.site.register(Active)
