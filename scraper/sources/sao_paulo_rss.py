# scraper/sources/sao_paulo_rss.py
from .base import BaseScraper
import feedparser

class SaoPauloRSS(BaseScraper):
    def fetch(self):
        feed_url = "https://ge.globo.com/ESP/Noticia/Rss/0,,AS0-4286,00.xml"
        feed = feedparser.parse(feed_url)

        articles = []
        for entry in feed.entries[:10]:  # get the 10 latest news
            articles.append({
                "title": entry.title,
                "url": entry.link
            })

        return articles
