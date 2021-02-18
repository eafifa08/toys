from django.contrib import admin

from .models import Toy
from .models import Category

admin.site.register(Toy)
admin.site.register(Category)

# Register your models here.
