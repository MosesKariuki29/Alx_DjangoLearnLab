from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_4a@mxx@8)j+a_!e937c6@#4b_rub!wd+y+8q996!j8#@a_m*w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# ==============================
# Security Configuration
# ==============================

SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

CSRF_TRUSTED_ORIGINS = [
    "https://yourdomain.com",
]

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]


# =========================
# Application Definition
# =========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'csp',  # Django CSP app

    'bookshelf',
    'relationship_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # CSP Middleware (must be high in the list)
    'csp.middleware.CSPMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'LibraryProject.wsgi.application'


# =========================
# Database
# =========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =========================
# Password Validation
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# =========================
# Internationalization
# =========================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# =========================
# Static & Media Files
# =========================
STATIC_URL = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# =========================
# Authentication
# =========================
LOGIN_REDIRECT_URL = 'list_books'
LOGOUT_REDIRECT_URL = 'login'
AUTH_USER_MODEL = 'bookshelf.CustomUser'


# =========================
# Content Security Policy
# =========================

# Only allow resources from your own domain by default
CSP_DEFAULT_SRC = ("'self'",)

# Allow styles from self (add Google Fonts etc if needed)
CSP_STYLE_SRC = ("'self'",)

# Allow scripts only from self
CSP_SCRIPT_SRC = ("'self'",)

# Allow images from self and data URIs
CSP_IMG_SRC = ("'self'", "data:")

# Allow fonts from self
CSP_FONT_SRC = ("'self'",)

# Block all object embeds (Flash, etc.)
CSP_OBJECT_SRC = ("'none'",)

# Prevent the site from being embedded in iframes
CSP_FRAME_ANCESTORS = ("'none'",)