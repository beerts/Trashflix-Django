from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

class FormHomepage(forms.Form):
    email = forms.EmailField(label=False)

class CriarContaForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Este e-mail já está cadastrado em outra conta! Por favor, utilize outro endereço de e-mail.")
        return email
