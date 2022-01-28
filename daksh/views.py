from django.shortcuts import render , HttpResponse , redirect
from daksh.models import Member
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login as dj_login , logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, 'index.html')


def about(request):
    if not request.user.is_authenticated:
        messages.error(request, "you are not able to see the page , please login first")
        return redirect('/')

    else:
        return render(request, 'about.html')   


def gallery(request):
    if not request.user.is_authenticated:
        messages.error(request, "you are not able to see the page , please login first")
        return redirect('/')

    else:   
        return render(request, 'gallery.html')   


def contact(request):
    if not request.user.is_authenticated:
        messages.error(request, "you are not able to see the page , please login first")
        return redirect('/')

    else:
        return render(request, 'contact.html')   


def join_us(request):
    if not request.user.is_authenticated:
        messages.error(request, "you are not able to see the page , please login first")
        return redirect('/')

    elif request.method == "POST":
        user = request.user
        name = request.POST.get('name')
        branch = request.POST.get('branch')
        reg_no = request.POST.get('Reg')
        roll_no = request.POST.get('Roll')
        session = request.POST.get('session')
        image = request.FILES['image']
        about = request.POST.get('about')


        if image.size > 2*1024*1024:
            messages.error(request , 'Maximum allowed size for image is less than 2mb')
            return redirect('/join_us')

        elif Member.objects.filter(user=request.user).exists():
            messages.error(request , 'User already a member , try unique one')
            return redirect('/join_us')

        else: 
            data = Member(user=user ,name=name , branch=branch , reg_no=reg_no ,roll_no=roll_no , session=session ,about=about , image=image  )
            data.save()
            messages.success(request, "Congrats now , you are a member")
            return redirect('/')

    else:
        return render(request, 'join_us.html')   



def signup(request):
    if request.method == "POST":
        signupuser = request.POST.get('signupuser')
        signupemail = request.POST.get('signupemail')
        signuppassword = request.POST.get('signuppassword')
        signupcpassword = request.POST.get('signupcpassword')

        if User.objects.filter(username = request.POST['signupuser']).exists():
            messages.error(request , 'Username already exists try unique one')
            return redirect('/')

        elif signuppassword != signupcpassword :
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
        loginuser = request.POST.get('loginuser')
        loginpassword = request.POST.get('loginpassword')

        user = authenticate(request , username=loginuser , password=loginpassword)

        if user is not None:
            dj_login(request, user)
            messages.success(request, 'You are logged in successfully')
            return redirect('/')
        
        else:
            messages.error(request, 'Invalid credentials please try again')
            return redirect('/')

    return HttpResponse('404 - page not found') 


def handlelogout(request):
    logout(request)
    messages.success(request, 'You are logged out successfully')
    return redirect('/')



def profile(request):
    if not request.user.is_authenticated:
        messages.error(request, "you are not able to see the page , please login first")
        return redirect('/')

    elif Member.objects.filter(user=request.user).exists():
        allmembers = Member.objects.filter(user=request.user)
        context = {'userprofile': allmembers}
        return render(request, 'profile.html' , context)   

    else:
        messages.error(request, " your profile does not exist , please join_us first")
        return redirect('/')
