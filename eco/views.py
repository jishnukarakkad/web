from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def product(request):
    return render(request,'product.html')

def cart(request):
    return render(request,'cart.html')
def review(request):
    return render(request,'review.html')