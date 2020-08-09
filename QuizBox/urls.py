from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("CS_Quiz/<int:quiz_id>",views.CS_Quiz,name="CS_Quiz"),
    path("nextQuiz/<int:quiz_id>",views.nextQuiz,name="nextQuiz"),
    path("Reattempt/<str:quiz_type>",views.Reattempt,name="Reattempt"),
    path("pravious/<str:quiz_type>/<int:quiz_id>",views.previous,name="previous"),
    path("next/<str:quiz_type>/<int:quiz_id>",views.next,name="next"),
    path("complete_quiz/<str:quiz_type>",views.complete_quiz,name="complete_quiz")
]
