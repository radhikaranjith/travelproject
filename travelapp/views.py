from django.http import HttpResponse
from django.shortcuts import render
from .models import place, suggetion


# Create your views here.
def fun(request):
    places=place.objects.all()
    return render(request,"index.html",{'places':places})
def fun1(request):
    suggetions=suggetion.objects.all()
    return render(request, "indexx.html", {'suggetions': suggetions})
def addition(request):
    num1=request.POST["num1"]
    num2=request.POST["num2"]
    num3=num1+num2
    return render(request,"result.html",{"add":num3})