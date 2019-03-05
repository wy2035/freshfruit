#from django.http import HttpResponse
from django.shortcuts import render_to_response
#from django.shortcuts import get_object_or_404,render
def index(request):
    render_to_response("home_page.html")