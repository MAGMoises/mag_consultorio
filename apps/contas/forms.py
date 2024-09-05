from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from contas.models import MyUser 

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Senha", 
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="Sua senha deve ter pelo menos 8 caracteres."
    )
    password2 = forms.CharField(
        label="Confirmação de Senha", 
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="Repita a senha para confirmação."
    )

    class Meta:
        model = MyUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')
        labels = {
            'email': 'E-mail', 
            'first_name': 'Nome', 
            'last_name': 'Sobrenome', 
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            css_class = 'form-check-input' if isinstance(field.widget, forms.CheckboxInput) else 'form-control'
            field.widget.attrs['class'] = css_class
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("As senhas não correspondem!")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
