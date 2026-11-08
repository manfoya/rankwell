"""Tests unitaires du tokenizer."""

from __future__ import annotations

import pytest


def test_tokenizer_removes_accents_and_case() -> None:
    """Le texte doit être mis en minuscules et désaccentué."""
    # TODO: Vérifier que "École" devient "ecole".
    pytest.skip("TODO: implémenter le tokenizer")


def test_tokenizer_removes_stop_words_and_single_letters() -> None:
    """Les mots vides et les mots d'une lettre doivent disparaître."""
    # TODO: Vérifier que "le chat et a" devient ["chat"].
    pytest.skip("TODO: implémenter le filtrage des stop words")


def test_tokenizer_is_identical_for_index_and_query() -> None:
    """La même instance doit produire les mêmes tokens dans les deux usages."""
    # TODO: Comparer tokenize(page_text) et tokenize(query_text).
    pytest.skip("TODO: vérifier la cohérence indexation / recherche")
