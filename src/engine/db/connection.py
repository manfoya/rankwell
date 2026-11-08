"""Gestion des connexions PostgreSQL et du routage vers les shards.

Toute la logique de choix de base de données doit rester ici.
"""

from __future__ import annotations

from typing import Any


class DatabaseRouter:
    """Gère la connexion à la base principale et aux bases fragmentées (Shards)."""

    def __init__(self, main_db_url: str, shard_db_urls: list[str] | None = None) -> None:
        """Initialise les connexions vers la base principale et les shards.

        Args:
            main_db_url: URL de connexion de la base principale (Phase 3).
            shard_db_urls: URLs des bases secondaires (Phase 4), vide en Phase 3.
        """
        # TODO: Initialiser la connexion (ou un pool psycopg_pool) vers la base principale.
        # TODO: Initialiser les connexions vers les bases secondaires (shards) si présentes.
        raise NotImplementedError("TODO: initialiser les connexions PostgreSQL")

    def get_connection_for_domain(self, domain: str) -> Any:
        """Choisit la connexion à utiliser pour un nom de domaine donné.

        Phase 4 : calcule un hash du domaine modulo le nombre de
        bases de données afin de répartir les pages (sharding).

        Args:
            domain: Nom de domaine de la page, par exemple ``"gouv.bj"``.

        Returns:
            La connexion à la base principale en Phase 3, ou la connexion du
            shard correspondant en Phase 4.
        """
        # TODO: Retourner la connexion principale si aucun shard n'est configuré.
        # TODO: Sinon, calculer hash(domain) % len(shard_db_urls) et retourner le bon shard.
        raise NotImplementedError("TODO: implémenter le routage par domaine")
