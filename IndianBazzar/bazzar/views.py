from django.shortcuts import render

def index(request):
        return render(request, 'bazzar/bazzar_index.html')

def hours(request):
        return render(request,'bazzar/hours.html')