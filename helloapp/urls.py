
from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path('', views.main, name='home'),
    path('home/', views.main, name='home'),
    path('electr/', views.electr, name='electr'),
    path('pol/', views.pol, name='pol'),
    path('others/', views.others, name='other'),
    path('admin/', admin.site.urls),
    path('save/',views.save,name='save'),
    path('s_data/<int:a>/<int:b>/<int:c>/<int:d>/<int:e>/<int:f>/<int:g>/<int:h>/<int:i>/<int:j>',views.s_data),
    path('e_data/<int:a>/<int:b>/<int:c>/<int:d>/<int:e>/<int:f>',views.e_data),
    path('p_data/<int:a>/<int:b>/<int:c>/<int:d>/<int:e>',views.p_data),
    path('o_data/<int:a>/<int:b>/<int:c>/<int:d>',views.o_data),
]
