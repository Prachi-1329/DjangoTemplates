from django.shortcuts import render
from .models import themes
# Create your views here.
def index(request):
 theme= themes.objects.all()
 return render(request, "index.html", {'theme':theme})
