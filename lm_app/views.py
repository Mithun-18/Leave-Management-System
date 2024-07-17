from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import Students

# Create your views here.
def login(request):
    if 'user_session' in request.session:
        request.session.pop('user_session')
    
    if(request.method == "POST"):
        try:
            user_id = request.POST['userid']
            pwd = request.POST['password']
            user = User.objects.get(user_id=user_id, password=pwd)
            if user:
                request.session['user_session'] = {'userid':user.user_id}
                return redirect('/')
        except Exception as ex:
            return render(request,'login.html', {"data": {"error": "Invalid credentials!"}})
    else:
        return render(request,'login.html')
    
def home(request):
    if(request.method=='POST'):
        try:
            date_from=request.POST['date_from']
            date_to=request.POST['date_to']
            user_id = request.session['user_session']['userid']
            leave_type = request.POST['leave_type']
            reason = request.POST['reason'] 
            Students.objects.create(user_id=user_id,date_from=date_from,date_to=date_to,leave_type=leave_type,reason=reason)     
        except Exception as ex:
            print(ex,user_id)
            
    if 'user_session' in request.session:
        return render(request,'home.html')
    else:
        return redirect('/login')
    