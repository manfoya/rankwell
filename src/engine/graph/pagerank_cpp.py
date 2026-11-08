"""Pont Python vers l'exécutable C++ de PageRank.

Exporte le graphe, lance le binaire et relit les scores.
"""

from __future__ import annotations


class PageRankCppBridge:
    """Appelle l'exécutable C++ compilé et récupère ses résultats."""

    def __init__(self, executable_path: str = "./build/pagerank_cpp") -> None:
        """Mémorise le chemin de l'exécutable C++.

        Args:
            executable_path: Chemin du binaire produit par CMake.
        """
        raise NotImplementedError("TODO: mémoriser le chemin de l'exécutable")

    def run_cpp_pagerank(
        self,
        graph_file: str,
        output_file: str,
        num_threads: int = 4,
    ) -> tuple[list[float], float]:
        """Exécute le PageRank C++ sur un graphe exporté.

        Args:
            graph_file: Fichier binaire produit par ``GraphBuilder.export_for_cpp``.
            output_file: Fichier où le C++ écrit les scores.
            num_threads: Nombre de threads demandé au binaire.

        Returns:
            Un couple ``(scores, temps_execution)`` où le temps est exprimé
            en millisecondes.
        """
        # TODO: Lancer subprocess.run([...]) avec les bons arguments.
        # TODO: Vérifier le code retour et lever une erreur explicite en cas d'échec.
        # TODO: Relire output_file et retourner (scores, temps_execution).
        raise NotImplementedError("TODO: appeler l'exécutable C++")
