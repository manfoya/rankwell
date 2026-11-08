"""Tests du PageRank : comparaison avec NetworkX sur un petit graphe."""

from __future__ import annotations

import pytest


def test_custom_pagerank_equals_networkx() -> None:
    """Le PageRank maison doit égaler celui de NetworkX."""
    # TODO: 1. Créer un petit graphe orienté de 5 ou 6 noeuds.
    # TODO:    Inclure au moins un noeud sans lien sortant (dangling node).
    # TODO: 2. Lancer PageRankPython.power_iteration().
    # TODO: 3. Lancer networkx.pagerank() sur le même graphe.
    # TODO: 4. Vérifier avec numpy.testing.assert_allclose.
    pytest.skip("TODO: implémenter le PageRank et le test NetworkX")


def test_pagerank_scores_sum_to_one() -> None:
    """La somme des scores doit rester égale à 1."""
    # TODO: Vérifier abs(sum(scores) - 1.0) < tol.
    pytest.skip("TODO: implémenter le PageRank")
