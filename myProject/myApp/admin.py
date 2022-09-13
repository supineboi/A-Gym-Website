from django.contrib import admin
from .models import Client, Employee
from tinymce.widgets import TinyMCE
from django.db import models


# Customize Order
class Customizer(admin.ModelAdmin):
  # fields = ['empName','empAge','empAddress','empJoinDate']

# Divide in Fields
  fieldsets = [ ("Name and Age",{"fields" :["empName","empAge"]}),("Address andJoinDate",{"fields":["empAddress","empJoinDate"]}) ]

  formfield_overrides = { models.TextField : {'widget' : TinyMCE()}  }
  
# Register your models here.
admin.site.register(Employee,Customizer)

admin.site.register(Client)
