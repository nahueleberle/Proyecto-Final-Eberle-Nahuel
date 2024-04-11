from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import logout, login, authenticate
from core.forms import UserRegisterForm, AvatarFormulario
from core.models import Avatar
# Create your views here.
def home(request):
    return render(request, "core/home.html")

#@login_required
def products(request):
    return render(request, "core/products.html")

def exit(request):
    logout(request)
    return redirect('home')

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request,user)

                return render(request,"core/home.html", {"mensaje":f"Bienvenido{usuario}"})
            else:
                return render(request,"core/home.html", {"mensaje":"Error, datos incorrectos"})
        else:
            return render(request,"core/home.html", {"mensaje":"Error, formulario erroneo"})
        
    form = AuthenticationForm()

    return render(request,"core/login.html", {'form':form})

def register(request):
    
    if request.method == 'POST':
         
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, "core/home.html" , {"mensaje":"Usuario Creado :)"})
        
    else:
        
        #form = UserCreationForm()
        form = UserRegisterForm()

    return render(request,"core/registro.html" , {"form":form})

@login_required
def agregar_avatar(request):
    if request.method == 'POST':
         
        formulario = AvatarFormulario(request.POST, request.FILES)

        if formulario.is_valid():

            info = formulario.cleaned_data

            usuario_actual = User.objects.get(username=request.user)
            nuevo_avatar = Avatar(usuario=usuario_actual, imagen=info ["imagen"])

            nuevo_avatar.save()
            return render(request, "core/home.html" , {"mensaje":"Avatar Creado :)"})
        
    else:
        
        formulario = AvatarFormulario()


    return render(request,"core/nuevo_avatar.html" , {"formu":formulario})

def profile(request):
    return render(request, "core/perfil.html")