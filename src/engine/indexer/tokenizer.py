"""Tokenisation et normalisation du texte.

La même classe doit être utilisée à l'indexation et à la recherche.
"""

from __future__ import annotations


class Tokenizer:
    """Découpe et nettoie le texte (utilisé à l'indexation ET à la recherche)."""

    def __init__(self, language: str = "fr") -> None:
        """Charge la liste de mots vides de la langue demandée.

        Args:
            language: Code de langue utilisé pour choisir les stop words.
        """
        # TODO: Définir la liste de mots vides (stop words : "le", "la", "de", "un", etc.).
        # TODO: Prévoir un jeu de stop words par langue, au minimum le français.
        raise NotImplementedError("TODO: initialiser le tokenizer et ses stop words")

    def tokenize(self, text: str) -> list[str]:
        """Transforme un texte brut en liste de tokens normalisés.

        Args:
            text: Texte issu d'une page ou d'une requête utilisateur.

        Returns:
            Liste de mots en minuscules, sans accents, sans ponctuation,
            sans stop words et sans mots d'une seule lettre.
        """
        # TODO: 1. Tout passer en minuscule.
        # TODO: 2. Retirer les accents (é -> e, à -> a).
        # TODO: 3. Extraire uniquement les mots alphanumériques.
        # TODO: 4. Filtrer les mots vides et les mots d'une seule lettre.
        # TODO: (Phase 4 optionnel) Appliquer une racinisation (stemming).
        raise NotImplementedError("TODO: tokeniser un texte")
