from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm, SeleccionInteresesForm
from .models import *
import logging
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

# Create your views here.
logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'pages/index.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirigir a la página principal después del inicio de sesión
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def registro_usuario(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = form.save()
            request.session['usuario_id'] = usuario.id  # Guardamos el id del usuario en la sesión
            return redirect('seleccion_intereses')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registration/registro.html', {'form': form})

def seleccion_intereses(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('registro_usuario')
    
    if request.method == "POST":
        form = SeleccionInteresesForm(request.POST)
        if form.is_valid():
            intereses = form.cleaned_data['intereses']
            usuario = Usuario.objects.get(id=usuario_id)
            for interes in intereses:
                UsuarioInteres.objects.create(id_usuario=usuario, id_interes=interes)
            # Autenticar al usuario recién registrado
            user = authenticate(request, username=usuario.correo, password=usuario.contrasena)
            if user is not None:
                login(request, user)
            del request.session['usuario_id']  # Eliminamos el id del usuario de la sesión
            # Redirigir a la página principal después del registro
            return redirect('home')  
    else:
        form = SeleccionInteresesForm()
    return render(request, 'registration/seleccion_intereses.html', {'form': form})

@login_required
def home_view(request):
    return render(request, 'user/home.html')

def logout_view(request):
    logout(request)
    return redirect('index')