"""File d'attente des URLs à explorer.

L'ordre de parcours influence fortement la qualité du crawl.
"""

from __future__ import annotations


class URLFrontier:
    """Gère l'ordre d'exploration du graphe web."""

    def __init__(self, mode: str = "bfs") -> None:
        """Initialise la structure de file adaptée au mode choisi.

        Args:
            mode: ``"bfs"`` pour une file FIFO (Phase 3) ou
                ``"best_first"`` pour une file de priorité (Phase 4).
        """
        # TODO: Si mode == "bfs", utiliser une file FIFO (collections.deque).
        # TODO: Si mode == "best_first", utiliser un tas (heapq) basé sur le
        #       nombre de liens entrants (priorité la plus haute d'abord).
        # TODO: Valider le mode et lever ValueError sinon.
        raise NotImplementedError("TODO: initialiser la frontière d'URLs")

    def push(self, url: str, priority: int = 0) -> None:
        """Ajoute une URL à explorer si elle n'a pas déjà été visitée.

        Args:
            url: URL absolue normalisée.
            priority: Priorité utilisée en mode ``"best_first"``.
        """
        # TODO: Ignorer l'URL si le filtre de Bloom indique qu'elle a déjà été vue.
        # TODO: Ajouter l'URL dans la file (FIFO ou tas selon le mode).
        raise NotImplementedError("TODO: ajouter une URL à la frontière")

    def pop(self) -> str | None:
        """Extrait la prochaine URL à visiter.

        Returns:
            L'URL suivante, ou ``None`` si la frontière est vide.
        """
        # TODO: Extraire l'élément de tête (ou la priorité maximale).
        raise NotImplementedError("TODO: extraire une URL de la frontière")

    def __len__(self) -> int:
        """Retourne le nombre d'URLs encore en attente."""
        # TODO: Retourner la taille de la structure interne.
        raise NotImplementedError("TODO: retourner la taille de la frontière")
