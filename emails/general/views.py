# -*- encoding: utf-8 -*-
from django.shortcuts import render

from .models import Person

def index(request):
    return render(request, 'home.html')

def list(request):
    people = Person.get_all_people()
    return render(request, 'list.html', {'people': people})

def add(request):
    contexto = {}
    if request.method == 'POST':
        print request.POST
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        if not name:
            contexto.update({'error_name': 'Preencha o campo nome'})
        else:
            contexto.update({'name': name})
        if not email:
            contexto.update({'error_email': 'Preencha o campo email'})
        else:
            contexto.update({'email': email})

        if name and email:
            pessoa, c = Person.objects.get_or_create(email=email)
            if pessoa:
                pessoa.name = name
                pessoa.save()

            contexto.update({'success': 'Formulário enviado com sucesso!'})
    print contexto
    return render(request, 'add.html', contexto)