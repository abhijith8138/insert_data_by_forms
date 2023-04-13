from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
from app.models import *
from django.db.models.functions import  *

def insert_topic(request):
    if request.method =='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('Topic insertion is successfull')
    

    return render(request,'insert_topic.html')
def insert_webpage(request):
    return render(request,'insert_webpage.html')
