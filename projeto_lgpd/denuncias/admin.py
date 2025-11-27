from django.contrib import admin
from .models import Denuncia

@admin.register(Denuncia)
class DenunciaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo', 'status', 'data_criacao', 'denunciante']
    list_filter = ['tipo', 'status', 'data_criacao']
    search_fields = ['titulo', 'descricao', 'email_contato']
    readonly_fields = ['data_criacao', 'ip_address']
    
    fieldsets = (
        ('Informações da Denúncia', {
            'fields': ('titulo', 'descricao', 'tipo', 'data_ocorrencia')
        }),
        ('Informações do Denunciante', {
            'fields': ('denunciante', 'email_contato', 'telefone_contato')
        }),
        ('Acompanhamento', {
            'fields': ('status', 'observacoes_internas')
        }),
        ('Metadados', {
            'fields': ('data_criacao', 'ip_address', 'user_agent'),
            'classes': ('collapse',)
        }),
    )