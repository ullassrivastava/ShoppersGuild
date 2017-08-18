from django.conf.urls import url
from django.contrib import admin
from Browser import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls)
    url(r'^$', views.openSignIn, name='index'),
    url(r'^SignUp/', views.openSignUp, name='index'),
    url(r'^SignIn/', views.openSignIn, name='index'),
    url(r'^Home/', views.openHome, name='index'),
    url(r'^Seed_Pack_Home/', views.openSeedPackHome, name='index'),
    url(r'^Seed_Pack_Garden/', views.openSeedPackGarden, name='index'),
    url(r'^Pots/', views.openPots, name='index'),
    url(r'^AboutUs/', views.openAboutUs, name='index'),
    url(r'^Checkout/', views.openCheckout, name='index')
]
