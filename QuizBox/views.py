from django.shortcuts import render,redirect
from .models import Countries,Quiz_result_table,Quiz_dashboard
from usr_auth.views import usr_auth,register_page,login_page,logout_view
from django.db.models import Max
from datetime import datetime
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        username = request.session["username"]
    else:
        username = "None"
    context = {
        "login_page": login_page,
        "register_page": register_page,
        "logout": logout_view,
        "username": username
    }
    return render(request,"QuizBox/index.html",context)

def countryQuiz(request,quiz_id):
    if not request.user.is_authenticated:
        return redirect('login_page')
    username = request.session["username"]
    length = Countries.objects.count()

    try:
        data = Countries.objects.get(pk=quiz_id)
    except Countries.DoesNotExist:
        data = None
    quiz_type = "countryQuiz"
    dashboard = Quiz_dashboard.objects.filter(username=username,quiz_type=quiz_type).last()
    total = Countries.objects.count()
    correct = dashboard.user_correct
    wrong = dashboard.user_wrong
    percentage = dashboard.percentage
    context = {
        "username": username,
        "quiz": data,
        "logout": logout_view,
        "total": total,
        "correct": correct,
        "wrong": wrong,
        "percentage": percentage
    }
    return render(request,"QuizBox/countryQuiz.html",context)

def nextCountryQuiz(request,quiz_id):
    username = request.session["username"]
    all_question = Countries.objects.count()
    data = Countries.objects.get(pk=quiz_id)
    answer = data.answer
    quiz_type = "countryQuiz"
    q_no = quiz_id
    dateTime = datetime.now()

    quiz_result_table = Quiz_result_table.objects.filter(username=username,quiz_type=quiz_type,q_no=q_no-1).last()
    quiz_dashboard = Quiz_dashboard.objects.filter(username=username,quiz_type=quiz_type).last()
    if quiz_result_table and quiz_dashboard:
        usr_correct = quiz_result_table.usr_correct
        usr_wrong = quiz_result_table.usr_wrong
        user_correct = quiz_dashboard.user_correct
        user_wrong = quiz_dashboard.user_wrong
    else:
        usr_correct = 0
        usr_wrong = 0
        user_correct = 0
        user_wrong = 0

    if request.method == 'POST':
        rbtn = request.POST.get("rbtn")

        if rbtn == answer:
            new_usr_correct = usr_correct + 1
            new_usr_wrong = usr_wrong
            result = "correct"
            new_user_correct = user_correct + 1
            new_user_wrong = user_wrong
            percentage = new_user_correct/all_question * 100
            # adding new entry to Quiz_result_table table
            quiz_result_table_data = Quiz_result_table(username=username,quiz_type=quiz_type,q_no=q_no,result=result,usr_correct=new_usr_correct,usr_wrong=new_usr_wrong,dateTime=dateTime)
            quiz_result_table_data.save()
            # updating Quiz_dashboard table entries
            Quiz_dashboard.objects.filter(username=username,quiz_type=quiz_type).update(username=username,quiz_type=quiz_type,user_correct=new_user_correct,user_wrong=new_user_wrong,percentage=percentage,dateTime=dateTime)

        else:
            new_usr_correct = usr_correct
            new_usr_wrong = usr_wrong + 1
            result = "wrong"
            new_user_correct = user_correct
            new_user_wrong = user_wrong + 1
            percentage = new_user_correct/all_question * 100
            # adding new entry to Quiz_result_table table
            quiz_result_table_data = Quiz_result_table(username=username,quiz_type=quiz_type,q_no=q_no,result=result,usr_correct=new_usr_correct,usr_wrong=new_usr_wrong,dateTime=dateTime)
            quiz_result_table_data.save()
            # updating Quiz_dashboard table entries
            Quiz_dashboard.objects.filter(username=username,quiz_type=quiz_type).update(username=username,quiz_type=quiz_type,user_correct=new_user_correct,user_wrong=new_user_wrong,percentage=percentage,dateTime=dateTime)


    new_quiz_id = quiz_id + 1
    return redirect('countryQuiz',quiz_id=new_quiz_id)
