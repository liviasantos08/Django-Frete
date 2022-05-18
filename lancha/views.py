from django.views import View
<<<<<<< Updated upstream


class Index(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template)

class Login(View):
    template = 'login.html'

    def get(self, request):
        return render(request, self.template)
=======
from django.views.generic import CreateView, UpdateView, ListView
from django.http.response import HttpResponseRedirect
from django.forms.models import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin

import lancha.forms
from .forms import ClientesForm, OrderForms, ItemOrderForms, SignUpForm, ProfileForm, FreteForm
from .models import Clientes, Order, ItemOrder, Frete
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from formtools.wizard.views import SessionWizardView


class Base(LoginRequiredMixin, View):
    template = 'base.html'
    login_url = '/login/'

    def get(self, request):
        return render(request, self.template)


class Cadastro(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template)


"""class Tabela(View):
    template = 'tabela.html'

    def get(self, request):
        return render(request, self.template)
"""

class Graficos(View):
    template = 'graficos.html'

    def get(self, request):
        return render(request, self.template)


"""class ClientesCreate(CreateView):
    model = Clientes
    form_class = ClientesForm
    template_name = 'index.html'
"""


def order(request):
    order_forms = Order()
    item_order_formset = inlineformset_factory(Order, ItemOrder, form=ItemOrderForms, extra=1, can_delete=False,
                                               min_num=1, validate_min=True)

    if request.method == 'POST':
        forms = OrderForms(request.POST, request.FILES, instance=order_forms, prefix='main')
        formset = item_order_formset(request.POST, request.FILES, instance=order_forms, prefix='product')

        if forms.is_valid() and formset.is_valid():
            forms = forms.save(commit=False)
            forms.save()
            formset.save()
            return HttpResponseRedirect('order/')

    else:
        forms = OrderForms(instance=order_forms, prefix='main')
        formset = item_order_formset(instance=order_forms, prefix='product')

    context = {
        'forms': forms,
        'formset': formset,
    }

    return render(request, 'order.html', context)


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('login')
    template_name = 'profile.html'


FORMS = [
    ("Clientes", lancha.forms.ClientesForm),
    ("Frete", lancha.forms.FreteForm)
]

TEMPLATES = {"Clientes": "clientes.html", "Frete": "frete.html"}


class FormWizardView(SessionWizardView):
    instance = None
    template_name = "step.html"
    form_list = [ClientesForm, FreteForm]

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def process_step(self, form):
        return self.get_form_step_data(form)

    def done(self, form_list, **kwargs):
        for form in form_list:
            form.save()

        return render(self.request, 'tabela.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })


class ClientesList(ListView):
    model = Clientes
    template_name = "tabela.html"


class FreteList(ListView):
    model = Frete
    template_name = "#"
>>>>>>> Stashed changes
