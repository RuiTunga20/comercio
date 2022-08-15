
# Create your views here.
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'index.html')


def loja(request):
    return render(request,'shop.html')