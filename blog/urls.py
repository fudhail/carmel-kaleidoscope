from django.urls import path
from blog.views import PostView, LikeView, CategoryView, SubCategoryView, ContactView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    # path('search', SearchView.as_view(), name="search"),
    path('category/<slug:slug>', CategoryView.as_view(), name="category"),
    path('subcategory/<slug:slug>', SubCategoryView.as_view(), name="subcategory"),
    path('contact-us',ContactView.as_view(), name="contact-us"),

    path('', PostListView.as_view(), name="index"),
    path('all-posts/', PostView.as_view(), name="all-posts"),
    path('posts/<slug:slug>', PostDetailView.as_view(), name="post-detail"),

    path('posts', PostCreateView.as_view(), name="post-create"),
    path('posts/<slug:slug>/update', PostUpdateView.as_view(), name="post-update"),
    path('posts/<slug:slug>/delete', PostDeleteView.as_view(), name="post-delete"),
    path('like-post/<slug:slug>', LikeView, name='like-post'),


]
