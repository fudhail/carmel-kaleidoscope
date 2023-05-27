from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from blog.models import Category, Post, SubCategory
from account.models import MyUser, User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.views import View
from django.views.generic import FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.forms import ContactForm, PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from main.views import HomePage
from django.db.models import Q

# Create your views here.
# class SearchView(ListView):
#     model = Post
#     context_object_name = "posts"
#     template_name = "blog/search.html"

#     def get_queryset(self):
#         query = self.request.GET['query']
#         title_queryset = Post.objects.filter(status="P", title__icontains=query)
#         content_queryset = Post.objects.filter(status="P", content__icontains=query)
#         queryset = title_queryset.union(content_queryset)
#         return queryset

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def LikeView(request, slug):
    post = Post.objects.get(slug=slug)
    ip = get_client_ip(request)
    user=User.objects.get(user=ip)
    liked = False
    if post.likes.filter(id=user.id).exists():
        post.likes.remove(user.id)
        liked = False
    else:
        post.likes.add(user.id)
        liked = True
    return HttpResponseRedirect(reverse('post-detail', args=[slug]))


class CategoryView(ListView):
    model = SubCategory
    context_object_name = "subcategories"
    template_name = "blog/sub_categories.html"
    queryset = Post.objects.filter(status="P")

    def get_context_data(self):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()

        context['slug'] = Category.objects.get(slug=self.request.resolver_match.kwargs.get('slug'))
        return context

    def get_queryset(self):
        category = Category.objects.get(slug = self.request.resolver_match.kwargs.get('slug'))
        queryset = SubCategory.objects.filter(category=category)
        return queryset

class SubCategoryView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/blog-post-list.html"
    paginate_by = 10
    queryset = Post.objects.filter(status="P")

    def get_context_data(self):
        context = super().get_context_data()
        context['subcategories'] = Category.objects.all()
        context['slug'] = SubCategory.objects.get(slug=self.request.resolver_match.kwargs.get('slug'))
        return context

    def get_queryset(self):
        category = SubCategory.objects.get(slug = self.request.resolver_match.kwargs.get('slug'))
        queryset = Post.objects.filter(subcategory=category)
        return queryset

class ContactView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy("contact-us")
    template_name = "blog/contact_us.html"

class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/index.html"
    queryset = Post.objects.filter(status="P")

    def get_context_data(self):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        context['avatar'] = MyUser.objects.all()
        return context


class PostView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/all_post.html"
    paginate_by = 10
    queryset = Post.objects.filter(status="P")

    def get_context_data(self):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        return context

class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/blog-post.html"
    queryset = Post.objects.filter(status="P")
    def get_context_data(self, *args, **kwargs):
        post_likes = Post.objects.get(slug=self.kwargs['slug'])
        total_likes = post_likes.total_likes()
        ip = get_client_ip(self.request)
        user=User.objects.get(user=ip)
        liked = False
        if post_likes.likes.filter(id=user.id).exists():
            liked = True
        else:
            liked = False
        context = super().get_context_data()
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = "/accounts/login"
    permission_required = "blog.add_post"
    form_class = PostForm
    template_name = "blog/post_create_update.html"
    success_url = "/accounts/my-posts"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = MyUser.objects.get(username= self.request.user)
        kwargs.update({'initial':{'author': user}})
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = "/accounts/login"
    permission_required = "blog.change_post"
    model = Post
    form_class = PostForm
    template_name = "blog/post_create_update.html"
    success_url = "/accounts/my-posts"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = MyUser.objects.get(username= self.request.user)
        kwargs.update({'initial':{'author': user}})
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self, *args, **kwargs):
        current_user = self.request.user
        post_obj = Post.objects.get(slug=self.kwargs.get('slug'))
        post_user = post_obj.author
        if current_user == post_user:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = "/accounts/login"
    permission_required = "blog.delete_post"
    model = Post
    success_url = reverse_lazy('my-posts')
    template_name = "blog/post_delete.html"

    def test_func(self, *args, **kwargs):
        current_user = self.request.user
        post_obj = Post.objects.get(slug=self.kwargs.get('slug'))
        post_user = post_obj.author
        if current_user == post_user:
            return True
        else:
            return False
