import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from .models import Provedor,ComprasEncabezado,ComprasDetalle
from django.shortcuts import get_object_or_404


def link_callback(uri, rel):
            """
            Convert HTML URIs to absolute system paths so xhtml2pdf can access those
            resources
            """
            result = finders.find(uri)
            if result:
                    if not isinstance(result, (list, tuple)):
                            result = [result]
                    result = list(os.path.realpath(path) for path in result)
                    path=result[0]
            else:
                    sUrl = settings.STATIC_URL        # Typically /static/
                    sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
                    mUrl = settings.MEDIA_URL         # Typically /media/
                    mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

                    if uri.startswith(mUrl):
                            path = os.path.join(mRoot, uri.replace(mUrl, ""))
                    elif uri.startswith(sUrl):
                            path = os.path.join(sRoot, uri.replace(sUrl, ""))
                    else:
                            return uri

            # make sure that file exists
            if not os.path.isfile(path):
                    raise RuntimeError(
                            'media URI must start with %s or %s' % (sUrl, mUrl)
                    )
            return path
        
        
def render_pdf_view(request):
    template_path = 'cmp/compras_pdf.html'
    #dia = timezone.now()
    compras = ComprasEncabezado.objects.all()
    
    context = {'obj': compras,'request': request}
    
    #creas el objeto de respuesta en django
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="DetalleCompras.pdf"'
    
    #pasamos la plantilla
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def imprimir_compras(request, pk):
    template_path = 'cmp/compra_detalle_pdf.html'
    detalles = ComprasDetalle.objects.filter(compra_id=pk)
    compraEn = get_object_or_404(ComprasEncabezado, id=pk)
    

    context = {'detalle': detalles, 'encabezado': compraEn, 'request': request}
    
    # Crear el objeto de respuesta en Django
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="compra.pdf"'

    # Pasar la plantilla
    template = get_template(template_path)
    html = template.render(context)

    # Crear el PDF
    pisa_status = pisa.CreatePDF(html, dest=response, link_callback=link_callback)

    # Manejar errores si existen
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response