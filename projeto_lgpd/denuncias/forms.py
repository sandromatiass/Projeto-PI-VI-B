from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Denuncia

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nome de usuário'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Senha'
        })
    )

class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = [
            'titulo', 'descricao', 'tipo', 'data_ocorrencia',
            'email_contato', 'telefone_contato'
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Vazamento de dados de clientes'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descreva detalhadamente a violação...',
                'rows': 6
            }),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'data_ocorrencia': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'email_contato': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'seu@email.com (opcional)'
            }),
            'telefone_contato': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(11) 99999-9999 (opcional)'
            }),
        }
        labels = {
            'titulo': 'Título da Denúncia',
            'descricao': 'Descrição Detalhada',
            'tipo': 'Tipo de Violação',
            'data_ocorrencia': 'Data da Ocorrência',
            'email_contato': 'E-mail para Contato (Opcional)',
            'telefone_contato': 'Telefone para Contato (Opcional)',
        }
        
class CadastroForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'seu@email.com'
        })
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Seu nome'
        })
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Seu sobrenome'
        })
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome de usuário'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Senha'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirme sua senha'
        })

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este e-mail já está em uso.')
        return email
    
class AcompanhamentoForm(forms.Form):
    token = forms.CharField(
        max_length=36,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Cole aqui o token recebido'
        }),
        label='Token de Acompanhamento'
    )