from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing(request):
    return render(request, 'landingpage/landing.html')

def landing_test(request):
    return HttpResponse('<h1>Landing test page</h1>')
