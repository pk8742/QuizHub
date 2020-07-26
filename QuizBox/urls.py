from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("countryQuiz/<int:quiz_id>",views.countryQuiz,name="countryQuiz"),
    path("nextCountryQuiz/<int:quiz_id>",views.nextCountryQuiz,name="nextCountryQuiz"),
]
