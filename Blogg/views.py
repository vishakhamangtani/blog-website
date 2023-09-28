from django.shortcuts import render,redirect
from django.db import models
from .models import *

def verify_user(request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
            print("I'm from Verify_User func  ",str(user) )
            print(user.email,user.password)
            if password == user.password:
                print("pass match")
                return user
            else:
                return "Wrong Password"
        except:
            return "User Not Registered"

def get_user(user_id):
    try:
        return User.objects.get(pk=user_id)
    except:
        return None

# Create your views here.
def index(request):
    print('index')
    return render(request, 'index.html')
def blogs(request):
    print('blogs')
    return render(request, 'blogs.html')
def login(request):
    try:
        email = request.GET['email']
        password = request.GET['password']
        print(email,password)   
        
        user = verify_user(request, email=email, password=password)
        print("login ka ",user)

        if user is not None:
            # login(request, user)
            print("idar  aaya aayaa par kch ni hua")
            return render(request, 'index.html')  # Replace with the appropriate URL
        else:
            # Authentication failed
            messages.error(request, 'Incorrect email or password. Please try again.')

    
    except:
        pass
        #  print("User not Registered")
    print('login')
    return render(request, 'login.html')
def signup(request):
    print('test')
    if request.method == 'POST':
        form_data = request.POST
         # Create an instance of the model and populate it with form data
        #  for now categories nahi le rhi
        my_model_instance = User(
            name=form_data['name'],
            email=form_data['email'],
            password=form_data['password'],
            phone_number=form_data['phone_number'],
            # phone_number=form_data['field_name2'],
            # Populate other fields as needed
        )

        # Save the instance to the database
        my_model_instance.save()
        return redirect('login') 

    return render(request, 'signup.html')
def texteditor(request):
    print('test')
    return render(request, 'texteditor.html')
