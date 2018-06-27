from django.template.response import TemplateResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from .forms import CountryForm
from . import service

def countries_form(request):
    if request.method == 'POST':
        post_form = CountryForm(request.POST)

        if post_form.is_valid():
            country_name = post_form.cleaned_data['name']
            service.add_country(country_name)
            return HttpResponseRedirect('/guide/countriesform/')
    else:
        get_form = CountryForm()
        countries = service.get_countries_all()

    return render(request, 'guide/countries_form.html', {'form': get_form, 'countries': countries})

def countries_view(request):
    countries = service.get_countries_all()
    return TemplateResponse(request, 'guide/countries_view.html', {
        'countries': countries
    })

def guide_view(request):
    return TemplateResponse(request, 'guide/index.html')
