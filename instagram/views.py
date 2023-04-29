
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PostForm

@login_required
def post_new(request):
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, "포스팅을 저장했습니다.")
            return redirect(post) # TODO : get_absolute_url 활용 
    else:
        form = PostForm()
    
    return render(request, "instagram/post_form.html", {
        "form": form,
    })