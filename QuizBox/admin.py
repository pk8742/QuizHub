from django.contrib import admin
from .models import CS_quiz,Quiz_dashboard,Quiz_result_table
# Register your models here.
admin.site.register(CS_quiz)
admin.site.register(Quiz_result_table)
admin.site.register(Quiz_dashboard)
