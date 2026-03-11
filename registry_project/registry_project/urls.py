from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("A2A Agent Marketplace Registry Running")

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("api/agents/", include("agents_registry.urls")),
]
