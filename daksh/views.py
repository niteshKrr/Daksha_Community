from django.shortcuts import render , HttpResponse , redirect
from daksh.models import Member
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout

# Create your views here.

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')   


def galary(request):
    return render(request, 'galary.html')   


def contact(request):
    return render(request, 'contact.html')   


def join_us(request):
    if request.method == "POST":
        name = request.POST.get('name')
        branch = request.POST.get('branch')
        reg_no = request.POST.get('Reg')
        roll_no = request.POST.get('Roll')
        session = request.POST.get('session')
        email = request.POST.get('email')
        image = request.FILES['image']

        data = Member(name=name , branch=branch , reg_no=reg_no ,roll_no=roll_no , session=session ,email=email , image=image  )
        data.save()
        messages.success(request, "Congrats now , you are a member")
        return redirect('/join_us')

    else:
        return render(request, 'join_us.html')   



def signup(request):
    if request.method == "POST":
        signupuser = request.POST.get('signupuser')
        signupemail = request.POST.get('signupemail')
        signuppassword = request.POST.get('signuppassword')
        signupcpassword = request.POST.get('signupcpassword')

        if signuppassword != signupcpassword :
            messages.error(request , 'conform your password')
            return redirect('/')

        else:
            myuser = User.objects.create_user(signupuser , signupemail , signuppassword)
            myuser.save()
            messages.success(request, ' signup success now , you can login')
            return redirect('/')

    return HttpResponse('404 - page not found')   
   

def login(request):
    if request.method == "POST":
        loginemail = request.POST.get('loginemail')
        loginpassword = request.POST.get('loginpassword')

        user = authenticate(emailaddress=loginemail , password=loginpassword)

        if user is not None:
            login(request, user )
            messages.success(request, 'You are logged in successfully')
            redirect('/')
        
        else:
            messages.error(request, 'Invalid credentials please try again')
            redirect('/')

    return HttpResponse('404 - page not found') 


def logout(request):
    return HttpResponse('logout page')   


def profile(request):
    return render(request, 'profile.html')   
