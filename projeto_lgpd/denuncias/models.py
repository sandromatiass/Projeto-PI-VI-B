import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Denuncia(models.Model):
    TIPO_DENUNCIA_CHOICES = [
        ('vazamento', 'Vazamento de Dados'),
        ('uso_indevido', 'Uso Indevido de Dados'),
        ('acesso_nao_autorizado', 'Acesso Não Autorizado'),
        ('coleta_excessiva', 'Coleta Excessiva de Dados'),
        ('outros', 'Outros'),
    ]
    
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_analise', 'Em Análise'),
        ('resolvida', 'Resolvida'),
        ('arquivada', 'Arquivada'),
    ]
    
    # Informações da denúncia
    titulo = models.CharField(max_length=200, verbose_name='Título da Denúncia')
    descricao = models.TextField(verbose_name='Descrição Detalhada')
    tipo = models.CharField(max_length=50, choices=TIPO_DENUNCIA_CHOICES, verbose_name='Tipo de Violação')
    data_ocorrencia = models.DateField(verbose_name='Data da Ocorrência')
    data_criacao = models.DateTimeField(default=timezone.now)
    
    # Informações do denunciante (opcionais para anonimato)
    denunciante = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        verbose_name='Denunciante'
    )
    
    # Contato opcional
    email_contato = models.EmailField(blank=True, null=True, verbose_name='E-mail para Contato')
    telefone_contato = models.CharField(max_length=20, blank=True, null=True, verbose_name='Telefone para Contato')
    
    # Status e acompanhamento
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    observacoes_internas = models.TextField(blank=True, verbose_name='Observações Internas')
    
    # Token para acompanhamento de denúncias anônimas
    token_acompanhamento = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    
    # Metadados para LGPD
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.titulo} - {self.get_status_display()}"
    
    def is_anonima(self):
        return self.denunciante is None
    
    class Meta:
        verbose_name = 'Denúncia'
        verbose_name_plural = 'Denúncias'
        ordering = ['-data_criacao']