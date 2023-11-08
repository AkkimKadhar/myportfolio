from django.shortcuts import render
from .models import data

def home(request):
    return render(request, 'index.html')


def reviews(request):
     if request.method=="POST":
          name=request.POST['name']
          mail=request.POST['mail'] 
          message=request.POST['message']
          a=data()
          a.name=name
          a.mail=mail
          a.message=message
          a.save()
          return render(request,"reviews.html",{"database":data.objects.all()})

