from django.contrib import admin
from.models import *

# Register your models here.

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 5


class ProductAdmin(admin.ModelAdmin):
    list_display=("categorie","name","short","long","image","price1","price","reduction","stock","point","mots","code","pourcentage","livraison")
    list_filter=("categorie","name","short","long","image","price1","price","reduction","stock","point","mots","code","pourcentage","livraison")
    ordering=("point",)
    search_fields=("name","short","long","image","price1","price","reduction","stock","point","mots","code","pourcentage","livraison")
    inlines = [
        PhotoInline
    ]

class OrderInline(admin.TabularInline):
   model=Order
   readonly_fields=["creation","validation","contact","product"]
class ContactAdmin(admin.ModelAdmin):
    list_display=("prenom","name","phone","adresse")
    list_filter=("prenom","name","phone","adresse")
    search_fields=("prenom","name","phone","adresse")
    inlines= [
        OrderInline
        ]

class ImgInline(admin.TabularInline):
    model = Img
    extra=10

class PubAdmin(admin.ModelAdmin):
    list_display=("name","picture")
    list_filter=("name","picture")
    ordering=("name",)
    search_fields=("name","picture")
    inlines = [
        ImgInline

        ]
class CategorieAdmin(admin.ModelAdmin):
    list_display=('name','icone')
    list_filter=('name','icone')
    ordering=('name',)
    search_fields=('name','icone')

class OrderAdmin(admin.ModelAdmin):
    list_display=("creation","validation","contact","product")
    list_filter=("creation","validation","contact","product")
    search_fields=("creation","validation","contact","product")

class BaseVendeurAdmin(admin.ModelAdmin):
    list_display=("prenom","nom","numero","produit","code","vente","product")
    list_filter=("prenom","nom","numero","produit","code","vente","product")
    ordering=("vente",)
    search_fields=("prenom","nom","numero","produit","code","vente","product")
class BaseClientAdmin(admin.ModelAdmin):
    list_display=("prenom","nom","numero","adresse","produit","achat")
    list_filter=("prenom","nom","numero","adresse","produit","achat")
    ordering=("achat",)
    search_fields=("prenom","nom","numero","adresse","produit","achat")
class CoursierAdmin(admin.ModelAdmin):
    list_display=("prenom","nom","numero","jour","code")
    list_filter=("prenom","nom","numero","jour","code")
    ordering=("prenom",)
    search_fields=("prenom","nom","numero","jour","code")

    
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Categorie,CategorieAdmin)
admin.site.register(Pub,PubAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(BaseVendeur,BaseVendeurAdmin)
admin.site.register(BaseClient,BaseClientAdmin)
admin.site.register(Coursier,CoursierAdmin)




