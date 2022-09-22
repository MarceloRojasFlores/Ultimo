# from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Curso, Docente
from django.contrib.auth import logout,authenticate,login

# Create your views here.

def index(request):
    return render(request,'index.html')

def actividad(request):
    return render(request,'actividad.html')

def infraestructura(request):
    return render(request,'infraestructura.html')

def nuestraHistoria(request):
    return render(request,'nuestraHistoria.html')       

def IniciarSesion(request):
    return render(request,'IniciarSesion.html')  


def login_autenticacion(request):
    if request.method=="POST":
        username = request.POST['usuario']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        
        else:
            messages.success(request,'error al iniciar sesion')
            # Return an 'invalid login' error message.
            return redirect('login_auth')
    else:
        return render(request,'login_auntenticacion.html')    
    




def home(request):
    cursos_listados = Curso.objects.all()
    # cursos_listados = Curso.objects.all()[:5]
    # cursos_listados = Curso.objects.all()[4:9]
    # cursos_listados = Curso.objects.all().order_by('nombre')
    # cursos_listados = Curso.objects.all().order_by('-nombre')
    # cursos_listados = Curso.objects.all().order_by('nombre', 'creditos')
    # cursos_listados = Curso.objects.filter(nombre='Historia', creditos=5)
    # cursos_listados = Curso.objects.filter(creditos__lte=4)
    # cursos_listados = Curso.objects.filter(nombre__startswith='Q')
    # cursos_listados = Curso.objects.filter(nombre__contains='g')

    # return HttpResponse("<h1>Hola Mundo!</h1>")
    data = {
        'titulo': 'Gestión de Cursos',
        'cursos': cursos_listados
    }
    # return render(request, "gestionCursos.html", {"cursos": cursos_listados})
    return render(request, "gestionCursos.html", data)


class CursoListView(ListView):
    model = Curso
    template_name = 'gestionCursos.html'

    def get_queryset(self):
        # return Curso.objects.filter(creditos__lte=4)
        return Curso.objects.all().order_by('nombre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Gestión de Cursos'
        # print(context)
        return context


def registrar_curso(request):
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.create(nombre=nombre, creditos=creditos)
    return redirect('/')


def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    return redirect('/')


def edicion_curso(request, id):
    curso = Curso.objects.get(id=id)
    data = {
        'titulo': 'Edición de Curso',
        'curso': curso
    }

    return render(request, "edicionCurso.html", data)


def editar_curso(request):
    id = int(request.POST['id'])
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(id=id)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    return redirect('/')


def contacto(request):
    return render(request, "contacto.html")
