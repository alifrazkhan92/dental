from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html ', {})


def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        return render(request, 'contact.html', {'message_name': message_name})
    
        send_mail(
            message_name, 
            message, 
            message_email, 
            ['alifrazkhan92@gmail.com'], 
            fail_silently=False,
        )
    
    else:
        return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})