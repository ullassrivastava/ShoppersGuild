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

    url(r'^Seed_Pack_Home/PackageA/', views.openAboutUs, name='index'),

    url(r'^AboutUs/', views.openAboutUs, name='index'),

    url(r'^AHomeSeeds/', views.openHomeSeedABuy, name='index'),
    url(r'^BHomeSeeds/', views.openHomeSeedBBuy, name='index'),
    url(r'^CHomeSeeds/', views.openHomeSeedCBuy, name='index'),

    url(r'^AGardenSeeds/', views.openGardenSeedABuy, name='index'),
    url(r'^BGardenSeeds/', views.openGardenSeedBBuy, name='index'),
    url(r'^CGardenSeeds/', views.openGardenSeedCBuy, name='index'),

    url(r'^APot/', views.openPotABuy, name='index'),
    url(r'^BPot/', views.openPotBBuy, name='index'),
    url(r'^CPot/', views.openPotCBuy, name='index'),

    url(r'^Checkout/', views.openCheckout, name='index')
]
