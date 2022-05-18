<<<<<<< Updated upstream
"""frete_express URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
=======
>>>>>>> Stashed changes
from django.contrib import admin
from django.urls import path
from lancha import views
from lancha.forms import ClientesForm, FreteForm, ProdutoForm, FormStepTwo, FormStepOne
from lancha.views import FormWizardView, FORMS, ClientesList
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< Updated upstream
    path('', views.Index.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login')
=======
    path('', views.Base.as_view(), name='base'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.SignUpView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    #path('index/', views.ClientesCreate.as_view(), name='index'),
    #path('tabela/', views.Tabela.as_view(), name='tabela'),
    path('graficos/', views.Graficos.as_view(), name='graficos'),
    path('order/', views.order),
    path('form/', FormWizardView.as_view(FORMS)),
    path('tabela/', ClientesList.as_view(), name='tabela')
>>>>>>> Stashed changes

]
