from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def hello(request):
    if(request.method == "POST"):
        return HttpResponse("<h1>hello</h1>")
    else:
        return render(request,'login.html')