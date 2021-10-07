from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """Home Page"""
    return HttpResponse('Home Page')


def room(request):
    """Room Page"""
    return HttpResponse('Room')
