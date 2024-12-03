from django.contrib import admin
from .models import Employee
class MonModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employee._meta.fields] #
    search_fields = ('ename',)

# Register your models here.
admin.site.register(Employee , MonModelAdmin)