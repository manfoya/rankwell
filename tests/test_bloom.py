"""Tests unitaires du filtre de Bloom."""

from __future__ import annotations

import pytest


def test_bloom_filter_has_no_false_negatives() -> None:
    """Un élément ajouté doit toujours être retrouvé."""
    # TODO: Ajouter plusieurs éléments et vérifier que might_contain retourne True.
    # TODO: Vérifier qu'un élément jamais ajouté retourne False (ou un faux positif).
    pytest.skip("TODO: implémenter le filtre de Bloom")


def test_bloom_filter_uses_expected_parameters() -> None:
    """La taille m et le nombre de hachages k doivent suivre les formules."""
    # TODO: Vérifier m et k pour n et p connus.
    pytest.skip("TODO: implémenter le dimensionnement du filtre de Bloom")
