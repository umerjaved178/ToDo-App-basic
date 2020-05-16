from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def index(request):
	list=Taskfield.objects.all()
	form =ArticleForm()

	if request.method=='POST':
		form=ArticleForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect("/")


	context={"list":list,"form":form}
	return render(request,"tasks/index.html",context)

def delete(request,pk):
	list=Taskfield.objects.get(id=pk)

	if request.method=='POST':
		list.delete()
		return redirect("/")
	context={"list":list}
	return render(request,'tasks/delete.html',context)

def edit(request,pk):
	list=Taskfield.objects.get(id=pk)
	form =ArticleForm(instance=list)

	if request.method=='POST':
		form=ArticleForm(request.POST,instance=list)
		if form.is_valid():
			form.save()
		return redirect("/")


	context={"list":list,"form":form}
	return render(request,"tasks/update.html",context)