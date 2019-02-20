from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Categorie(models.Model):
    name=models.CharField(max_length=200,verbose_name="Nom de la catégorie")
    icone=models.ImageField(upload_to='photo/',verbose_name="Icone")
    def __str__(self):
        return self.name

class Product(models.Model):
    categorie=models.ForeignKey(Categorie,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,verbose_name="Nom")
    short=models.CharField(max_length=200,verbose_name="Description courte",blank=True)
    long=models.TextField(verbose_name="Description longue")
    image=models.ImageField(upload_to='photo/',verbose_name="Image")
    price1=models.CharField(max_length=200,verbose_name="Prix du marché",blank=True)
    price=models.CharField(max_length=200,verbose_name="Prix réel")
    reduction=models.IntegerField(default=0,verbose_name="Réduction",blank=True)
    stock=models.IntegerField(default=0,verbose_name="Stock",blank=True)
    point=models.IntegerField(default=0,verbose_name="Point de classement",blank=True)
    mots=models.TextField(verbose_name="Mots clés de recherches",default="general")
    code=models.CharField(max_length=200,verbose_name="Code du vendeur",default="phénix")
    pourcentage=models.CharField(max_length=200,verbose_name="Pourcentage prélevé par Skerli",default=0)
    livraison=models.CharField(max_length=200,verbose_name="Prix de livraison",default=1000)

    
    def __str__(self):
        return self.name

class Photo(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_photo=models.ImageField(upload_to='photo/',verbose_name="Photos")

class Pub(models.Model):
    name=models.CharField(max_length=200,verbose_name="Nom de la pub")
    picture=models.ImageField(upload_to='photo/')
    def __str__(self):
        return self.name

class Img(models.Model):
    pub=models.ForeignKey(Pub,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='photo/')

class Order(models.Model):
    creation=models.DateTimeField('Date de commande',default=timezone.now)
    validation=models.BooleanField('Validation',default=True)
    contact=models.ForeignKey("Contact",on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
        return self.contact.name

class Contact(models.Model):
    prenom=models.CharField(max_length=200,verbose_name="Prénom")
    name=models.CharField(max_length=200,verbose_name="Nom")
    phone=models.CharField(max_length=200,verbose_name="Téléphone")
    adresse=models.CharField(max_length=500,verbose_name="Lieu de livraison/références")
    def __str__(self):
        return self.name
    
class BaseVendeur(models.Model):
    prenom=models.CharField(max_length=200,verbose_name="Prénom")
    nom=models.CharField(max_length=200,verbose_name="Nom")
    numero=models.CharField(max_length=200,verbose_name="Numéro")
    produit=models.TextField(verbose_name="Ses produits vendus sur skerli et leur prix",blank=True)
    code=models.CharField(max_length=200,verbose_name="Code du vendeur")
    vente=models.IntegerField(default=0,verbose_name="Nombre de ventes")
    product=models.ForeignKey(Product,on_delete=models.CASCADE,default=0)
    def __str__(self):
        return self.prenom

class BaseClient(models.Model):
    prenom=models.CharField(max_length=200,verbose_name="Prénom")
    nom=models.CharField(max_length=200,verbose_name="Nom")
    numero=models.CharField(max_length=200,verbose_name="Numéro")
    adresse=models.TextField(verbose_name="Adresse")
    produit=models.TextField(verbose_name="Nom du ou des produits achetés et leur prix",default=0)
    achat=models.IntegerField(default=0,verbose_name="Nombre d'achats")
    def __str__(self):
        return self.prenom
   
class Coursier(models.Model):
    prenom=models.CharField(max_length=200,verbose_name="Prénom")
    nom=models.CharField(max_length=200,verbose_name="Nom")
    numero=models.CharField(max_length=200,verbose_name="Numéro")
    jour=models.TextField(verbose_name="Jours et heures de livraison")
    code=models.CharField(max_length=200,verbose_name="Code de livraison du coursier",default="bravo")
    def __str__(self):
        return self.prenom   
    
    
