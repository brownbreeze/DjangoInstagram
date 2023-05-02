
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Tag

@login_required
def post_new(request):
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            for tag_name in post.extract_tag_list():
                tag, _= Tag.objects.get_or_create(name=tag_name)
            # TODO 
            post.save()
            
            messages.success(request, "포스팅을 저장했습니다.")
            return redirect('/')
            #return redirect(post) # TODO : get_absolute_url 활용 
    else:
        form = PostForm()
    
    return render(request, "instagram/post_form.html", {
        "form": form,
    })