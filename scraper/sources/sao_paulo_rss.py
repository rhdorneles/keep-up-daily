from .base import BaseScraper
from dataclasses import dataclass, field, asdict
from typing import List
import feedparser
import logging

logger = logging.getLogger(__name__)

@dataclass
class Article:
    title: str
    url: str
    description: str
    tags: List[str] = field(default_factory=list)
    category: str = ""        # for categorizer
    score: float = 0.0        # for sorting
    author: str = ""          # for digest/fallback
    source: str = ""          # the scraper identifier
    comments_count: int = 0   # fallback digest expects this

    def to_dict(self):
        """Convert Article to dictionary for JSON serialization."""
        return asdict(self)

class SaoPauloRSS(BaseScraper):
    """Scraper for São Paulo FC news from Globo RSS feed."""

    def fetch(self):
        feed_url = "https://www.arqtricolor.com/feed/"
        feed = feedparser.parse(feed_url)

        articles = []

        for entry in feed.entries[:20]:  # fetch more to allow filtering
            title = getattr(entry, "title", "")
            if "São Paulo" not in title:
                continue  # skip unrelated articles

            link = getattr(entry, "link", "")
            description = getattr(entry, "summary", "") or ""
            tags = [tag.term for tag in getattr(entry, "tags", [])] if getattr(entry, "tags", None) else []
            author = getattr(entry, "author", "")

            articles.append(
                Article(
                    title=title,
                    url=link,
                    description=description,
                    tags=tags,
                    author=author,
                    source="sao_paulo_rss",
                    comments_count=0
                )
            )

        logger.info(f"Fetched {len(articles)} São Paulo articles from Globo RSS")
        return articles