from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

# from django.shortcuts import HttpResponse


def index (request) :
    return render(request , 'index.html')


def contact (request) : 
    return render (request , 'contact.html')


def products (request) : 
    return render (request , 'products.html')


def services (request) : 
    return render (request , 'services.html')

# def about(request) : 
#     return HttpResponse("This is About Page")
def postcontact(request) :
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    question = request.POST.get('question')

    try:
    
        subject = 'New User Has Contacted us!! His Details are as follows !!'
        print(subject)
        message = f'User has filled following details in the Contact Us Form :\n Name : {name} \nEmail Address : {email} \nPhone Number : {phone} \n  Question Asked : {question}'
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject,message,email_from,['yram18223@gmail.com'], fail_silently=False)
        msg="Your Question and Details have been forwarded to the Shiv Kailas PaniPuri !! We will Contact You Shortly !! "
    
        return render (request , "contact.html" , {'msg' : msg})

    except :
        msg = "Something went wrong !! Please Enter your Details Again !!"
        return render (request , "contact.html" , {'msg':msg})    




        
        

def test (request) :
    return render (request , 'test.html')

def about(request): 
    return render (request ,'about.html')




# paraswaruday@gmail.com