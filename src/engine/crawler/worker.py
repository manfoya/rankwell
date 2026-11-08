"""Boucle principale du robot d'exploration.

Orchestre frontier, fetcher, parser, filtres et stockage.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.crawler.bloom import BloomFilter
    from engine.crawler.fetcher import PoliteFetcher
    from engine.crawler.frontier import URLFrontier
    from engine.crawler.parser import HTMLParser
    from engine.db.repository import PageRepository


class CrawlWorker:
    """Relie les composants du crawler pour explorer un ensemble de pages."""

    def __init__(
        self,
        frontier: URLFrontier,
        fetcher: PoliteFetcher,
        parser: HTMLParser,
        repository: PageRepository,
        url_filter: BloomFilter,
        content_filter: BloomFilter,
    ) -> None:
        """Reçoit les dépendances du crawler (injection explicite).

        Args:
            frontier: File des URLs à visiter.
            fetcher: Client HTTP poli.
            parser: Extracteur de texte et de liens.
            repository: Accès aux tables PostgreSQL.
            url_filter: Filtre de Bloom des URLs déjà vues.
            content_filter: Filtre de Bloom des contenus déjà vus.
        """
        raise NotImplementedError("TODO: mémoriser les dépendances du worker")

    def run(self, seed_urls: list[str], max_pages: int = 1000) -> None:
        """Lance l'exploration depuis les URLs de départ.

        Args:
            seed_urls: URLs initiales du crawl.
            max_pages: Nombre maximal de pages à traiter.
        """
        # TODO: Boucler tant que la frontière n'est pas vide et que pages < max_pages :
        # TODO: 1. Prendre une URL dans la frontière.
        # TODO: 2. Télécharger la page avec PoliteFetcher.
        # TODO: 3. Extraire texte, hash et liens avec HTMLParser.
        # TODO: 4. Vérifier le hash dans le filtre de Bloom, puis en BDD pour les faux positifs.
        # TODO: 5. Sauvegarder la page et ses liens en BDD.
        # TODO: 6. Ajouter les nouveaux liens à la frontière.
        raise NotImplementedError("TODO: implémenter la boucle de crawl")
