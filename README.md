# Sistema de Denúncias LGPD

## 📋 Descrição do Projeto

Sistema web desenvolvido em Django para recebimento e gerenciamento de denúncias de violações da Lei Geral de Proteção de Dados (LGPD). Permite que usuários realizem denúncias de forma anônima ou identificada, com total conformidade aos princípios da legislação brasileira de proteção de dados.

## 🎯 Objetivo

Fornecer uma plataforma segura e acessível para que cidadãos possam reportar violações à LGPD, garantindo anonimato quando desejado e transparência no tratamento das informações.

## ✨ Funcionalidades

### Para Usuários
- **Denúncia Anônima**: Registro sem identificação pessoal
- **Token de Acompanhamento**: Código único para consulta do andamento
- **Denúncia Identificada**: Cadastro com conta pessoal
- **Dashboard Pessoal**: Acompanhamento de denúncias registradas
- **Termos LGPD**: Transparência no tratamento de dados

### Para Administradores
- **Painel Administrativo**: Gestão completa de denúncias
- **Controle de Status**: Atualização do andamento das denúncias
- **Relatórios**: Visualização de estatísticas e métricas
- **Gestão de Usuários**: Administração de contas do sistema

## 🛠 Tecnologias Utilizadas

### Backend
- **Python 3.11+**
- **Django 4.2**
- **SQLite** (desenvolvimento)

### Frontend
- **HTML5**
- **CSS3** (Bootstrap 5.3)
- **JavaScript** (Vanilla)
- **Jinja2 Templates**

### Segurança
- **Autenticação Django**
- **Proteção CSRF**
- **Validação de Formulários**
- **Tokens UUID**

## 📥 Instalação e Configuração

### Pré-requisitos
- Python 3.11 ou superior
- pip (gerenciador de pacotes Python)
- Git

### Passos para Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/sandromatiass/Projeto-PI-VI-B.git
cd Projeto-PI-VI-B
```

2. **Crie um ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Execute as migrações**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crie um superusuário**
```bash
python manage.py createsuperuser
```

6. **Execute o servidor**
```bash
python manage.py runserver
```

7. **Acesse o sistema**
- **Sistema**: http://localhost:8000
- **Admin**: http://localhost:8000/admin

## 🏗 Estrutura do Projeto

```
Projeto-PI-VI-B/
├── lgpd_denuncias/          # Configurações do projeto
├── denuncias/               # Aplicação principal
├── templates/               # Templates HTML
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   └── ...
├── static/                  # Arquivos estáticos
├── manage.py
└── requirements.txt
```

## 📊 Modelo de Dados

### Denúncia
- Título e descrição da violação
- Tipo de violação (vazamento, uso indevido, etc.)
- Data da ocorrência
- Status (pendente, em análise, resolvida)
- Token de acompanhamento (para denúncias anônimas)
- Metadados de auditoria

### Usuário
- Sistema de autenticação nativo do Django
- Campos extendidos para conformidade LGPD

## 🔒 Conformidade LGPD

O sistema implementa os seguintes princípios:

- **Finalidade**: Coleta específica para processamento de denúncias
- **Adequação**: Dados pertinentes à finalidade
- **Necessidade**: Minimização da coleta
- **Livre Acesso**: Transparência no tratamento
- **Qualidade**: Verificação e atualização de dados
- **Segurança**: Proteção técnica e administrativa
- **Prevenção**: Mecanismos contra violações

## 🚀 Como Usar

### Para Denunciantes

1. **Denúncia Anônima**
   - Acesse "Denúncia Anônima"
   - Preencha os dados da violação
   - Guarde o token recebido
   - Use o token para acompanhar

2. **Denúncia Identificada**
   - Crie uma conta ou faça login
   - Acesse "Nova Denúncia"
   - Preencha o formulário
   - Acompanhe pelo dashboard

### Para Administradores

1. **Gestão de Denúncias**
   - Acesse o painel administrativo
   - Visualize todas as denúncias
   - Atualize status e observações

## 🧪 Testes

Execute a suíte de testes:
```bash
python manage.py test
```

## 📝 Desenvolvimento

### Adicionando Novas Funcionalidades

1. Crie migrações para mudanças no modelo
```bash
python manage.py makemigrations
```

2. Aplique as migrações
```bash
python manage.py migrate
```

3. Execute testes
```bash
python manage.py test
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique a documentação
2. Abra uma issue no GitHub
3. Entre em contato com a equipe de desenvolvimento

## 🔄 Versões

- **v1.0.0**: Versão inicial com funcionalidades básicas
- **v1.1.0**: Adição de sistema de tokens e acompanhamento

---

**Desenvolvido como projeto acadêmico** - Conformidade LGPD & Tecnologia