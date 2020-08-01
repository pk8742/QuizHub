from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("countryQuiz/<int:quiz_id>",views.countryQuiz,name="countryQuiz"),
    path("nextCountryQuiz/<int:quiz_id>",views.nextCountryQuiz,name="nextCountryQuiz"),
    path("Reattempt/<str:quiz_type>",views.Reattempt,name="Reattempt"),
    path("pravious/<str:quiz_type>/<int:quiz_id>",views.previous,name="previous"),
    path("next/<str:quiz_type>/<int:quiz_id>",views.next,name="next"),
]
