"""Scoring des résultats de recherche.

BM25 pour la pertinence textuelle, fusion avec le PageRank pour
l'autorité des pages.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from engine.db.repository import PageRepository
    from engine.indexer.tokenizer import Tokenizer


class SearchRanker:
    """Calcule BM25 et le combine avec PageRank."""

    def __init__(self, repository: PageRepository, tokenizer: Tokenizer) -> None:
        """Reçoit les dépendances du moteur de recherche.

        Args:
            repository: Accès aux index, pages et scores PageRank.
            tokenizer: Tokenizer identique à celui utilisé pour l'indexation.
        """
        raise NotImplementedError("TODO: mémoriser les dépendances du ranker")

    def compute_bm25(
        self,
        query_tokens: list[str],
        k1: float = 1.5,
        b: float = 0.75,
    ) -> dict[int, float]:
        """Calcule le score BM25 des pages candidates.

        Formule pour chaque mot ``q_i`` de la requête dans un document ``D`` :
        ``IDF(q_i) * (tf * (k1 + 1)) / (tf + k1 * (1 - b + b * (|D| / avgdl)))``

        Args:
            query_tokens: Tokens normalisés de la requête.
            k1: Paramètre de saturation de la fréquence de terme.
            b: Paramètre de normalisation par la longueur du document.

        Returns:
            Dictionnaire ``{page_id: score_bm25}``.
        """
        # TODO: 1. Chercher dans 'inverted_index' les pages contenant au moins un mot.
        # TODO: 2. Appliquer la formule BM25 pour chaque page candidate.
        # TODO: 3. Retourner {page_id: score_bm25}.
        raise NotImplementedError("TODO: calculer BM25")

    def rank_query(
        self,
        raw_query: str,
        weight_bm25: float = 0.7,
        top_k: int = 10,
    ) -> list[dict[str, Any]]:
        """Classe les pages pour une requête brute.

        Score final : ``w * BM25_norm + (1 - w) * PageRank_norm``.

        Args:
            raw_query: Requête saisie par l'utilisateur.
            weight_bm25: Poids ``w`` du BM25, entre 0 et 1.
            top_k: Nombre de résultats à retourner.

        Returns:
            Liste de dictionnaires triés par score décroissant. Chaque
            résultat contient au minimum ``page_id``, ``url``, ``title``,
            ``score`` et ``snippet``.
        """
        # TODO: 1. Découper raw_query avec Tokenizer.tokenize().
        # TODO: 2. Obtenir les scores BM25 et les PageRank des pages candidates.
        # TODO: 3. Normaliser BM25 et PageRank entre 0 et 1.
        # TODO: 4. Calculer le score final, trier et retourner les top_k pages.
        raise NotImplementedError("TODO: classer les résultats d'une requête")
