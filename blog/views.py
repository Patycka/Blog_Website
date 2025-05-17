from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main_page(request):
    return render(request, 'blog/index.html')

def posts(request):
    return render(request, 'blog/all-posts.html')

def show_post(request, slug):
    return HttpResponse("First post")