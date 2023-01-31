import random

from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from search.models import Site
from search.scrappers import Scrapper


class HomeView(TemplateView):
    template_name = 'index.html'


class SearchView(TemplateView):
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', None)
        if q:
            final_result = []
            sites = Site.objects.all()
            for site in sites:
                ask_scrapper = Scrapper(site, q)
                content = ask_scrapper.get_content()
                final_result += content
            random.shuffle(final_result)
            context = {
                'final_result': final_result
            }
            return render(request, 'search.html', context)
        else:
            return redirect('index')
