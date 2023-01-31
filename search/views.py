import random

from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from search.scrappers import Scrapper
from search.sites import sites


class HomeView(TemplateView):
    template_name = 'index.html'


class SearchView(TemplateView):
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', None)
        if q:
            final_result = []
            for site in sites:
                site_url = f"{site['site_url']}{q}"
                topic = site['topic']
                title = site['title']
                url = site['url']
                description = site['description']
                ask_scrapper = Scrapper(site_url, topic, url, title, description)
                content = ask_scrapper.get_content()
                print(f'Content --> {content}')
                final_result += content
            print(f'final_result --> {final_result}')
            random.shuffle(final_result)
            context = {
                'final_result': final_result
            }
            return render(request, 'search.html', context)
        else:
            return redirect('index')
