from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            long_url = request.POST['long_url']
            uid = str(uuid.uuid4())[:5]
            user = request.user
            new_url = Url(long_url=long_url, token=uid, user=user)
            new_url.save()
            return HttpResponse(uid)
        else:
            long_url = request.POST['long_url']
            uid = str(uuid.uuid4())[:5]
            new_url = Url(long_url=long_url, token=uid)
            new_url.save()
            return HttpResponse(uid)

def go(request, pk):
    data = Url.objects.get(token=pk)
    return redirect(data.long_url)