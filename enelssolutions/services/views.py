from django.shortcuts import render
from django.http import HttpResponse
from services.models import Subscriber,Contact
from django.core import validators
# Create your views here.

def index(request):
    return render(request,'services/index.html',{'sub':subscribe(request)})

def subscribe(request):
    msg = ""
    if request.method == 'POST' and request.POST.get('state'):
        sub_name = request.POST.get('name')
        sub_email = request.POST.get('email')
        subs = Subscriber.objects.get_or_create(name=sub_name,email=sub_email)
        #if sub_email not in Subscriber.get_objects().emails:
        msg = "Thank You!"
        #else:
        #    msg = "Email already exists"
        print("Name: "+sub_name)
        print("Email: "+sub_email)
    return msg
def contact_us(request):
    msg = ""
    if request.method == 'POST':
        con_fname = request.POST.get('firstname')
        con_lname = request.POST.get('lastname')
        con_email = request.POST.get('email')
        con_sub = request.POST.get('subject')
        con_msg = request.POST.get('message')
        cons = Contact.objects.get_or_create(firstname=con_fname,lastname=con_lname,email=con_email,subject=con_sub,message=con_msg)
        msg = "Thank You!"
        print("Name: "+con_fname)
        print("Email: "+con_email)
        print("Subject:" +con_sub)
    return msg


def about(request):
    return render(request,'services/about.html',{'sub':subscribe(request)})

def blog(request):
    return render(request,'services/blog.html',{'sub':subscribe(request)})

def contact(request):
    return render(request,'services/contact.html',{'sub':subscribe(request),'con':contact_us(request)})

def service(request):
    return render(request,'services/service.html',{'sub':subscribe(request)})

def blog_details(request):
    return render(request,'services/blog-details.html',{'sub':subscribe(request)})
