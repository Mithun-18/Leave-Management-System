from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from .models import Students
from django.contrib import messages
from datetime import datetime

# Create your views here.
def login(request):
    if 'user_session' in request.session:
        request.session.pop('user_session')
    
    if(request.method == "POST"):
        try:
            user_id = request.POST['userid']
            pwd = request.POST['password']
            user = User.objects.get(user_id=user_id, password=pwd)
            is_student_res=User.objects.filter(user_id=user_id).values('is_student')
            is_student=is_student_res[0]['is_student']
            print(is_student)
            if user:
                request.session['user_session'] = {'userid':user.user_id,'is_student':is_student}
                return redirect('/')
        except Exception as ex:
            return render(request,'login.html', {"data": {"error": "Invalid credentials!"}})
    else:
        return render(request,'login.html')

def logout(request):
    if 'user_session' in request.session:
        request.session.pop('user_session')
        return render(request,'logout.html')
    else:
        return redirect('/login')
    
def home(request):
    if 'user_session' in request.session:
        is_student=request.session['user_session']['is_student']
        if   not is_student:
            total_approved_leaves=Students.objects.filter(status='Approved').count()
            total_rejected_leaves=Students.objects.filter(status='Rejected').count()
            data=Students.objects.filter(status='Pending').values()       
            for d in data:
                name_set=User.objects.filter(user_id=d['user_id']).values('name')
                name=name_set[0]['name']
                d['name']=name
            return render(request,'home.html',{'data':data,'total_approved_leaves':total_approved_leaves,'total_rejected_leaves':total_rejected_leaves,'is_student':is_student})
          
        else:              
            if(request.method=='POST'):
                try:
                    date_from=request.POST['date_from']
                    date_to=request.POST['date_to']
                    user_id = request.session['user_session']['userid']
                    leave_type = request.POST['leave_type']
                    reason = request.POST['reason'] 
                    total_days=abs((datetime.strptime(date_to, '%Y-%m-%d') - datetime.strptime(date_from, '%Y-%m-%d')).days)+1
                    Students.objects.create(user_id=user_id,date_from=date_from,date_to=date_to,leave_type=leave_type,total_days=total_days,reason=reason)
                    messages.add_message(request, messages.SUCCESS, "Leave added successfully!")  
                except Exception as ex:
                    print(ex,user_id)
                return  redirect('/')
            
            else: 
                total_leaves=Students.objects.filter(user_id=request.session['user_session']['userid'],status='Approved').count()
                total_leaves_sick=Students.objects.filter(user_id=request.session['user_session']['userid'],status='Approved',leave_type='sick').count()
                total_leaves_other=Students.objects.filter(user_id=request.session['user_session']['userid'],status='Approved',leave_type='other').count()
                total_pending_leaves=Students.objects.filter(user_id=request.session['user_session']['userid'],status='Pending').count()
                total_rejected_leaves=Students.objects.filter(user_id=request.session['user_session']['userid'],status='Rejected').count()
                
                data={
                    "total_leaves":total_leaves,
                    "total_leaves_sick":total_leaves_sick,
                    "total_leaves_other":total_leaves_other,
                    "total_pending_leaves":total_pending_leaves,
                    "total_rejected_leaves":total_rejected_leaves,
                    }
                return render(request,'home.html',{'data':data,'is_student':is_student})
    
    else: 
        return redirect('/login')
    
def leave_info(request):
    status=request.GET['type']
    is_student=request.session['user_session']['is_student']
    
    if   not is_student:
        data=Students.objects.filter(status=status).values()
        for d in data:
            name_set=User.objects.filter(user_id=d['user_id']).values('name')
            name=name_set[0]['name']
            d['name']=name
        return render(request,'leave_info.html',{'data':data,'status':status,'is_student':is_student})
    else:      
        user_id=request.session['user_session']['userid']
        data=Students.objects.filter(user_id=user_id,status=status).values()
        return render(request,'leave_info.html',{'data':data,'status':status,'is_student':is_student})
    
def action(request):
    if request.method=='POST':
        try:
            status=request.POST['status']
            id=request.POST['leave_id']
            Students.objects.filter(id=id).update(status=status)
        except Exception as ex:
            return redirect('/')
    return redirect('/')

def cancel(request):
    if 'user_session' in request.session:
        is_student=request.session['user_session']['is_student']
        if  is_student:
            if request.method=='POST':
                try:
                    id=request.POST['leave_id']
                    res=Students.objects.get(id=id)
                    res.delete()
                except Exception as ex:
                    return redirect('/')
                
            total_pending_leaves=Students.objects.filter(user_id=request.session['user_session']['userid'],status='Pending').count()
            if(total_pending_leaves):
                return redirect("/leaves?type=Pending")
            else:
                return redirect('/')
            