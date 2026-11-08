"""Évaluation de la qualité des résultats sur les 20 requêtes de test.

Compare BM25 seul, PageRank seul et leur combinaison.
"""

from __future__ import annotations

from pathlib import Path


def evaluate(queries_path: Path, k: int = 5) -> dict[str, float]:
    """Calcule la qualité moyenne des résultats pour plusieurs valeurs de ``w``.

    Args:
        queries_path: Fichier contenant les requêtes et les URLs jugées
            pertinentes manuellement.
        k: Taille du top utilisé pour Precision@K.

    Returns:
        Dictionnaire associant chaque configuration (``bm25``, ``pagerank``,
        ``w=0.3``, etc.) à sa précision moyenne.
    """
    # TODO: 1. Charger les requêtes et leurs jugements manuels.
    # TODO: 2. Faire tourner chaque requête avec BM25 seul (w = 1.0),
    #          PageRank seul (w = 0.0) et w = 0.3, 0.5, 0.7, 0.85.
    # TODO: 3. Calculer Precision@K pour chaque configuration.
    # TODO: 4. Retourner le tableau comparatif.
    raise NotImplementedError("TODO: implémenter l'évaluation")


def main() -> None:
    """Point d'entrée CLI de l'évaluation."""
    # TODO: Lire --queries et --k, appeler evaluate() et afficher un tableau.
    raise NotImplementedError("TODO: implémenter le point d'entrée d'évaluation")


if __name__ == "__main__":
    main()
