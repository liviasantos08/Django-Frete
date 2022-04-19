
from django.contrib import admin
from django.urls import path
from lancha import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Base.as_view(), name='base'),
    path('login/', views.Login.as_view(), name='login'),
    path('index/', views.Cadastro.as_view(), name='index'),

]


