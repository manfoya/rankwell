"""Serveur web Flask du moteur de recherche.

Une seule route GET, rendue côté serveur, sans JavaScript.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flask import Flask

if TYPE_CHECKING:
    from engine.search.ranker import SearchRanker


def create_app(ranker: SearchRanker | None = None) -> Flask:
    """Construit l'application Flask.

    Args:
        ranker: Moteur de recherche à interroger. En production, il est
            construit avec le dépôt PostgreSQL et le tokenizer.

    Returns:
        L'application Flask configurée.
    """
    # TODO: Créer Flask(__name__, template_folder="templates").
    # TODO: Construire un SearchRanker par défaut si ranker est None.
    # TODO: Enregistrer la route GET "/" :
    #       - lire ?q=... et ?w=...
    #       - appeler ranker.rank_query(q, w)
    #       - générer un snippet autour des mots recherchés
    #       - rendre search.html avec résultats et temps de réponse en ms.
    raise NotImplementedError("TODO: créer l'application Flask")
