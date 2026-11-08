"""Paramètres globaux du moteur de recherche.

Ce module centralise les valeurs de configuration afin qu'aucun autre fichier
n'ait à lire directement les variables d'environnement.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class Settings:
    """Configuration immuable du moteur.

    Les valeurs par défaut correspondent à l'environnement Docker local.
    Utiliser ``Settings.from_env()`` pour prendre en compte le fichier ``.env``
    déjà chargé par l'appelant (par exemple via ``python-dotenv``).
    """

    database_url: str = "postgresql://rankwell:rankwell@localhost:5432/rankwell"
    shard_database_urls: tuple[str, ...] = ()
    user_agent: str = "RankWellBot/0.1 (+https://example.org/bot)"
    crawl_delay_seconds: float = 1.0
    damping: float = 0.85
    tolerance: float = 1e-6
    max_iterations: int = 200
    top_k: int = 10
    weight_bm25: float = 0.7
    data_dir: Path = Path("data")

    @classmethod
    def from_env(cls) -> Settings:
        """Construit la configuration à partir des variables d'environnement.

        Variables lues : ``DATABASE_URL``, ``SHARD_DATABASE_URLS``,
        ``USER_AGENT``, ``CRAWL_DELAY_SECONDS``, ``DAMPING``, ``TOLERANCE``,
        ``MAX_ITERATIONS``, ``TOP_K``, ``WEIGHT_BM25`` et ``DATA_DIR``.
        """
        shard_urls = tuple(
            url.strip()
            for url in os.getenv("SHARD_DATABASE_URLS", "").split(",")
            if url.strip()
        )
        return cls(
            database_url=os.getenv(
                "DATABASE_URL", "postgresql://rankwell:rankwell@localhost:5432/rankwell"
            ),
            shard_database_urls=shard_urls,
            user_agent=os.getenv("USER_AGENT", "RankWellBot/0.1 (+https://example.org/bot)"),
            crawl_delay_seconds=float(os.getenv("CRAWL_DELAY_SECONDS", "1.0")),
            damping=float(os.getenv("DAMPING", "0.85")),
            tolerance=float(os.getenv("TOLERANCE", "1e-6")),
            max_iterations=int(os.getenv("MAX_ITERATIONS", "200")),
            top_k=int(os.getenv("TOP_K", "10")),
            weight_bm25=float(os.getenv("WEIGHT_BM25", "0.7")),
            data_dir=Path(os.getenv("DATA_DIR", "data")),
        )


def load_settings() -> Settings:
    """Charge le fichier ``.env`` s'il existe, puis retourne la configuration."""
    try:
        from dotenv import load_dotenv
    except ImportError:  # pragma: no cover - dépendance déclarée dans pyproject.toml
        pass
    else:
        load_dotenv()
    return Settings.from_env()
