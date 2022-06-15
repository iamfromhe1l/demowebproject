
from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path('', views.main, name='home'),
    path('home/', views.main, name='home'),
    path('electr/', views.electr, name='electr'),
    path('pol/', views.pol, name='pol'),
    path('others/', views.others, name='other'),
    path('cart/', views.cart, name='cart'),
    path('admin/', admin.site.urls),
]
