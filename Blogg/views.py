from django.shortcuts import render,redirect
from django.db import models
from .models import *
from django.db import IntegrityError 
from django.http import HttpResponse
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

def search(request):
    print('search')
    if request.method == 'POST':
        form_data = request.POST
        search=form_data.get('search')
        try:
            ref = Blog.objects.get(title=search)
            id = ref.id
            print(id)
            return blogs(request,id)
            
        except:
            return index(request)
        
        print(search)
    
def index(request,context=None):
    print('index')
    if context==None:
        posts = Blog.objects.all()[:12]
    else:
        return render(request,'index.html',context)
    
    context={
        'keypost':posts[:12]
    }
   
    return render(request, 'index.html',context)

def blogs(request,pk):
    print('blogs')
    blog_id = pk
    # blog_id = request.session.get('blog_id')
    print(blog_id)
    blogRef =Blog.objects.get( id=blog_id)
    print(blogRef)
    context = {
        'blog' : blogRef,
        'blog_id':blog_id,
        'message':"Blog Created Successfully"
    }
    print(context['blog'].title)
    return render(request, 'blogs.html',context)

def login(request):
    
    if request.method =='POST':
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
            print(email,password)   
            
            user = verify_user(request, email=email, password=password)
            
            print("login ka ",user)
            
            print(user.id)
            print(user.name)
            posts = Blog.objects.all()
            print(posts)
    
            context={
                 'keypost':posts
            }
   

            if user :
                # login(request, user)
                print("idar  aaya aayaa par kch ni hua")  
                print(user.name)
                request.session['name'] = user.name
                request.session['id'] = user.id
                return render(request, 'index.html',context)  # Replace with the appropriate URL
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
            user_id = my_model_instance.id

            print("Inserted ID:", user_id)
            # request.session['name'] = author
            # request.session['id'] = user_id
            # print(request.session['name'])
            # print(request.session['id'])
            return redirect('login') 
        except IntegrityError:
            print("idar nahi aana chhye")
            return render(request,'signup.html',{'message':"Email already exists! please Login"})

    return render(request, 'signup.html')

def texteditor(request):
    print(request.session.get('name'))
    # author='khsho'
    author  = request.session.get('name')
    user_id  = request.session.get('id')
    ref = User.objects.get(id=user_id)
    print(author)
    print(user_id)
    print(ref)
    # print(abc)
    print('test')
    if request.method == 'POST':
        # Get the form data
        title = request.POST.get('title')
        # author = request.POST.get('author')
        category_name = request.POST.get('category')
        content = request.POST.get('content')

        # Handle image upload
        image = request.FILES.get('image')
        print(request.FILES)
        if image:
            # Generate a unique filename
            filename = os.path.join('media/blog_images', image.name)
            filepath = default_storage.save(filename, image)

        # Create a new Blog object and save it to the database
        blog = Blog(
            title=title,
            author=author,
            category=category_name,
            content=content,
            user=ref,
            image=filepath if image else None,
        )
        blog.save()
        blog_id = blog.id
        request.session['blog_id'] = blog_id 
        print(blog_id)
        blogRef =Blog.objects.get(  id=blog_id)
        print(blogRef)
        context = {
            'blog' : blogRef,
        }
        print(context['blog'].title)
        # return render(request,'blogs.html',{'blog_id':blog_id, 'message':"Blog Created Successfully"},context)  
        return render(request,'success.html')  


    return render(request, 'texteditor.html')
def success(request):
    print('success')
    return render(request, 'success.html')
def my_blogs(request):
    user_id  = request.session.get('id')
    print(user_id)
    ref = User.objects.get(id=user_id)
    print(ref)
    blogs = Blog.objects.filter(user=ref)
    print(blogs)
    
    context={
        'keypost':blogs,
        'name':ref.name
    }
    print(context)
    return render(request, 'my_blogs.html',context)

from django.http import HttpResponse

def partial_template(request,category):
    # Get the anchor text from the query parameter
    print('partial_template',category)
    anchor_text = request.GET.get('anchor', '')
    print(anchor_text)
    

    # Depending on the anchor_text or other parameters, you can generate dynamic content here
    # For this example, we'll concatenate the anchor text with some new content
    new_content = f"New content for the div based on anchor text: {anchor_text}"
    if anchor_text=='Featured':
        blogs = Blog.objects.all()
        
    else:
        blogs = Blog.objects.filter(category=category)
    context = {
        'keypost':blogs,
        'category':category,
    }
    
    print(anchor_text)
    for i in blogs:
        print(i.title)
    return index(request,context)
    # return render(request,'partial_template.html',context)

def edit_profile(request):
    user_id  = request.session.get('id')
    print(user_id)
    ref = User.objects.get(id=user_id)
    
    if request.method == 'POST':
       
        ref.name = request.POST.get('name')
        ref.email = request.POST.get('email')
        ref.phone_number = request.POST.get('phone_number')
        ref.password = request.POST.get('password')
        ref.save()
        return index(request)
    return render(request, 'edit_profile.html',{'context':ref})
    