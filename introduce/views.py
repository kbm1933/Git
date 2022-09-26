from django.shortcuts import render


def first_view(request):
    return render(request,'introduce.html')
# Create your views here.
