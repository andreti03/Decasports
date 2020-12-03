"""DECASPORTS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from . import views
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from customers.views import formulario
from products.views import updateItem
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from categories.views import Home, Futbol, Basketball, Ping, Natacion, Boxeo, Taekwondo, Atletismo, Ciclismo


urlpatterns = [
    path('', views.Home, name ='Home'),
    path('login/', views.Sign_in, name ='Sign_in'),
    path('cr_acc/', views.registerPage, name ='Sign_up'),
    path('sign_out/', views.Sign_out, name ='Sign_out'),
    path('update_item/', updateItem, name ='Update_Item'),
    path('admin/', admin.site.urls),
    path('address/', include(('address.urls','address'))),
    path('bill/', include(('bill.urls','bill'))),
    path('categories/', include(('categories.urls','categories'))),
    path('customers/', include(('customers.urls','customers'))),
    path('shopping_cart/', include(('shopping_cart.urls','shopping_cart'))),
    path('products/', include(('products.urls','products'))),
    path('products/Futbol/', Futbol, name = 'Futbol'),
    path('products/Basketball/', Basketball, name = 'Basketball'),
    path('products/Ping-Pong/', Ping, name = 'Ping'),
    path('products/Natación/', Natacion, name = 'Natacion'),
    path('products/Boxeo/', Boxeo, name = 'Boxeo'),
    path('products/Taekwondo/', Taekwondo, name = 'Taekwondo'),
    path('products/Atletismo/', Atletismo, name = 'Atletismo'),
    path('products/Ciclismo/', Ciclismo, name = 'Ciclismo'),
    path('customer/actualizar_datos/', formulario, name='encuesta')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)