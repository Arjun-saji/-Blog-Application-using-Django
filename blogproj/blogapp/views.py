from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
	blogs=Blog.objects.all()
	recent=Blog.objects.latest('created_date')
	recent_blogs = Blog.objects.exclude(pk=recent.pk).order_by('created_date')[:4]
	context={"blogs":blogs,"recent":recent,"recent_blogs":recent_blogs}
	return render(request,"index.html",context)

def single(request,object_id):
	blogs=Blog.objects.get(pk=object_id)
	all_blogs=Blog.objects.exclude(pk=object_id)
	context={"blogs":blogs,"all_blogs":all_blogs}
	return render(request,"single.html",context)



def allblogs(request):
	blogs=Blog.objects.all()
	context={"blogs":blogs}
	return render(request,"allblog.html",context)

def contact(request):
	return render(request,"contact.html")




