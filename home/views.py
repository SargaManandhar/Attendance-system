from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login , logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import*
from .forms import CreateUserForm

def registerPage(request):

	
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'register.html', context)

def loginPage(request):
     
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user )
                return redirect('dashboard')
            else:
                messages.info(request,'Username or password is incorrect')
                return render( request,'login.html')

        context = {}
        return render( request,'login.html',context)
        
def logoutUser(request):
    logout(request)
    return redirect('login')

def index(request):
    return render(request, 'index.html')

#student
login_required(login_url='login')
def student(request):
    return render(request, 'student/student.html')

def attdetailsPage(request):
    return render(request,'student/attdetails.html')    

#teacher 
def teacherPage(request):
    return render(request, 'teacher/teacher.html')

def attteacherPage(request):
    return render(request, 'teacher/attendence.html') 

def stdetailsPage(request):
    return render(request, 'teacher/stdetails.html') 

def teacherdetailsPage(request):
    return render(request, 'teacher/attdetails.html') 
#admin
def adminPage(request):
    return render(request, 'admin/base_html.html')


   