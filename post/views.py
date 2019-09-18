from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.utils import timezone
from .models import Post, Editor,Remark, Contact
from .forms import CommentForm, ContactForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.
def blog(request):
    postList = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    query = request.GET.get('q')
    if query:
        postList = postList.filter(
            Q(title__icontains=query) |
            Q(text__icontains=query) 
        ).distinct()
    paginator = Paginator(postList, 4)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'post/blog.html', {'posts': posts})

def about(request):
    autobiographiers = Editor.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'post/about.html', {'autobiographiers':autobiographiers} )
def editorinchief(request):
    return render(request,'post/editorinchief.html',{})
def contact(request):
    form = ContactForm(request.POST)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect('contact')
        else:
            form=ContactForm()
    return render(request,'post/contact.html',{'form':form})
def post_list(request):
    return render(request,'post/post_list.html',{})
def post_detail(request, pk):
    post= get_object_or_404(Post, pk=pk)
    return render(request, 'post/post_detail.html',{'post':post})
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'post/add_comment_to_post.html', {'form': form})
@login_required
def c(request, pk):
    comment = get_object_or_404(Remark, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def a(request, pk):
    comment = get_object_or_404(Remark, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)