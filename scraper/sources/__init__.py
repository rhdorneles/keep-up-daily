"""Source scrapers for keep-up-daily."""

from .sao_paulo_rss import SaoPauloRSS

ALL_SCRAPERS = [
    SaoPauloRSS,
]

__all__ = [
    "SaoPauloRSS",
    "ALL_SCRAPERS",
]
