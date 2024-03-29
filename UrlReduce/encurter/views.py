from django.db.models.functions import TruncDate
from django.db.models import Count
from django.shortcuts import render, redirect

from UrlReduce.encurter.models import UrlLog, UrlRedirect

def relatorios(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    url_reduzida = request.build_absolute_uri(f'/{slug}')
    redirecionamentos_por_data = list(
        UrlRedirect.objects.filter(
            slug=slug
        ).annotate(
            data=TruncDate('Logs__updated')
        ).annotate(
            cliques=Count('data')
        ).order_by(
            'data'
        )
    )

    context = {''
        'reduce': url_redirect,
        'url_reduzida': url_reduzida, 
        'redirecionamentos_por_data': redirecionamentos_por_data,
        'total_de_cliques': sum(r.cliques for r in redirecionamentos_por_data)   
        }
    return render(request, 'encurter/relatorio.html', context)
    

def redirecionar(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    UrlLog.objects.create(
        origin = request.META.get('HTTP_REFERER '),
        user_agent = request.META.get('HTTP_USER_AGENT'), 
        host = request.META.get('HTTP_HOST'),
        ip = request.META.get('REMOTE_ADDR'),
        url_redirect = url_redirect
    ) 

    return redirect(url_redirect.destiny)
      
