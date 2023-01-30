import requests
from bs4 import BeautifulSoup as bs
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View


class HomeView(TemplateView):
    template_name = 'index.html'


class SearchView(View):
    http_method_names = ['post']
    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.http_method_names:
            search = self.request.POST.get('search')
            url = f'https://www.ask.com/web?q={search}'
            req = requests.get(url)
            soup = bs(req.text, 'lxml')
            result_listings = soup.find_all('div', {'class': 'PartialSearchResults-item-wrapper'})
            final_result = []
            for result in result_listings:
                title = result.find(class_='PartialSearchResults-item-title').text
                url = result.find('a').get('href')
                description = result.find(class_='PartialSearchResults-item-abstract').text
                final_result.append((title, url, description))
            context = {
                'final_result': final_result
            }
            return render(request, 'search.html', context)
        else:
            return redirect('index')
