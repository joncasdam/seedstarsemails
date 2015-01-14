# -*- encoding: utf-8 -*-
from django.shortcuts import render

from .models import Person

def index(request):
    return render(request)

def list(request):
    people = Person.get_all_people()
    return render(request)

def add(request):
    return render(request)