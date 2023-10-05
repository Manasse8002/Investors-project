from rest_framework import cookies
from rest_framework import views

class ApplicationController(views.APIView, cookies.CookiesMixin):
    pass
