from django.urls import path
from . import views

urlpatterns = [
    path('',views.usr_auth,name="usr_auth"),
    path('login_page',views.login_page,name="login_page"),
    path('register_page',views.register_page,name="register_page"),
    path('login',views.login_view,name="login"),
    path('register',views.register_view,name="register"),
    path('logout',views.logout_view,name="logout"),
]
