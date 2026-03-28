import os
from pathlib import Path
import dj_database_url

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Chave de segurança (Mantenha em segredo!)
SECRET_KEY = 'django-insecure-bs-0+rc7atrk3c+6wl4x%4&mq1crrhngp5#x)r@=n2tx#l11n3'

# DEBUG deve ser True para testes, False em produção real
DEBUG = True

# Links autorizados a acessar o site
ALLOWED_HOSTS = ['loja-virtual-t5sm.onrender.com', '127.0.0.1', 'localhost']

# Definição dos Apps instalados
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'produtos', # Seu app de roupas
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Ajuda a carregar estilos no Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

# Configuração do visual (Templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Pasta onde ficará o seu home.html
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# BANCO DE DADOS (Configurado para máxima estabilidade no Supabase)
# Usando o modo Pooler (porta 6543) para evitar erros de rede no Render
# BANCO DE DADOS - CORRIGIDO E DIRETO
DATABASES = {
    'default': dj_database_url.parse('postgresql://postgres:AUosKuyU8y7WBr8E@://aws-0-sa-east-1.pooler.supabase.com')
}

# Validação de senhas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Idioma e fuso horário
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# Arquivos Estáticos (CSS, Imagens, JS)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Padrão para campos de ID
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
