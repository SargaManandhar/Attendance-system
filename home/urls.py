
from django.urls import path
from .import views

urlpatterns = [
    path("",views.index, name='index'),

    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"), 
    path('logout', views.logoutUser, name="logout"), 

    #student
    path('student/', views.student, name="dashboard"),
    path('attdetails/', views.attdetailsPage, name="attdetails"),


    #teacher 
    path('teacher/',views.teacherPage,name="teacher"),
    path('attteacher/',views.attteacherPage,name="attteacher"),
    path('class/', views.stdetailsPage, name="class"),
    path('attgraph/', views.teacherdetailsPage, name="graph"), 
	
    #admin
    path('admin/',views.adminPage,name="admin"),
    
    
]
