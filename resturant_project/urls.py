"""
URL configuration for resturant_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from django.conf import settings 
# from django.conf.urls.static import static
# from base_app.views import * 



# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path(" ",HomeView),
#     path("/book_table", BookTableView),
#     path("/menu", MenuView),
#     path("/about",AboutView),
# ]

# if settings.DEBUG:
#     urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATICS_ROOT)  
    
#     urlpatterns +=  staic(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

    
    
from django.urls import path
from base_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('contact/', views.contact, name='contact'),
    path('reservations/', views.reservations, name='reservations'),
    path('reviews/', views.reviews, name='reviews'),
    path('about/', views.about, name='about'),
]
