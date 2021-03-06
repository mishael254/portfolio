from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Contact
# Create your views here.
def home(request):

    if request.method == 'POST'and request.is_ajax():
        
        if request.POST['name'] == "":
            username = "Jane Doe"   #  set default name
        else:
            username = request.POST['name']
        # check for select field
        if request.POST['gender'] == "Select":
            gender = "f"
        else:
            gender = request.POST['gender']
        # return name and gender to success in ajax call top update content
        return HttpResponse(json.dumps({'name': username, 'gender': gender}))
    else:
        return render(request, 'home/home.html')


#Portfolio View
def portfolio(request):
    return render(request, 'home/portfolio.html')


# Contact View
def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        form = Contact(email=email, subject=subject, message=message)
        # Saving Form data to Database
        form.save()

        return render(request, 'home/contact.html')
    else:
        return render(request, 'home/contact.html')