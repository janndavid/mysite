from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
                            ListView,
                            DetailView,
                            CreateView,
                            UpdateView,
                            DeleteView)
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


# Function based view
def home(request):
    # Render metoden tager tre argumenter, hvor den tredje netop er kontekst.
    # Dette argument bruger vi til at sende data som html-filen kan render ud
    # fra, hvilket kan være navne, datoer osv.
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


# Forneden er et class based view som bruges oftere end function based views
# Dog er konvention for template_name følgende: <app>/<model>_<viewtype>.html
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


# Her vil vi navngive template efter: <app>/<model>_<viewtype>.html
class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    success_url = "/blog"


def about(request):
    return render(request, 'blog/about.html')
