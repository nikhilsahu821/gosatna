
from django.shortcuts import render




def home_page(request):
    context = {
        "title" : "Hello World!",
        "content" : "welcome to the homepage",
    }
    
    return render(request, "index.html", context )
