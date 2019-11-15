from django.urls import path
from . import views

app_name = 'default_auth'
urlpatterns = [
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('dashboard/', views.Dashboard, name="dashboard"),
    path('logout/', views.Logout, name="logout"),
    path('login/', views.LoginView.as_view(), name="login"),

]
