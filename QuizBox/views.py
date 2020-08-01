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

    list = []
    for i in range(1,length+1):
        i_data = Quiz_result_table.objects.filter(username=username,quiz_type=quiz_type,q_no=i).last()
        if i_data:
            i_result = i_data.result
            i_selected_value = i_data.selected_value
        else:
            i_result = None
            i_selected_value = None
        list.append([i,i_result,i_selected_value])

    dashboard = Quiz_dashboard.objects.filter(username=username,quiz_type=quiz_type).last()
    if not dashboard == None:
        total = Countries.objects.count()
        correct = dashboard.user_correct
        wrong = dashboard.user_wrong
        left = Quiz_result_table.objects.filter(username=username,quiz_type=quiz_type,result="left").count()
        percentage = dashboard.percentage
    else:
        total = Countries.objects.count()
        correct = 0
        wrong = 0
        left = 0
        percentage = 0

    quiz_result = Quiz_result_table.objects.filter(username=username,quiz_type=quiz_type,q_no=quiz_id).last()
    if quiz_result:
        quiz_selected_value = quiz_result.selected_value
    else:
        quiz_selected_value = "None"
    
    context = {
        "username": username,
        "quiz": data,
        "logout": logout_view,
        "total": total,
        "correct": correct,
        "wrong": wrong,
        "left": left,
        "percentage": percentage,
        "list": list,
        "quiz_selected_value": quiz_selected_value,
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

    if not quiz_id == 1:
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
            percentage = new_user_correct/quiz_id * 100
            selected_value = rbtn
            # adding new entry to Quiz_result_table table
            quiz_result_table_data = Quiz_result_table(username=username,quiz_type=quiz_type,q_no=q_no,result=result,usr_correct=new_usr_correct,usr_wrong=new_usr_wrong,dateTime=dateTime,selected_value=selected_value)
            quiz_result_table_data.save()
            if not quiz_id == 1:
                # updating Quiz_dashboard table entries
                Quiz_dashboard.objects.filter(username=username,quiz_type=quiz_type).update(username=username,quiz_type=quiz_type,user_correct=new_user_correct,user_wrong=new_user_wrong,percentage=percentage,dateTime=dateTime)
            else:
                # inserting first user data in Quiz_dashboard table
                quiz_dashboard_data = Quiz_dashboard(username=username,quiz_type=quiz_type,user_correct=new_user_correct,user_wrong=new_user_wrong,percentage=percentage,dateTime=dateTime)
                quiz_dashboard_data.save()

        elif rbtn == None:
            new_usr_correct = usr_correct
            new_usr_wrong = usr_wrong
            result = "left"
            new_user_correct = user_correct
            new_user_wrong = user_wrong
            percentage = new_user_correct/quiz_id * 100
            selected_value = "none"
            # adding new entry to Quiz_result_table table
            quiz_result_table_data = Quiz_result_table(username=username,quiz_type=quiz_type,q_no=q_no,result=result,usr_correct=new_usr_correct,usr_wrong=new_usr_wrong,dateTime=dateTime,selected_value=selected_value)
            quiz_result_table_data.save()
            if not quiz_id == 1:
                # updating Quiz_dashboard table entries
                Quiz_dashboard.objects.filter(username=username,quiz_type=quiz_type).update(username=username,quiz_type=quiz_type,user_correct=new_user_correct,user_wrong=new_user_wrong,percentage=percentage,dateTime=dateTime)
            else:
                # inserting first user data in Quiz_dashboard table
                quiz_dashboard_data = Quiz_dashboard(username=username,quiz_type=quiz_type,user_correct=new_user_correct,user_wrong=new_user_wrong,percentage=percentage,dateTime=dateTime)
                quiz_dashboard_data.save()
        else:
            new_usr_correct = usr_correct
            new_usr_wrong = usr_wrong + 1
            result = "wrong"
            new_user_correct = user_correct
            new_user_wrong = user_wrong + 1
            percentage = new_user_correct/quiz_id * 100
            selected_value = rbtn
            # adding new entry to Quiz_result_table table
            quiz_result_table_data = Quiz_result_table(username=username,quiz_type=quiz_type,q_no=q_no,result=result,usr_correct=new_usr_correct,usr_wrong=new_usr_wrong,dateTime=dateTime,selected_value=selected_value)
            quiz_result_table_data.save()
            if not quiz_id == 1:
                # updating Quiz_dashboard table entries
                Quiz_dashboard.objects.filter(username=username,quiz_type=quiz_type).update(username=username,quiz_type=quiz_type,user_correct=new_user_correct,user_wrong=new_user_wrong,percentage=percentage,dateTime=dateTime)
            else:
                # inserting first user data in Quiz_dashboard table
                quiz_dashboard_data = Quiz_dashboard(username=username,quiz_type=quiz_type,user_correct=new_user_correct,user_wrong=new_user_wrong,percentage=percentage,dateTime=dateTime)
                quiz_dashboard_data.save()

    return redirect('next',quiz_type="countryQuiz",quiz_id=quiz_id)

def Reattempt(request,quiz_type):
    username = request.session["username"]

    Quiz_result_table.objects.filter(username=username,quiz_type=quiz_type).delete()
    Quiz_dashboard.objects.filter(username=username,quiz_type=quiz_type).delete()

    return redirect(quiz_type,1)

def previous(request,quiz_type,quiz_id):
    prev_quiz_id = quiz_id - 1
    return redirect(quiz_type,quiz_id=prev_quiz_id)

def next(request,quiz_type,quiz_id):
    nxt_quiz_id = quiz_id + 1
    return redirect(quiz_type,quiz_id=nxt_quiz_id)
