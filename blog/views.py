from django.conf.urls import url
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from .models import Post, Topic, Comment
from blog.forms import NewCommentForm


# Create your views here.q

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
    """ A view to display individual post details with comments and comment form """

    post = get_object_or_404(Post, slug=slug, status='published')

    comments = post.comments.filter(status=True)

    user_comment = None

    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.save()
            return redirect(reverse('post_detail', args=[slug]))
    else:
        comment_form = NewCommentForm()

        context = {
            'post': post, 
            'comments':  user_comment, 
            'comments': comments, 
            'comment_form': comment_form
        }
        return render(request, 'blog/post_detail.html', context )
 

class PostCreateView(LoginRequiredMixin, CreateView):
    """ A view to create a blog post """
    model = Post

    fields = [
        'title',
        'excerpt',
        'content',
        'topic',
        'status'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ A view to update a blog post """
    model = Post

    fields = [
        'title',
        'excerpt',
        'content',
        'topic',
        'status'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()
        if self.request.user  == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ A view to Delete a blog post """
    model = Post
    success_url = '/'


    def test_func(self):
        post = self.get_object()
        if self.request.user  == post.author:
            return True
        return False


class TopicListView(ListView):
    """ A view to list topics """

    template_name = 'blog/post_list.html'
    context_object_name = 'topiclist'

    def get_queryset(self):
        content = {
            'topic': self.kwargs['topic'],
            'posts': Post.objects.filter(topic__name=self.kwargs['topic']).filter(status='published')
        }
        return content

def topic_list(request):
    ''' Topic list for dynamic dropdown nav item '''
    topic_list = Topic.objects.exclude(name='No Topic')
    context = {
        "topic_list": topic_list,
    }
    return context

