from datetime import timedelta

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.utils import timezone
from .forms import PostForm
from .models import Post

@login_required
def index(request):
    timesince = timezone.now() - timedelta(days=3)
    post_list = Post.objects.all()\
        .filter(
            Q(author=request.user) |
            Q(author__in=request.user.following_set.all())
            ).\
                filter(
                    created_at__gte = timesince
                )
        
    suggested_user_list = get_user_model().objects.all()\
        .exclude(pk=request.user.pk)\
        .exclude(pk__in=request.user.following_set.all())[:4]
    
    return render(request, "instagram/index.html", {
        "suggested_user_list" : suggested_user_list,     
        "post_list" : post_list,   
    })

@login_required
def post_new(request):
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()# many to many 는 pk 가 있어야하기 때문에, 먼저 선 저장이 필요하다. 
            post.tag_set.add(*post.extract_tag_list())
            # TODO 
            messages.success(request, "포스팅을 저장했습니다.")
            return redirect(post)
            #return redirect(post) # TODO : get_absolute_url 활용 
    else:
        form = PostForm()
    
    return render(request, "instagram/post_form.html", {
        "form": form,
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "instagram/post_detail.html", {
        "post": post,        
    })
    
@login_required
def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # TODO : like 처리 필요
    messages.success(request, f"{post}를 좋아합니다.")
    redirect_url = request.META.get("HTTP_REFEER", "root")
    return redirect(redirect_url)        

@login_required
def post_unlike(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # TODO : like 처리 필요
    messages.success(request, f"{post}를 좋아요를 취소합니다.")
    redirect_url = request.META.get("HTTP_REFEER", "root")
    return redirect(redirect_url)        

def user_page(request, username):
    page_user = get_object_or_404(get_user_model(), username=username, is_active=True)    
    post_list = Post.objects.filter(author=page_user)
    post_list_count = post_list.count() # 실제 디비에 count query 사용. len(post_list) 가 오히려 느림 
    
        #request.user # login  되어 있으면, User 객체 or AnonymousUser
    if request.user.is_authenticated:
        is_follow = request.user.following_set.filter(pk=page_user.pk).exists() 
    else:
        is_follow = False   

    return render(request, "instagram/user_page.html",{
        "page_user" : page_user,        
        "post_list" : post_list,
        "post_list_count" : post_list_count,
        "is_follow" : is_follow,
    })
