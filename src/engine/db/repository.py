"""Requêtes SQL du projet.

Aucune requête SQL ne doit se trouver en dehors de ce module.
"""

from __future__ import annotations

from typing import Any


class PageRepository:
    """Regroupe toutes les opérations SQL liées aux pages, liens et index."""

    def __init__(self, connection: Any) -> None:
        """Conserve la connexion PostgreSQL fournie par ``DatabaseRouter``.

        Args:
            connection: Connexion psycopg (ou pool) déjà ouverte.
        """
        raise NotImplementedError("TODO: mémoriser la connexion PostgreSQL")

    def save_page(
        self,
        url: str,
        domain: str,
        content_hash: str,
        text: str,
        status: int,
    ) -> int:
        """Insère une page dans la table ``pages`` et retourne son identifiant.

        Args:
            url: URL absolue normalisée de la page.
            domain: Domaine de la page, par exemple ``"gouv.bj"``.
            content_hash: Empreinte SHA-256 du texte propre.
            text: Texte propre extrait du HTML.
            status: Code HTTP observé lors du téléchargement.

        Returns:
            L'identifiant SQL de la page insérée.
        """
        # TODO: Exécuter un INSERT ... RETURNING id et retourner la valeur.
        raise NotImplementedError("TODO: insérer une page")

    def hash_exists(self, content_hash: str) -> bool:
        """Indique si une empreinte de contenu existe déjà en base.

        Cette vérification a lieu après le filtre de Bloom, pour éliminer ses
        faux positifs.

        Args:
            content_hash: Empreinte SHA-256 à rechercher.

        Returns:
            ``True`` si une page possède déjà cette empreinte, sinon ``False``.
        """
        # TODO: Exécuter un SELECT 1 FROM pages WHERE content_hash = %s.
        raise NotImplementedError("TODO: vérifier l'existence d'un contenu")

    def save_links(self, source_id: int, target_urls: list[str]) -> None:
        """Insère les liens sortants d'une page dans la table ``links``.

        Args:
            source_id: Identifiant SQL de la page source.
            target_urls: URLs absolues des cibles. Les cibles absentes de la
                table ``pages`` doivent être créées ou ignorées selon la
                stratégie retenue.
        """
        # TODO: Résoudre chaque URL cible en target_id puis insérer (source_id, target_id).
        # TODO: Utiliser ON CONFLICT DO NOTHING pour éviter les doublons d'arêtes.
        raise NotImplementedError("TODO: enregistrer les liens sortants")

    def fetch_all_links(self) -> list[tuple[int, int]]:
        """Récupère toutes les arêtes du graphe.

        Returns:
            Liste de couples ``(source_id, target_id)`` prêts pour la
            construction de la matrice CSR.
        """
        # TODO: Exécuter SELECT source_id, target_id FROM links.
        raise NotImplementedError("TODO: récupérer toutes les arêtes")
