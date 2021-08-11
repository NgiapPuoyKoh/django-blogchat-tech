from django.conf.urls import url
from django.shortcuts import render, get_object_or_404, redirect
# from blog.models import Post 
from .models import Post, Topic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse


# Create your views here.

def blog(request):
    """ A view to return the Blog Page """
    return render(request, "blog/blog.html")


def all_posts(request):
    """ A view to show all posts, including sorting and search queries """

    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'blog/posts.html', context)



def post_detail(request, slug):
    """ A view to show individual post details """

    post = get_object_or_404(Post, slug=slug, status='published')

    context = {
        'post': post,
    }

    return render(request, 'blog/post_detail.html', context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post

    fields = [
        'title',
        'excerpt',
        'content',
        'topic',
        'status'
        # 'slug'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        # form.instance.slug = slugify(self.post.title)
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse('post_detail', kwargs={'slug': self.post})

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post

    fields = [
        'title',
        'excerpt',
        'content',
        'topic',
        'status'
        # 'slug'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        # form.instance.slug = slugify(self.post.title)
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()
        if self.request.user  == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'


    def test_func(self):
        post = self.get_object()
        if self.request.user  == post.author:
            return True
        return False

class TopicListView(ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'topiclist'

    def get_queryset(self):
        content = {
            'topic': self.kwargs['topic'],
            'posts': Post.objects.filter(topic__name=self.kwargs['topic']).filter(status='published')
        }
        return content

# def add_post(request, user):
#     """ A function to create a blog post and 
#     render the add_blog page "
    
# def PostDetailView(DetailView):
#     model = Post


#<app>/<model>_<viewtype>.html