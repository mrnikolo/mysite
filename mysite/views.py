import mimetypes
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# def HomeView(request):
#     return render (request , 'home.html')
class home(TemplateView):
    template_name = 'home.html'


def download(request):
    file = open('mysite/resource/Programing-Resume-09358508586.jpg', 'rb') #Open the specified file
    response = HttpResponse(file)   #Give file handle to HttpResponse object
    response['Content-Type'] = 'application/octet-stream' #Set the header to tell the browser that this is a file
    response['Content-Disposition'] = 'attachment;filename="Programing-Resume-09358508586.jpg"' #This is a simple description of the file. Note that the writing is the fixed one
    return response 