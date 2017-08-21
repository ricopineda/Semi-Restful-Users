from __future__ import unicode_literals
from models import *
from django.shortcuts import render
import random
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.contrib import messages
from django.utils.crypto import get_random_string
# the index function is called when root is visited
def index(request):
	# context = {
	# 	'id': User.objects.id()
	# 	'full_name': User.objects.all().full_name
	# 	'email': User.objects.all().email
	# 	'created_at': User.objects.all()created_at
	# }

	return render(request,'user_app/index.html', {'users': User.objects.all() })

def create(request):


	return render(request, 'user_app/new.html')

def add(request):

	User.objects.create(full_name=request.POST['full_name'], email=request.POST["email"])

	return redirect('/')

def show(request, id):

	return render(request, 'user_app/show.html', {'users': User.objects.get(id = id) })

def delete(request, id):

	a = User.objects.get(id = id)
	a.delete()
	messages.success(request, 'User Successfully Deleted.')

	return redirect('/')

def edit(request, id):

	return render (request, 'user_app/edit.html', {'users': User.objects.get(id = id) })

def update(request, id):
	a = User.objects.get(id = id)
	a.full_name = request.POST['full_name']
	a.email = request.POST['email']
	a.save()

	return redirect('/')




