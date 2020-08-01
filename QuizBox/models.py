from django.db import models

# Create your models here.
class Countries(models.Model):
    question = models.CharField(max_length=64)
    a = models.CharField(max_length=64)
    b = models.CharField(max_length=64)
    c = models.CharField(max_length=64)
    d = models.CharField(max_length=64)
    answer = models.CharField(max_length=64)

    def __str__(self):
        return f"id={self.id},question={self.question},a={self.a},b={self.b},c={self.c},d={self.d},answer={self.answer}"

class Quiz_result_table(models.Model):
    username = models.CharField(max_length=64)
    quiz_type = models.CharField(max_length=64)
    q_no = models.IntegerField()
    selected_value = models.CharField(max_length=64,default='default',blank='true')
    result = models.CharField(max_length=64)
    usr_correct = models.IntegerField()
    usr_wrong = models.IntegerField()
    dateTime = models.DateField()

class Quiz_dashboard(models.Model):
    username = models.CharField(max_length=64)
    quiz_type = models.CharField(max_length=64)
    user_correct = models.IntegerField()
    user_wrong = models.IntegerField()
    percentage = models.IntegerField()
    dateTime = models.DateField()
