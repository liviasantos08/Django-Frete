from django.shortcuts import render
from django.views import View


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