from django.contrib import admin
from .models import Posts , Author , Comments
# Register your models here.


for model in [Posts,Author,Comments]:
    admin.site.register(model)