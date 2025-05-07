from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def home(request):
#     return HttpResponse("""<h2>Hi, im a django server.</h2>
#                         <h2>this is coming from django server</h2>
#                         <hr>
#                         <h3>Hope you guy's enjoying it :)
#                         """)

peoples = [
    {"name": "Alex", "age": 29},
    {"name": "Sophia", "age": 9},
    {"name": "Nick", "age": 41},
    {"name": "Diana", "age": 15}
]
def home(request):
    return render(request, "index.html", context= {'peoples': peoples})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def success_page(request):
    return HttpResponse("<h2>Hey! This is a success page</h2>")