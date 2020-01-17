
from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})

#render 메서드 호출. blog/post_list 템플릿 보여줌.
