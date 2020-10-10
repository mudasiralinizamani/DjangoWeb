from django.shortcuts import render
import app.models as app_modules
from django.contrib import messages

# Create your views here.

def Contact(req):
    if req.method == 'POST':
        Name = req.POST.get('name')
        Email = req.POST.get('email')
        Message = req.POST.get('message')

        if len(Name) < 2 or len(Email) < 4 or '@' not in Email or len(Message) < 3:
            messages.error(req, 'Plz, Fill the fields Correctly.')
            
        else:
            contact = app_modules.Contact(name=Name, email=Email, message=Message)
            contact.save()
            messages.success(req, f'Thanks for Contacting, {Name}.')
    return render(req, 'Pages/Contact.html')