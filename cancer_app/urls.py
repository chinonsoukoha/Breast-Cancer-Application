from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name='landingpage'),
    path('about/',views.about, name='about'),
    path('signup/',views.signup, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),


    path('Home/',views.home, name='home'),
    path('Home/Diagnosis/',views.diagnosis, name='diagnosis'),
    path('Home/Diagnosis/Instructions',views.instructions, name='instructions'),
    path('Home/Diagnosis/Result/',views.diagResult, name='diagResult'),
    path('Home/Diagnosis/History', views.history, name='history'),
    path('Home/Assessment/',views.risk, name='risk'),
    path('Home/Assessment/Result/', views.riskResult, name='riskResult'),
    path('Home/Assessment/Result/Insights', views.insights, name='insights'),
    path('Home/Assessment/History/', views.historyRisk, name='historyRisk'),
]
