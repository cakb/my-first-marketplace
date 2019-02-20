from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages
from.models import *
from.forms import *
# Create your views here.

def accueil(request):
    pub=Pub.objects.order_by('-id')
    product=Product.objects.order_by('-point')
    categorie=Categorie.objects.all()
    return render(request,'store/accueil.html',{'pub':pub,'product':product,'categorie':categorie})

def detail(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    carousel=Photo.objects.filter(product__pk=product.id)
    return render(request,'store/detail.html',{'product':product,'carousel':carousel})

def display(request):
    categorie=Categorie.objects.all().order_by('-name')
    return render(request,'store/display.html',{'categorie':categorie})

def categorie(request,categorie_id):
    categorie=get_object_or_404(Categorie,pk=categorie_id)
    product=Product.objects.filter(categorie__pk=categorie.id)
    return render(request, 'store/categorie.html',{'categorie':categorie,'product':product})

def commande(request,product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product_name': product.name,
        'product_id': product.id,
        'image': product.image,
    }
    if request.method == 'POST':
        form = ContactForm(request.POST, error_class=ParagraphErrorList)
        if form.is_valid():
            prenom = form.cleaned_data['prenom']
            name = form.cleaned_data['name']
            phone=form.cleaned_data['phone']
            adresse=form.cleaned_data['adresse']
            try:
                    contact = Contact.objects.filter(prenom=prenom, name=name,phone=phone,
                        adresse=adresse)
                    if not contact.exists():
                        contact = Contact.objects.create(
                            prenom=prenom,
                            name=name,
                            phone=phone,
                            adresse=adresse
                        )
                    else:
                        contact = contact.first()

                    product = get_object_or_404(Product, id=product_id)
                    order = Order.objects.create(
                        contact=contact,
                        product=product
                    )
                    product.save()
                    return render(request,"store/merci.html",context)
            except:
                form.errors['internal'] = "Une erreur interne est apparue. Merci de recommencer votre requête."

    else:
        form = ContactForm()
    context['form'] = form
    context['errors'] = form.errors.items()
    return render(request, 'store/commande.html', context)

def search(request):
    query = request.GET.get('query')
    if not query:
        product = Product.objects.all()
    else:
        product = Product.objects.filter(long__icontains=query).order_by('-point')
    if not product.exists():
        product = Product.objects.filter(mots__icontains=query).order_by('-point')
        
    name = "Résultats pour la requête %s"%query
    context = {
        'product': product,
        'name': name
    }
    return render(request, 'store/search.html', context)
                   


def about(request):
    return render(request,'store/about.html',{})
def confidentialite(request):
    return render(request,'store/confidentialite.html',{})
def merci(request):
    return render(request,'store/merci.html',{})


