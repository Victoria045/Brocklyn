from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect, JsonResponse


def index(request):

  return render(request, 'brocklyn/index.html',)  