from django.shortcuts import render
from django.http import HttpResponse
# Create your views here
"""In Django, a "views.py" file typically contains Python code that defines the logic for handling HTTP requests and generating HTTP responses. Specifically, views.py contains functions or classes called "views" that correspond to different URLs or URL patterns defined in a Django project's "urls.py" file.

When a user makes an HTTP request to a specific URL that matches a URL pattern defined in urls.py, Django's URL dispatcher determines which view function or class should be called to handle the request. The view function or class processes the request and generates an HTTP response, which is returned to the user's browser.

Views in Django can perform a variety of tasks, such as fetching data from a database, rendering HTML templates, processing form submissions, and returning JSON or other data formats. They are a central component of the Model-View-Controller (MVC) architectural pattern that Django follows."""
def say_hello(request):
    return HttpResponse("Hello")