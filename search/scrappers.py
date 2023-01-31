import requests
from bs4 import BeautifulSoup as bs

from search.models import RequestSiteLog


class Scrapper:
    def __init__(self, site, q):
        self.site = site
        self.q = q

    def get_text_from_request_url(self):
        req = ''
        try:
            site_url = f'{self.site.url}/{self.site.page_search_name}?{self.site.param_search_name}={self.q}'
            req = requests.get(site_url)
            return req.text
        except:
            RequestSiteLog.objects.create(site=self.site.name, response=req)
            return None

    def scrape_text(self):
        text = self.get_text_from_request_url()
        if text:
            soup = bs(text, 'lxml')
            return soup

    def get_content(self):
        soup = self.scrape_text()
        if soup:
            results = soup.find_all(class_=self.site.card_class)
            content = []
            for result in results:
                title = result.find(class_=self.site.title_class).text
                url = result.find('a').get('href')
                description = result.find(class_=self.site.description_class).text
                if not url.startswith('http'):
                    url = self.site.url + url[1:]
                content.append((title, url, description))
            return content
