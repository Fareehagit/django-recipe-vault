from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required


User = get_user_model()

# Create your views here.
@login_required(login_url="/login/")
def reciepes(request):
    if request.method == "POST":

        data = request.POST
        reciepe_name = data.get('reciepe_name')
        reciepe_description = data.get('reciepe_description')
        reciepe_image = request.FILES.get('reciepe_image')

        Reciepe.objects.create(
            reciepe_name = reciepe_name,
            reciepe_description =reciepe_description, 
            reciepe_image  = reciepe_image,
        )

        return redirect('/reciepes')

       
    
    queryset = Reciepe.objects.all().order_by('id')

    if request.GET.get('search_re'):
        queryset = queryset.filter(reciepe_name__icontains = request.GET.get('search_re'))

        
    context = {'reciepes': queryset}

    return render(request, 'reciepes.html', context)

def delete_recipe(request, id):
    queryset = Reciepe.objects.get(id = id)
    queryset.delete()
    
    return redirect('/reciepes')

def update_recipe(request, id):
    queryset = Reciepe.objects.get(id = id)

    if request.method == "POST":

        data = request.POST
        reciepe_name = data.get('reciepe_name')
        reciepe_description = data.get('reciepe_description')
        reciepe_image = request.FILES.get('reciepe_image')

        queryset.reciepe_name = reciepe_name
        queryset.reciepe_description = reciepe_description

        if reciepe_image:
            queryset.reciepe_image = reciepe_image

        queryset.save()

        return redirect('/reciepes')

    context = {'recipe': queryset}

    return render(request, 'update_recipe.html', context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        print("User authenticated:", user)

        if user is None:
            messages.error(request, "Invalid credentials")
            return redirect('/login')
        else:
            login(request, user)
            return redirect('/reciepes')
        
    return render(request, 'login.html')

def logout_page(request):
    logout(request)

    return redirect('/login')



def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password') # None

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "Username already taken.")
            return redirect('/register')
        
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            )
        print("Password (after create_user):", user.id)

        messages.info(request, "Account created successfully.")

    return render(request, 'register.html')