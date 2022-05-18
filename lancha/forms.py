from django.forms import inlineformset_factory
from lancha.models import Clientes, Order, ItemOrder, Frete, Produto
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.forms.widgets import NumberInput

gol = [('blue', 'BLUE'), ('green', 'GREEN'), ('black', 'BLACK')]


class ClientesForm(forms.ModelForm):
    color = forms.ChoiceField(widget=forms.RadioSelect, choices=gol)

    class Meta:
        model = Clientes
        fields = '__all__'


class FreteForm(forms.ModelForm):
    data_entrega = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    class Meta:
        model = Frete
        fields = '__all__'


familyFormSet = inlineformset_factory(Frete, Produto, form=FreteForm, extra=1)


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'


class OrderForms(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['date']


class ItemOrderForms(forms.ModelForm):
    class Meta:
        model = ItemOrder
        exclude = ['order']


favorite = [('blue', 'BLUE'), ('green', 'GREEN'), ('black', 'BLACK')]


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    color = forms.ChoiceField(widget=forms.RadioSelect, choices=favorite)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]


class FormStepOne(forms.Form):
    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    email = forms.EmailField()
    data = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    hora = forms.TimeField(widget=NumberInput(attrs={'type': 'time'}))
    color = forms.ChoiceField(widget=forms.RadioSelect, choices=favorite)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'name',
                'last name'
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )


class FormStepTwo(forms.Form):
    job = forms.CharField(max_length=100)
    salary = forms.CharField(max_length=100)
    job_description = forms.CharField(widget=forms.Textarea)
