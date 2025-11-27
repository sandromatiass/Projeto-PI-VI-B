from django.contrib import admin
from django.urls import path
from denuncias import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('denuncia-anonima/', views.denuncia_anonima, name='denuncia_anonima'),
    path('acompanhamento/', views.acompanhamento_denuncia, name='acompanhamento'),
    path('termos-lgpd/', views.pagina_termos, name='termos_lgpd'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('nova-denuncia/', views.nova_denuncia_identificada, name='nova_denuncia'),
    path('denuncia/<int:id>/', views.detalhes_denuncia, name='detalhes_denuncia'),
]