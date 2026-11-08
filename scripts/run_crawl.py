"""Point d'entrée CLI du crawler.

Exemple d'utilisation future :
    python scripts/run_crawl.py --seeds https://example.bj --max-pages 1000
"""

from __future__ import annotations


def main() -> None:
    """Prépare la configuration puis lance ``CrawlWorker.run``."""
    # TODO: Lire les arguments (--seeds, --max-pages, --mode, --threads).
    # TODO: Charger la configuration avec engine.config.load_settings().
    # TODO: Construire DatabaseRouter, PageRepository, Tokenizer et les filtres de Bloom.
    # TODO: Construire URLFrontier, PoliteFetcher, HTMLParser et CrawlWorker.
    # TODO: Appeler worker.run(seed_urls, max_pages).
    raise NotImplementedError("TODO: implémenter le point d'entrée du crawler")


if __name__ == "__main__":
    main()
