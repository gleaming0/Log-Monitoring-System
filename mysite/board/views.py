from django.shortcuts import render
# from .models import SystemEvents

# Create your views here.

def index(request):
    boards = [i for i in range(1, 10)]

    context = {"boards":boards}
    return render(request, "board/index.html", context)