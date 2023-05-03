
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
# from .models import Tag

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