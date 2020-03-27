from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Dummy data:
posts = [
    {
    'author': 'Jann Jacobsen',
    'title': 'Ny blog!',
    'content': 'Lige lavet en ny blog!',
    'date_posted': '13. marts, 2020'
    },
    {
    'author': 'Pernille Kjær',
    'title': 'Bedste blog nogensinde!',
    'content': 'Min kæreste har lavet verdens bedste blog!',
    'date_posted': '14. marts, 2020'
    },
    {
    'author': 'Simon Bendixen',
    'title': 'Jeg kunne aldrig selv lave en blog',
    'content': 'Jann er bare meget bedre end mig fordi han bruger OSX.',
    'date_posted': '15. marts, 2020'
    },
]


# Create your views here.
def home(request):
    # Render metoden tager tre argumenter, hvor den tredje netop er kontekst.
    # Dette argument bruger vi til at sende data som html-filen kan render ud
    # fra, hvilket kan være navne, datoer osv.
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
