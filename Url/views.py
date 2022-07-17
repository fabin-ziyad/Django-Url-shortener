"""    <!--=====================================
       devopled by fabin ziyad
       github: https://github.com/fabin-ziyad
    ==========================================-->"""
from django.shortcuts import render,redirect
import uuid
from django.http import HttpResponse
from . models import Url
def index(request):
    return render(request,'home.html')
def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:8]
        new_url = Url(link=url, uuid = uid)
        new_url.save()
        return HttpResponse(uid)
def go(request, pk):
    url_details = Url.objects.get(uuid = pk)
    return redirect('' + url_details.link)