from  django.http  import   HttpResponse
from django.shortcuts import render, redirect

def  main(request):
    return  render(request, "main.html")

def  top(request):
    return  render(request, "top.html")

def  bottom(request):
    return  render(request, "bottom.html")

