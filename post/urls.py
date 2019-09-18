from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list, name='post_list'),
    path('about',views.about, name='about'),
    path('editorinchief',views.editorinchief, name='editorinchief'),
    path('contact',views.contact, name='contact'),
    path('blog',views.blog, name='blog'),
    path('post_detail/<int:pk>/',views.post_detail,name='post_detail'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.c, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.a, name='comment_remove'),
]