from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Auto
from .forms import AutoForm


def lista_autos(request):
    """Vista que muestra la lista de todos los autos registrados."""
    autos = Auto.objects.all()
    total = autos.count()
    context = {
        'autos': autos,
        'total': total,
    }
    return render(request, 'autos/lista_autos.html', context)


def agregar_auto(request):
    """Vista con formulario para agregar un nuevo auto."""
    if request.method == 'POST':
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Auto agregado exitosamente!')
            return redirect('lista_autos')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = AutoForm()

    context = {
        'form': form,
        'titulo': 'Agregar Nuevo Auto',
    }
    return render(request, 'autos/agregar_auto.html', context)
