from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Contact
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST.get('car_id')
        car_title = request.POST.get('car_title')
        user_id = request.POST.get('user_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        customer_need = request.POST.get('customer_need')
        city = request.POST.get('city')
        state = request.POST.get('state')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id = user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry about this car. Please wait until we get back to you.')
                return redirect('/cars/'+car_id)

        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id,
        first_name=first_name, last_name=last_name, customer_need=customer_need, city=city,
        state=state, email=email, phone=phone, message=message)

        # admins = User.objects.all().filter(is_superuser=True)
        
        # # Send mails to all admins
        # for admin in admins:
        #     admin_email = admin.email
        #     send_mail(
        #         'New Car Inquiry', # Subject
        #         'You have a new inquiry for the car ' + car_title + '. Please login to your admin panel for more info.', # Body
        #         'khomosikhuzema894@gmail.com', # From email
        #         [admin_email], # To email
        #         fail_silently=False,
        #     )

        contact.save()
        messages.success(request, 'Your request has been submitted, we will get back to you shortly.')
        return redirect('/cars/'+car_id)
