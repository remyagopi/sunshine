from django.shortcuts import render,get_object_or_404,redirect,Http404
from .models import Post
from .forms import PostForm
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.db.models import Q

def PostList(request):
    qs=Post.objects.all()
    query=request.GET.get('q')
    if query:
        qs=qs.filter(Q(title__icontains=query)|Q(content__icontains=query)).distinct()
    paginator = Paginator(qs,8)
    page=request.GET.get('page')
    qs=paginator.get_page(page)
    context={
        'contacts':qs
    }
    return render(request,'list.html',context)

def PostDetailView(request,pk):

    query = get_object_or_404(Post,pk=pk)
    context={
        'query':query
    }
    return render(request,'detail.html',context)

def PostCreateView(request):
    if not request.user.is_authenticated:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
       instance= form.save(commit=False)
       instance.user=request.user
       instance.save()
       return redirect('post:list')

    return render(request,'post_form.html',{'form':form})

def PostDeleteView(request,pk):
    if Post.objects.filter(user=request.user):
     query = get_object_or_404(Post, pk=pk)
     query.delete()
    return redirect('post:list')

def PostUpdateView(request,pk):
    if not Post.objects.filter(user=request.user):
        raise Http404
    query=get_object_or_404(Post,pk=pk)
    form=PostForm(request.POST or None, request.FILES or None,instance=query)
    if form.is_valid():
        form.save()
        return redirect('post:list')
    return render(request,'update.html',{'form':form})









