from django.shortcuts import render,redirect
from django.db import models
from .models import *
from django.db import IntegrityError 
import os
from django.core.files.storage import default_storage


def verify_user(request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
            print("I'm from Verify_User func  ",str(user) )
            print(user.email,user.password)
            if password == user.password:
                print("pass match")
                return user
            else:
                return False
        except:
            return False


# Create your views here.
def index(request):
    print('index')
    return render(request, 'index.html')
def blogs(request):
    print('blogs')
    return render(request, 'blogs.html')

def login(request):
    if request.method =='POST':
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
            print(email,password)   
            
            user = verify_user(request, email=email, password=password)
            print("login ka ",user)

            if user :
                # login(request, user)
                print("idar  aaya aayaa par kch ni hua")
                return render(request, 'index.html')  # Replace with the appropriate URL
            else:
                # Authentication failed
                print("Fail")
                message = 'Incorrect email or password. Please try again.'
                return render(request, 'login.html',{'message': message})
        except:
            pass
            message="Pls Enter Password"
            print("User not Registered")
            return render(request, 'login.html',{'message': message})
    
    print('login')
    return render(request, 'login.html')

def signup(request):
    print('test')
    if request.method == 'POST':
        
        form_data = request.POST
        author=form_data.get('name')
        
         # Create an instance of the model and populate it with form data
        #  for now categories nahi le rhi
        try:
            my_model_instance = User(
                name=form_data.get('name'),
                email=form_data.get('email'),
                password=form_data.get('password'),
                phone_number=form_data.get('phone_number')
                # phone_number=form_data['field_name2'],
                # Populate other fields as needed
               
            )
            my_model_instance.save()
            request.session['name'] = author
            print(request.session['name'])
            return redirect('login') 
        except IntegrityError:
            print("idar nahi aana chhye")
            return render(request,'signup.html',{'message':"Email already exists! please Login"})
            
            
        # Save the instance to the database
       

    return render(request, 'signup.html')

def texteditor(request):
    author = request.session.get('name')
    print(author)
    print('test')
    if request.method == 'POST':
        # Get the form data
        title = request.POST.get('title')
        # author = request.POST.get('author')
        category_name = request.POST.get('category')
        content = request.POST.get('content')

        # Handle image upload
        image = request.FILES.get('image')
        if image:
            # Generate a unique filename
            filename = os.path.join('blog_images', image.name)
            filepath = default_storage.save(filename, image)

        # Create a new Blog object and save it to the database
        blog = Blog(
            title=title,
            author=author,
            category=category_name,
            content=content,
            image=filepath if image else None,
        )
        blog.save()

        return redirect('blogs')  # Redirect to a view that lists all blogs


    return render(request, 'texteditor.html')
