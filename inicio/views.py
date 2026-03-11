from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return HttpResponse("¡holiis! soy belen 💋")
def perro(request):
    return HttpResponse("Soy un perrito me llamo duende y hago guau guau 🐶")

def gato(request):
    return HttpResponse("Soy un gatito me llamo chimuela y hago miau miau 🐱")

   