from django.shortcuts import redirect, render
from .models import Team
from cars.models import Car
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def home(request):
    teams = Team.objects.all() # Fetch all data inside Team Model
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured = True)
    all_cars = Car.objects.order_by('-created_date') # Descending Order of created_date
    
    # Returns list of distinct values for these columns which can be used to populate search form
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

    data = {
        'teams' : teams,
        'featured_cars' : featured_cars ,
        'all_cars': all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    if request.method == "POST":
        # name = request.POST.get('name')        

        # name = request.POST['name']
        # email = request.POST['email']
        # subject = request.POST['subject']
        # phone = request.POST['phone']
        # message = request.POST['message']

        # email_subject = 'You have a new message from Carzone website regarding ' + subject
        # message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message
        # admins = User.objects.all().filter(is_superuser=True)
        
        # Send mails to all admins
        # for admin in admins:
        #     admin_email = admin.email
        #     send_mail(
        #         email_subject,
        #         message_body,
        #         'rathan.kumar049@gmail.com',
        #         [admin_email],
        #         fail_silently=False,
        #     )
        # messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')
    
    return render(request, 'pages/contact.html')