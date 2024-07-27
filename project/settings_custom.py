"""
Put your custom settings here, not in settings.py

Settings structure:

- settings.py         : Defaults from Django, do not edit
- settings_ansible.py : Generated by Ansible (not committed)
- settings_custom.py  : Your custom project settings, edit this one
"""

# Standard Library
from socket import getfqdn

# Requirements
from dotenv import load_dotenv

# Project
from project.settings_ansible import *


# Load environment variables
load_dotenv(f'{BASE_DIR}/.envrc')

# Applications
INSTALLED_APPS += [
]

# Static files
STATICFILES_DIRS = [
    BASE_DIR / 'project' / 'static',
]

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'project' / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Emails
ADMINS = ()
MANAGERS = ADMINS

fqdn = getfqdn()
DEFAULT_FROM_EMAIL = 'webmaster@' + fqdn
SERVER_EMAIL = 'root@' + fqdn

# Local settings, these should not be committed
try:
    from .settings_local import *
except ImportError:
    pass
