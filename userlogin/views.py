from django.shortcuts import redirect, render
from userlogin.models import Details
# Create your views here.

def login(request):
    flag=False
    if request.method=="POST":
        eml=request.POST["eml"]
        pwd=request.POST["pwd"]
        detail=Details.objects.all()
        for i in detail:
            e=i.email
            p=i.password
            if eml==e and pwd==p:
                flag=True
        
        if flag==True:
            request.session["email"]=eml
            return redirect("userdetails")
        
        else:
            msg="Invalid email & password."
            return render(request,"index.html",{'msg':msg})
    else:   
        return render(request,"index.html")

def signup(request):
    detail=Details()
    if request.method=="POST":
        pwd=request.POST["pwd"]
        cpwd=request.POST["cpwd"]
        if pwd == cpwd:
            detail.name=request.POST["n"]
            detail.email=request.POST["email"]
            detail.password=pwd
            detail.address=request.POST["address"]
            detail.save()
            msg="Record added successfully."
            clr="green"
        else:
            msg="Password not match."
            clr="red"
        return render(request,"signupform.html",{'msg':msg,'clr':clr})
    else:
        return render(request,"signupform.html")

def userdetails(request):
    #email=request.session['email']
    if 'email' in request.session:
        detail=Details.objects.all()
        if 'btn1' in request.POST:
            e=request.POST['btn1']
            n=request.POST.getlist('n')
            ind=n.index(e)
            n=n[ind:ind+5]
            Details.objects.filter(id = e).update(name = n[1], email=n[2], password=n[3], address=n[4])
            return render(request,"userdetailspage.html",{'detail':detail})
        
        elif 'btn2' in request.POST:
            d=request.POST['btn2']
            Details.objects.get(id=d).delete()
            return render(request,"userdetailspage.html",{'detail':detail})
        
        elif 'btn3' in request.POST:
            return redirect("login")
        else:
            return render(request,"userdetailspage.html",{'detail':detail})
    else:
        return redirect("login")


    