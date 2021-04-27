from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.contrib.auth.models import User

from .models import Post

post = [
    {
        'author': 'ganeshG',
        'title': "Django",
        'content': 'Best of Both worlds',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Rahul',
        'title': "php",
        'content': 'Made a project earlier',
        'date_posted': 'August 28, 2018'
    }
]


# Create your views here.
def home(request):
    # context = {'post': post}
    context = {'post': Post.objects.all()}
    return render(request, 'Blog/home.html', context=context)


class PostListView(ListView):
    model = Post
    template_name = 'Blog/home.html'
    # for looping
    context_object_name = 'post'
    ordering = ['-date_posted']
    paginate_by = 4


class UserPostListView(ListView):
    model = Post
    template_name = 'Blog/user_posts.html'
    # for looping
    context_object_name = 'post'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'linkV', 'ChannelV', 'PlaylistV', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'linkV', 'ChannelV', 'PlaylistV', 'image']

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
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'Blog/about.html', {'title': 'About'})


def Search(request):
    return render(request, 'Blog/Search.html', {'title': 'Search'})
