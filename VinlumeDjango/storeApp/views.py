from django.shortcuts import render

# Create your views here.

def store_lobby(request):
    return render(request, 'storeApp/store_home.html')