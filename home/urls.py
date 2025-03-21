from django.contrib import admin
from django.urls import path
from home import views

urlpatterns=[
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("Spofty", views.Spofty, name='Spofty'),
    path("Ice_Cream", views.Ice_Cream, name='Ice_Cream'),
    path("Family_Pack", views.Family_Pack, name='Family_Pack'),
    # path("submitcontact",views.contact,name='contact'),
    path("home", views.home, name='home'),
]