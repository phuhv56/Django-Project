from django.shortcuts import render
from django.shortcuts import  render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from club.models import Club
# Create your views here.
def simple_request(request):
    name = 'Rich'
    html = '<html> Hi %s this is simple request view in django </html>' % name
    return HttpResponse(html)
def template_request(request):
    name = 'Rich'
    t = get_template('exp.html')
    ctext = Context({'name': name})
    html = t.render(ctext)
    return HttpResponse(html)
def temp_simple(request):
    name = 'Phus'
    return render_to_response('exp.html', {'name': name})
def clubs(request):
    return render_to_response('clubs.html', {'clubs': Club.objects.all()})
def club(request, club_id=1):
    return render_to_response('club.html', {'club': Club.objects.get(id=club_id)})