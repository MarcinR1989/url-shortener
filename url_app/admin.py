import django.contrib.auth.models
from django.contrib import admin, auth
from url_app.models import ShortUrl


@admin.register(ShortUrl)
class ShortUrlAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)

