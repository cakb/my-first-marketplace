from django.urls import path
from.import views


app_name='store'
urlpatterns=[
    path("accueil/",views.accueil,name="accueil"),
    path('detail/<product_id>',views.detail,name="detail"),
    path('display/',views.display,name="display"),
    path('categorie/<categorie_id>',views.categorie,name="categorie"),
    path("commande/<product_id>",views.commande,name='commande'),
    path("search/",views.search,name='search'),
    path("about/",views.about,name='about'),
    path("confidentialite/",views.confidentialite,name='confidentialite'),
    path("merci/",views.merci,name='merci'),
    ]
