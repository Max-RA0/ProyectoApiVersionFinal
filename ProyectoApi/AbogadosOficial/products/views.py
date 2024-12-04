from django.shortcuts import render, redirect, get_object_or_404
from .models import Divorcio, AsesoriaLegal, ServicioLegal
from .forms import SearchForm, DivorcioForm, AsesoriaLegalForm
from django.http import JsonResponse
from rest_framework import viewsets
from .serializer import ServicioLegalSerializer, DivorcioSerializer, AsesoriaLegalSerializer

class AsesoriaLegalViewSet(viewsets.ModelViewSet):
    queryset = AsesoriaLegal.objects.all()
    serializer_class = AsesoriaLegalSerializer

class DivorcioViewSet(viewsets.ModelViewSet):
    queryset = Divorcio.objects.all()
    serializer_class = DivorcioSerializer

class ServicioLegalViewSet(viewsets.ModelViewSet):
    queryset = ServicioLegal.objects.all()
    serializer_class = ServicioLegalSerializer
    
def mostrar_info_servicio(servicio):
    # Devuelve la información en formato de string
    if isinstance(servicio, Divorcio):
        return (f"Nombre: {servicio.nombre_servicio}, Descripción: {servicio.descripcion}, "
                f"Costo: {servicio.costo}, Número de Divorcios: {servicio.num_divorcios}, "
                f"Duración Estimada: {servicio.duracion_estimada} años, ")
    elif isinstance(servicio, AsesoriaLegal):
        return (f"Nombre: {servicio.nombre_servicio}, Descripción: {servicio.descripcion}, "
                f"Costo: {servicio.costo}, Especialidad: {servicio.especialidad},")
    else:
        return "Información no disponible"
# Página principal con el listado de asesorías legales
def home(request):
    # Obtener todos los servicios de asesoría y divorcio
    servicios_asesoria = AsesoriaLegal.objects.all()
    servicios_divorcio = Divorcio.objects.all()

    # Añadir los detalles de cada servicio
    detalles_asesoria = [mostrar_info_servicio(servicio) for servicio in servicios_asesoria]
    detalles_divorcio = [mostrar_info_servicio(servicio) for servicio in servicios_divorcio]

    # Pasar los servicios y detalles al contexto
    context = {
        'servicios_asesoria': zip(servicios_asesoria, detalles_asesoria),  # Asociamos cada servicio con su detalle
        'servicios_divorcio': zip(servicios_divorcio, detalles_divorcio),
    }
    return render(request, 'home.html', context)

def lista_asesoria(request, tipo):
    if tipo == 'juridico':
        asesorias = AsesoriaLegal.objects.filter(cargo__icontains='juridico')
    elif tipo == 'financiero':
        asesorias = AsesoriaLegal.objects.filter(cargo__icontains='financiero')
    else:
        asesorias = AsesoriaLegal.objects.all()

    return render(request, 'lista_asesoria.html', {
        'asesorias': asesorias,
        'tipo': tipo
    })
    
def lista_servicios(request, tipo):
    # Filtrar los servicios según el tipo (divorcio o asesoría)
    if tipo == 'divorcio':
        servicios = Divorcio.objects.all()
    elif tipo == 'asesoria':
        servicios = AsesoriaLegal.objects.all()
    else:
        servicios = []

  # Obtener los detalles de los servicios // mostrar_info es el metodo que se sobreescribe pata cada una de las clases hijas
    detalles_servicios = [mostrar_info_servicio(servicio) for servicio in servicios]

    return render(request, 'lista_servicios.html', {'tipo': tipo, 'servicios': servicios, 'detalles': detalles_servicios})
    
def crear_servicio(request, tipo):
    # Selección del formulario dependiendo del tipo
    if tipo == 'asesoria':
        form_class = AsesoriaLegalForm
    elif tipo == 'divorcio':
        form_class = DivorcioForm
    else:
        return redirect('lista_asesoria', tipo='asesoria')
    
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir al tipo correcto de lista de servicios
            if tipo == 'asesoria':
                return redirect('lista_asesoria', tipo='asesoria')
            else:
                return redirect('lista_servicios', tipo='divorcio')
    else:
        form = form_class()
    
    return render(request, 'crear_servicios.html', {'form': form, 'tipo': tipo})

def editar_servicio(request, tipo, pk):
    # Determinar el modelo y formulario según el tipo
    if tipo == 'asesoria':
        model = AsesoriaLegal
        form_class = AsesoriaLegalForm
    elif tipo == 'divorcio':
        model = Divorcio
        form_class = DivorcioForm
    else:
        return redirect('lista_asesoria', tipo='asesoria')
    
    # Obtener el servicio con la pk proporcionada
    servicio = get_object_or_404(model, pk=pk)
    
    if request.method == 'POST':
        form = form_class(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            # Redirigir al tipo correcto de lista de servicios
            if tipo == 'asesoria':
                return redirect('lista_asesoria', tipo='asesoria')
            else:
                return redirect('lista_servicios', tipo='divorcio')
    else:
        form = form_class(instance=servicio)
    
    return render(request, 'editar_servicios.html', {'form': form, 'tipo': tipo, 'servicio': servicio})

def eliminar_servicio(request, pk):
    # Intentar obtener el servicio como asesoría legal
    try:
        servicio = AsesoriaLegal.objects.get(pk=pk)
        tipo = 'asesoria'
    except AsesoriaLegal.DoesNotExist:
        # Si no es asesoría, intentamos obtenerlo como divorcio
        try:
            servicio = Divorcio.objects.get(pk=pk)
            tipo = 'divorcio'
        except Divorcio.DoesNotExist:
            return redirect('error_servicio_no_encontrado')
    
    # Eliminar el servicio
    if servicio:
        servicio.delete()
    
    # Redirigir al tipo correcto de lista de servicios
    if tipo == 'asesoria':
        return redirect('lista_asesoria', tipo='asesoria')
    else:
        return redirect('lista_servicios', tipo='divorcio')
    
def search(request):
    query = request.GET.get('query', '')
    resultados_divorcio = []
    resultados_asesoria = []
    
    if not query:
        return redirect('home')
    
    if query:
        resultados_divorcio = Divorcio.objects.filter(nombre_servicio__icontains=query)
        resultados_asesoria = AsesoriaLegal.objects.filter(nombre_servicio__icontains=query)
    
    # Obtener los detalles de cada servicio
    detalles_divorcio = [mostrar_info_servicio(servicio) for servicio in resultados_divorcio]
    detalles_asesoria = [mostrar_info_servicio(servicio) for servicio in resultados_asesoria]

    context = {
        'query': query,
        'servicios_divorcio': zip(resultados_divorcio, detalles_divorcio),
        'servicios_asesoria': zip(resultados_asesoria, detalles_asesoria),
    }
    
    return render(request, 'home.html', context)
