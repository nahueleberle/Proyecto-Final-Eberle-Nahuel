from django.contrib import admin
from core.models import *
from core.views import *
# Register your models here.

admin.site.register(Avatar)

from django import forms

class ProductoAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'imagen':
            formfield.widget = forms.FileInput(attrs={'accept': 'image/*'})
        return formfield

admin.site.register(Producto, ProductoAdmin)