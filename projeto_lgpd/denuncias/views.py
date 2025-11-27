from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .forms import LoginForm, DenunciaForm, CadastroForm, AcompanhamentoForm
from .models import Denuncia
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def denuncia_anonima(request):
    if request.method == 'POST':
        form = DenunciaForm(request.POST)
        if form.is_valid():
            denuncia = form.save(commit=False)
            denuncia.ip_address = get_client_ip(request)
            denuncia.user_agent = request.META.get('HTTP_USER_AGENT', '')
            denuncia.save()
            
            messages.success(request, 
                'Denúncia enviada com sucesso! Número do protocolo: #{}'.format(denuncia.id))
            return redirect('home')
    else:
        form = DenunciaForm()
    
    return render(request, 'denuncia_anonima.html', {'form': form})

@login_required
def dashboard(request):
    denuncias_usuario = Denuncia.objects.filter(denunciante=request.user)
    return render(request, 'dashboard.html', {
        'denuncias': denuncias_usuario,
        'total_denuncias': denuncias_usuario.count(),
        'denuncias_pendentes': denuncias_usuario.filter(status='pendente').count(),
    })

@login_required
def nova_denuncia_identificada(request):
    if request.method == 'POST':
        form = DenunciaForm(request.POST)
        if form.is_valid():
            denuncia = form.save(commit=False)
            denuncia.denunciante = request.user
            denuncia.ip_address = get_client_ip(request)
            denuncia.user_agent = request.META.get('HTTP_USER_AGENT', '')
            denuncia.save()
            
            messages.success(request, 
                'Denúncia enviada com sucesso! Número do protocolo: #{}'.format(denuncia.id))
            return redirect('dashboard')
    else:
        form = DenunciaForm()
    
    return render(request, 'nova_denuncia.html', {'form': form})

@login_required
def detalhes_denuncia(request, id):
    denuncia = get_object_or_404(Denuncia, id=id, denunciante=request.user)
    return render(request, 'detalhes_denuncia.html', {'denuncia': denuncia})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def cadastro_view(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()
            
            # Loga o usuário automaticamente após o cadastro
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            
            messages.success(request, f'Cadastro realizado com sucesso! Bem-vindo, {user.first_name}!')
            return redirect('dashboard')
    else:
        form = CadastroForm()
    
    return render(request, 'cadastro.html', {'form': form})

def denuncia_anonima(request):
    if request.method == 'POST':
        form = DenunciaForm(request.POST)
        if form.is_valid():
            denuncia = form.save(commit=False)
            denuncia.ip_address = get_client_ip(request)
            denuncia.user_agent = request.META.get('HTTP_USER_AGENT', '')
            denuncia.save()
            
            messages.success(request, 
                'Denúncia enviada com sucesso! Seu token de acompanhamento é: {}'.format(denuncia.token_acompanhamento))
            messages.info(request, 
                'Guarde este token para acompanhar o andamento da sua denúncia.')
            return redirect('acompanhamento')
    else:
        form = DenunciaForm()
    
    return render(request, 'denuncia_anonima.html', {'form': form})

def acompanhamento_denuncia(request):
    denuncia = None
    token = None
    
    if request.method == 'POST':
        form = AcompanhamentoForm(request.POST)
        if form.is_valid():
            token = form.cleaned_data['token']
            try:
                denuncia = Denuncia.objects.get(token_acompanhamento=token)
            except Denuncia.DoesNotExist:
                messages.error(request, 'Token inválido. Verifique o código e tente novamente.')
    else:
        form = AcompanhamentoForm()
        # Verificar se veio por GET com token
        token_get = request.GET.get('token')
        if token_get:
            try:
                denuncia = Denuncia.objects.get(token_acompanhamento=token_get)
                token = token_get
            except Denuncia.DoesNotExist:
                messages.error(request, 'Token inválido.')
    
    return render(request, 'acompanhamento.html', {
        'form': form,
        'denuncia': denuncia,
        'token': token
    })

def pagina_termos(request):
    return render(request, 'termos_lgpd.html')

def denuncia_anonima(request):
    if request.method == 'POST':
        form = DenunciaForm(request.POST)
        if form.is_valid():
            denuncia = form.save(commit=False)
            denuncia.ip_address = get_client_ip(request)
            denuncia.user_agent = request.META.get('HTTP_USER_AGENT', '')
            denuncia.save()
            
            messages.success(request, 
                'Denúncia enviada com sucesso! Seu token de acompanhamento é:')
            messages.info(request, 
                f'<strong>{denuncia.token_acompanhamento}</strong>')
            messages.warning(request, 
                'Guarde este token em local seguro para acompanhar o andamento da sua denúncia.')

            return redirect('acompanhamento') + f'?token={denuncia.token_acompanhamento}'
    else:
        form = DenunciaForm()
    
    return render(request, 'denuncia_anonima.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    messages.success(request, 'Você saiu do sistema com sucesso.')
    return redirect('home') 