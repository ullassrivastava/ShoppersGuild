from django.conf.urls import url
from django.contrib import admin
from Browser import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls)
    url(r'^$', views.openSignIn, name='index'),
    url(r'^SignUp/', views.openSignUp, name='index'),
    url(r'^SignIn/', views.openSignIn, name='index')
]
