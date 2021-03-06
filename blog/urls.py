from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog'),
    path('new/', views.BlogCreateView.as_view(), name='blog_new'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('<int:pk>/edit', views.BlogUpdateView.as_view(), name='blog_edit'),
    path('<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog_delete'),
]