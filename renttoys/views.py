from django.http import HttpResponse
from django.template import loader

from .models import Toy

def index(request):
    template=loader.get_template('renttoys\index.html')
    toys=Toy.objects.all
    context={'toys':toys}
    return HttpResponse(template.render(context,request))
    
def howtofindus(request):
    template=loader.get_template('renttoys\howtofindus.html')
    toys=Toy.objects.all
    context={'toys':toys}
    return HttpResponse(template.render(context,request))
