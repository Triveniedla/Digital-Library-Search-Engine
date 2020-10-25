# users/urls.py
from django.urls import path
from .views import SignUpView, HomePageView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
path('', HomePageView.as_view(), name='home'),

path('signup/', views.SignUpView, name='signup'),
# path('', HomePageView.as_view(), name='home'),

path('password_reset/',
 auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"),
 name="password_reset"),

path('reset/<uidb64>/<token>/',
 auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"),
 name="password_reset_confirm"),

#Activating account
 path('activate/<uidb64>/<token>/', views.activateaccount, name='activate'),
 path('accountconfirmation/', views.accountconfirmation, name='accountconfirmation'),

 path('searchhistory/',views.SearchHistoryView, name='searchhistory'),

 path('serp/',views.SERPView,name='serp'),

]
