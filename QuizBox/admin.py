from django.contrib import admin
from .models import Countries,Quiz_dashboard,Quiz_result_table
# Register your models here.
admin.site.register(Countries)
admin.site.register(Quiz_result_table)
admin.site.register(Quiz_dashboard)
