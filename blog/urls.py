from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogUpdateView, BlogDetailView, BlogDeleteView, toggle_activity

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('edit<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('view<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('activity/<int:pk>/', toggle_activity, name='toggle_activity')

]
