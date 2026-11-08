"""Point d'entrée CLI du calcul de PageRank.

Exemple d'utilisation future :
    python scripts/run_pagerank.py --implementation python --export data/graph.csr
"""

from __future__ import annotations


def main() -> None:
    """Construit le graphe, calcule les scores et les enregistre en base."""
    # TODO: Lire les arguments (--implementation, --damping, --threads, --export).
    # TODO: Construire DatabaseRouter, PageRepository et GraphBuilder.
    # TODO: Appeler build_csr_matrix().
    # TODO: Lancer PageRankPython ou PageRankCppBridge selon l'option.
    # TODO: Écrire les scores dans pages.pagerank.
    raise NotImplementedError("TODO: implémenter le point d'entrée du PageRank")


if __name__ == "__main__":
    main()
