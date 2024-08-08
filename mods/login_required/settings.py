def insert(items, name, before=None, after=None):
    assert type(items) is list
    assert type(name) is str
    assert not (before and after)

    if before is None and after is None:
        after = items[-1]

    i = items.index(before) if before else items.index(after) + 1
    items.insert(i, name)


insert(MIDDLEWARE, 'django.contrib.auth.middleware.LoginRequiredMiddleware',
       after='django.contrib.auth.middleware.AuthenticationMiddleware')
