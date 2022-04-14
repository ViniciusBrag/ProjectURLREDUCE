from django.shortcuts import render, redirect

from UrlReduce.encurter.models import UrlRedirect


def relatorios(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    url_reduzida = request.build_absolute_uri(f'/{slug}')
    context = {''
        'reduce': url_redirect,
        'url_reduzida': url_reduzida,   
        }
    return render(request, 'encurter/relatorio.html', context)
    

def redirecionar(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    return redirect(url_redirect.destiny)
