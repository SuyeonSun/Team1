"""perfectrip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from cautionboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('detail',views.detail, name="detail"),
    path('detail/<str:place>/', views.getplacedetails, name="detail_detail"),
    path('detail/<str:place>/addcaution/', views.addcaution, name="addcaution"),
    path('detail/<str:place>/<str:id>/yesUp/',views.yesUp,name="yesUp"),
    path('detail/<str:place>/<str:id>/noUp/',views.noUp,name="noUp"),
]
