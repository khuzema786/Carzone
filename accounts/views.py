from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        
        user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    # request.method == 'GET':
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        # firstname, lastname, username, email, password, confirm_password = request.POST.values()
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in.')
                    return redirect('dashboard')
                    # user.save()
                    # messages.success(request, 'You are registered successfully.')
                    # return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    # request.method == 'GET':
    return render(request, 'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return redirect('home')
    
@login_required(login_url= 'login')
def dashboard(request):
    user_inquiry = Contact.objects.order_by('-create_date').filter(user_id = request.user.id)
    data = {
        'inquires' : user_inquiry,
    }
    return render(request, 'accounts/dashboard.html', data)