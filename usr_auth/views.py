from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
def usr_auth(request):
    from QuizBox.views import index
    if not request.user.is_authenticated:
        return redirect('login_page')
    else:
        return redirect('index')

def register_page(request):
    from QuizBox.views import index
    context = {
        "index": index
    }
    return render(request,"usr_auth/registerPage.html",context)

def login_page(request):
    from QuizBox.views import index
    context = {
        "index": index
    }
    return render(request,"usr_auth/loginPage.html",context)

def register_view(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        username = request.POST.get("uname")
        password = request.POST.get("pass")
        Repassword = request.POST.get("rpass")
        check = request.POST.get("check")

        if password != Repassword:
            context = {
                "msg": "Both password fields must be same"
            }
            return render(request,"usr_auth/registerPage.html",context)

        if check != "on":
            context = {
                "msg": "Please checkout the checkbox field"
            }
            return render(request,"usr_auth/registerPage.html",context)

        user = User.objects.create_user(username=username,first_name=name,email=email,password=password)
        user.save()
        context = {
            "msg": "Account created successfully"
        }
        return render(request,"usr_auth/registerPage.html",context)

def login_view(request):
    from QuizBox.views import countryQuiz
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["pass"]
        check = request.POST.get("check")

        if check != 'on':
            context = {
                "msg": "Please checkout the checkbox"
            }
            return render(request,"usr_auth/loginPage.html",context)

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            #creating user session
            request.session["username"] = username
            return redirect('countryQuiz',quiz_id=1)
        else:
            context = {
                "msg": "Invalid Credentials"
            }
            return render(request,"usr_auth/loginPage.html",context)

def logout_view(request):
    logout(request)
    # username = request.session['username']
    request.session.flush()
    return render(request,"usr_auth/loginPage.html",{"msg": "logged out successfully"})
