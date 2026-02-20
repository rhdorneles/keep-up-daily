# scraper/sources/sao_paulo_rss.py
from .base import BaseScraper
from collections import namedtuple
import feedparser

Article = namedtuple("Article", ["title", "url"])

class SaoPauloRSS(BaseScraper):
    def fetch(self):
        feed_url = "https://ge.globo.com/ESP/Noticia/Rss/0,,AS0-4286,00.xml"
        feed = feedparser.parse(feed_url)

        articles = []
        for entry in feed.entries[:10]:
            articles.append(
                Article(title=entry.title, url=entry.link)  # <-- use object
            )
        return articles
