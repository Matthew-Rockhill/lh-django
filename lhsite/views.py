from django.shortcuts import render

def index(request):
  return render(request, 'home.html')

def about_us(request):
  return render(request, 'about-us.html')

def sermons(request):
  return render(request, 'sermons.html')

def contact_us(request):
  return render(request, 'contact-us.html')