"""Tests unitaires du calcul BM25."""

from __future__ import annotations

import pytest


def test_bm25_matches_manual_example() -> None:
    """Le score BM25 doit correspondre à un calcul manuel sur un mini corpus."""
    # TODO: Construire un mini corpus (2 ou 3 documents) et une requête.
    # TODO: Calculer BM25 à la main, puis comparer au résultat de SearchRanker.
    pytest.skip("TODO: implémenter BM25")


def test_bm25_favors_rare_terms() -> None:
    """Un terme rare doit peser plus qu'un terme présent partout."""
    # TODO: Vérifier que l'IDF d'un terme rare est supérieur à celui d'un terme fréquent.
    pytest.skip("TODO: implémenter BM25")
