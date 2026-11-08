"""Benchmarks et figures de performance (Phase 4)."""

from __future__ import annotations

from typing import Any


def benchmark_graph() -> dict[str, Any]:
    """Compare le crawl BFS et Best-First et produit les statistiques du graphe."""
    # TODO: Générer le tableau des statistiques (degrés, composantes, hubs).
    # TODO: Comparer BFS vs Best-First (qualité et temps).
    raise NotImplementedError("TODO: implémenter le benchmark du graphe")


def benchmark_pagerank() -> dict[str, Any]:
    """Trace les courbes de convergence et compare Power Iteration et Jacobi."""
    # TODO: Tester d = 0.5, 0.7, 0.85, 0.95.
    # TODO: Tracer erreur vs itération pour chaque méthode.
    # TODO: Mesurer la mémoire CSR vs dense.
    raise NotImplementedError("TODO: implémenter le benchmark du PageRank")


def benchmark_cpp_speedup() -> dict[str, Any]:
    """Compare les temps Python et C++ pour 1, 2, 4 et 8 threads."""
    # TODO: Mesurer les temps d'exécution pour chaque nombre de threads.
    # TODO: Vérifier que les scores C++ et Python sont identiques.
    raise NotImplementedError("TODO: implémenter le benchmark de l'accélération C++")


def benchmark_database() -> dict[str, Any]:
    """Mesure l'impact des index SQL et du sharding."""
    # TODO: Comparer les requêtes SQL sans index vs avec index.
    # TODO: Comparer 1 base vs 3 bases (Sharding).
    raise NotImplementedError("TODO: implémenter le benchmark de la base de données")


def main() -> None:
    """Exécute tous les benchmarks et écrit les résultats dans ``data/``."""
    # TODO: Appeler les quatre benchmarks et sauvegarder les résultats.
    raise NotImplementedError("TODO: implémenter le point d'entrée des benchmarks")


if __name__ == "__main__":
    main()
