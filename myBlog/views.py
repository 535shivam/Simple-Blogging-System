from django.shortcuts import render , get_object_or_404 , redirect
from .models import *
from .forms import *

def post_list_view(request):
    posts = PostModel.objects.order_by('-create_at')
    return render(request,'postlist.html',{'posts':posts})

def post_detail_view(request,pk):
    post = get_object_or_404(PostModel,pk=pk)
    return render(request,'postdetail.html',{'post':post})

def post_add_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
        return render(request,'postadd.html',{'form':form})
    
def post_update_view(request,pk):
    post = get_object_or_404(PostModel,pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST ,request.FILES or None , instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request,'postadd.html',{'form':form})


def post_delete_view(request,pk):
    post = get_object_or_404(PostModel , pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    else:
        return render(request,'postdelete.html',{'post':post})