
# 📋 Agenda de Contatos Django

Uma aplicação web completa para gerenciamento de contatos desenvolvida com Django. Permite criar, visualizar, editar e organizar seus contatos com fotos e categorias.

## 🚀 Demo

Acesse a aplicação em funcionamento: https://agenda-q6n3.onrender.com

## ✨ Funcionalidades

- ✅ **Gerenciamento completo de contatos** (CRUD)
- 📱 **Interface responsiva** e amigável
- 🔐 **Sistema de autenticação** (login/registro)
- 📸 **Upload de fotos** dos contatos (Supabase Storage)
- 🏷️ **Categorização** de contatos
- 🔍 **Listagem paginada** de contatos
- 👤 **Contatos privados** por usuário
- 📊 **Admin panel** do Django

## 🛠️ Tecnologias Utilizadas

- **Backend:** Django 5.2.4
- **Frontend:** HTML5, CSS3, JavaScript
- **Banco de Dados:** PostgreSQL (produção) / SQLite (desenvolvimento)
- **Armazenamento:** Supabase Storage (para imagens)
- **Deploy:** Render.com
- **Outros:** Bootstrap, django-crispy-forms, Pillow

## 📋 Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)
- Git

## 🚀 Instalação e Configuração

### 1. Clone o repositório
```bash
git clone https://github.com/devNatanfreitas/agenda.git
cd agenda
```

### 2. Crie um ambiente virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente
```bash
# Copie o arquivo de exemplo
cp .env.example .env
```

Edite o arquivo `.env` com suas configurações:

```env
# Django Settings
SECRET_KEY=sua_chave_secreta_aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

# Database Configuration
DATABASE_URL=sqlite:///db.sqlite3

# Supabase Configuration (OBRIGATÓRIO para salvar fotos)
SUPABASE_URL=https://seu_projeto.supabase.co
SUPABASE_SERVICE_KEY=sua_service_key_do_supabase
SUPABASE_BUCKET=media
```

### 5. Execute as migrações
```bash
python manage.py migrate
```

### 6. Crie um superusuário (opcional)
```bash
python manage.py createsuperuser
```

### 7. Execute o servidor
```bash
python manage.py runserver
```

A aplicação estará disponível em: http://localhost:8000

## ⚠️ Configuração do Supabase (Obrigatória para Fotos)

Para que o upload de fotos funcione corretamente, você precisa configurar o Supabase:

### 1. Crie uma conta no Supabase
- Acesse: https://supabase.com
- Crie um novo projeto

### 2. Configure o Storage
- No painel do Supabase, vá para **Storage**
- Crie um bucket chamado `media`
- Configure as políticas de acesso público para o bucket

### 3. Obtenha as credenciais
- **SUPABASE_URL**: URL do seu projeto (ex: https://abc123.supabase.co)
- **SUPABASE_SERVICE_KEY**: Service Role Key (encontrada em Settings > API)
- **SUPABASE_BUCKET**: Nome do bucket (`media`)

### 4. Adicione ao .env
```env
SUPABASE_URL=https://seu_projeto.supabase.co
SUPABASE_SERVICE_KEY=sua_service_key_aqui
SUPABASE_BUCKET=media
```

## 🔧 Comandos Úteis

```bash
# Executar testes
python manage.py test

# Criar migrações após alterações nos models
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Coletar arquivos estáticos
python manage.py collectstatic

# Acessar shell do Django
python manage.py shell

# Criar dados de teste (se disponível)
python manage.py shell < utils/create_contacts.py
```

## 📁 Estrutura do Projeto

```
agenda/
├── contact/                 # App principal
│   ├── models.py           # Modelos (Contact, Category)
│   ├── views/              # Views organizadas
│   ├── templates/          # Templates HTML
│   ├── forms.py           # Formulários
│   └── supabase_storage.py # Storage customizado
├── project/                # Configurações Django
├── base_templates/         # Templates base
├── base_static/           # Arquivos estáticos
├── utils/                 # Utilitários
├── requirements.txt       # Dependências
└── manage.py             # Gerenciador Django
```

## 🔐 Funcionalidades de Usuário

- **Registro:** Criar nova conta
- **Login:** Acessar conta existente
- **Perfil:** Atualizar dados do usuário
- **Contatos Privados:** Cada usuário vê apenas seus contatos

## 📱 Interface

- **Design Responsivo:** Funciona em desktop, tablet e mobile
- **Tabela de Contatos:** Lista organizada com paginação
- **Formulários Intuitivos:** Criação e edição simplificada
- **Upload de Imagens:** Adicione fotos aos contatos

## 🤝 Contribuição

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🐛 Problemas Conhecidos

### Salvar Contatos sem Supabase
Se você não configurar o Supabase, os contatos **SEM FOTO** funcionarão normalmente. Apenas o upload de fotos falhará. Para resolver:

1. Configure o Supabase seguindo as instruções acima, OU
2. Comente/remova o campo `picture` do modelo `Contact` e execute as migrações

### SQLite em Produção
O projeto usa SQLite por padrão para desenvolvimento. Para produção, recomenda-se PostgreSQL:

```env
DATABASE_URL=postgresql://usuario:senha@host:5432/banco
```

## 📞 Suporte

- **Issues:** [GitHub Issues](https://github.com/devNatanfreitas/agenda/issues)
- **Documentação:** [Django Documentation](https://docs.djangoproject.com/)
- **Supabase Docs:** [Supabase Documentation](https://supabase.com/docs)

## 🎯 Próximas Funcionalidades

- [ ] Busca de contatos
- [ ] Exportação para CSV/PDF
- [ ] API REST
- [ ] Integração com calendários
- [ ] Backup automático

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!
