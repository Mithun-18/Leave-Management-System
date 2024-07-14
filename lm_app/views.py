from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def login(request):
    if 'user_session' in request.session:
        request.session.pop('user_session')
    
    if(request.method == "POST"):
        try:
            name = request.POST['userid']
            pwd = request.POST['password']
            user = User.objects.get(name=name, password=pwd)
            if user:
                request.session['user_session'] = {'userid':user.name}
                return redirect('/')
        except Exception as ex:
            return render(request,'login.html', {"data": {"error": "Invalid credentials!"}})
    else:
        return render(request,'login.html')
    
def home(request):
    if 'user_session' in request.session:
        return render(request,'home.html')
    else:
        return redirect('/login')