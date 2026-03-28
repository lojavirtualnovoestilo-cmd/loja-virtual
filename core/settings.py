import os
from pathlib import Path
import dj_database_url

# 1. Caminhos e Segurança
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-bs-0+rc7atrk3c+6wl4x%4&mq1crrhngp5#x)r@=n2tx#l11n3'
DEBUG = True # Mantenha True para vermos erros se houver, depois mudamos
ALLOWED_HOSTS = ['loja-virtual-t5sm.onrender.com', '127.0.0.1', 'localhost']

# 2. Aplicativos
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'produtos', 
]

# 3. Middleware (Segurança e Estáticos)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

# 4. Visual (Templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# 5. BANCO DE DADOS (Ajustado para o Pooler do Supabase - Sem erros de socket)
DATABASES = {
    'default': dj_database_url.parse('postgresql://postgres:AUosKuyU8y7WBr8E@://aws-0-sa-east-1.pooler.supabase.com')
}

# 6. Idioma e Arquivos Estáticos
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
