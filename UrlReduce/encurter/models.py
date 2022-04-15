from django.db import models

class UrlRedirect(models.Model):
    """_summary_
    Modelo para encurtar URLs e redirecionar 

    Args:
        destiny (URLField): campo de formato de URL
        slug (SlugField): campo de formato de slug, que tem como argumento unico para não tem ambiguidades.

    """
    destiny = models.URLField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)
    dated = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'UrlRedirect para {self.destiny}'


class UrlLog(models.Model):
    updated = models.DateTimeField(auto_now=True)
    origin = models.URLField(max_length=512, null=True, blank=True)
    user_agent = models.CharField(max_length=512, null=True, blank=True)
    host = models.CharField(max_length=512, null=True, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    url_redirect = models.ForeignKey(UrlRedirect, models.DO_NOTHING, related_name='Logs')

    def __str__(self):
        return self.host