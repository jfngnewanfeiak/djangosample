from django.urls import path
from . import views
app_name ='webapp'

urlpatterns = [
    path('post_list', views.PostListView.as_view(), name='post_list'),
    path('post_create', views.PostCreateView.as_view(), name='post_create'),
    path('post_detail/<int:pk>/', view=views.PostDetailView.as_view(), name='post_detail'),
    path('post_update/<int:pk>', view=views.PostUpdateView.as_view(), name='post_update'),
    path('post_delete/<int:pk>/', view=views.PostDeleteView.as_view(), name="post_delete")
]