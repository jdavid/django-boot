INSTALLED_APPS += ['channels']
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}

{% if django.debug %}
INSTALLED_APPS.insert(0, 'daphne')
ASGI_APPLICATION = 'project.asgi.application'
{% endif %}
