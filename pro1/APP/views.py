from django.shortcuts import render
from APP.models import Contact
def index(request):
    return render(request,"index.html")
def home(request):
    return render(request,"index.html")

def contact(request):
    return  render(request,"contact.html")

def about(request):
    return  render(request,"about.html")
def register(request):
    if request.method=="POST":
        name=request.POST["name"]
        address = request.POST["address"]
        number = request.POST["number"]
        comment = request.POST["comment"]
        email = request.POST["email"]


        obj=Contact(name=name,address=address,comment=comment,number=number,email=email)
        obj.save();
        return render(request,"register.html",{"name":name})

    return  render(request,"register.html")
