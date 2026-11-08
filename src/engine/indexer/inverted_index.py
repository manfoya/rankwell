"""Construction de l'index inversé.

Lit les pages stockées et remplit la table
``inverted_index`` avec les fréquences de termes.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.db.repository import PageRepository
    from engine.indexer.tokenizer import Tokenizer


class InvertedIndexBuilder:
    """Construit l'index inversé (mot -> liste de [page_id, fréquence])."""

    def __init__(self, repository: PageRepository, tokenizer: Tokenizer) -> None:
        """Reçoit les dépendances nécessaires à l'indexation.

        Args:
            repository: Accès aux pages et à la table ``inverted_index``.
            tokenizer: Tokenizer partagé avec le moteur de recherche.
        """
        raise NotImplementedError("TODO: mémoriser les dépendances de l'indexeur")

    def build_index_for_all_pages(self) -> None:
        """Parcourt toutes les pages et enregistre leur index inversé."""
        # TODO: 1. Lire le texte de chaque page depuis la BDD.
        # TODO: 2. Appeler Tokenizer.tokenize(text).
        # TODO: 3. Compter combien de fois chaque mot apparaît dans la page.
        # TODO: 4. Enregistrer (mot, page_id, compte) dans la table 'inverted_index'.
        # TODO: 5. Mettre à jour doc_length et la longueur moyenne globale.
        raise NotImplementedError("TODO: construire l'index inversé")
