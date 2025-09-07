from django.contrib import admin
from  .models import Author , Posts , Comments


for model in [Posts,Author ,Comments]:
    admin.site.register(model)
# Register your models here.
