from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Person

class IndexView(generic.ListView):
    model = Person
    # latest_person = Person.objects.order_by('name')
    template_name = 'agenda_personal/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['person'] = Person.objects.all()
        return context

class ResultView(generic.DetailView):
    model = Person
    template_name = 'agenda_personal/result.html'
    context_object_name = 'person'

    def post(self, request, *args, **kwargs):
        # Obtener datos del formulario
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        age = request.POST.get('age')

        # Crear una nueva instancia de Person y guardarla en la base de datos
        person = Person.objects.create(name=name, surname=surname, age=age)

        # Redirigir a una página de éxito o a donde necesites
        return HttpResponseRedirect(reverse('agenda_personal:result'))