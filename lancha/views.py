from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from .forms import StudentForm
from .models import Student


class Base(View):
    template = 'base.html'

    def get(self, request):
        return render(request, self.template)


class Login(View):
    template = 'login.html'

    def get(self, request):
        return render(request, self.template)


class Cadastro(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template)


class Tabela(View):
    template = 'tabela.html'

    def get(self, request):
        return render(request, self.template)


class Graficos(View):
    template = 'graficos.html'

    def get(self, request):
        return render(request, self.template)


class StudentCreate(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'index.html'
