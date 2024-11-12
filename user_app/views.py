from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = auth.authenticate(username=username , password=password)
        
        if user is not None:
            auth.login(request , user)
            return redirect("home")
        else:
            messages.info(request , "Username or password is wrong")
            return redirect("login")
    else:
        return render(request , "login.html")
    

def register(request):
    if request.method=="POST":
        
        if request.method=="POST":
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]
            password2 = request.POST["password2"]
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request , "Email already used")
                return redirect("register")
            elif User.objects.filter(username=username).exists():
                messages.error(request , "Username already used")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username,password=password,email=email)
                user.save()
                messages.success(request , "Successfull")
                return redirect("login")
        else:
            messages.error(request , "Passwords are not the same")
            return redirect("register.html")
    else:
        return render(request ,"register.html")
    
    
def logout(request):
    print("Logging out user")
    auth.logout(request)
    return redirect("login")