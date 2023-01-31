import requests
from bs4 import BeautifulSoup as bs


class Scrapper:
    def __init__(self, site, topic, url, title, description):
        self.site = site
        self.topic = topic
        self.url = url
        self.title = title
        self.description = description

    def get_text_from_request_url(self):
        try:
            req = requests.get(self.site)
            return req.text
        except:
            return ''

    def scrape_text(self):
        text = self.get_text_from_request_url()
        soup = bs(text, 'lxml')
        print(soup)
        return soup

    def get_content(self):
        soup = self.scrape_text()
        results = soup.find_all('div', {'class': self.topic})
        content = []
        print(self.site, self.topic, self.title, self.url, self.description)
        for result in results:
            title = result.find(class_=self.title).text
            url = result.find(class_=self.url).get('href')
            description = result.find(class_=self.description).text
            content.append((title, url, description))
        return content
