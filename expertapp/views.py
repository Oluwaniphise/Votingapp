from django.shortcuts import render
from django.http import JsonResponse

def home(request):

    # post = PoliticalPost.objects.all()
    context = {
        # 'post':post
        }
    return render(request, 'index.html', context)