from django.shortcuts import render

# Create your views here.
#Las vistas son funciones de python

def home(request):
    return render(request,'index.html')

def ingreso(request):
	return render(request,"entrada.html")

def salida(request):
	return render(request,"salida.html")
