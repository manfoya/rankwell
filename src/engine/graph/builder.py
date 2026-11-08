"""Construction de la matrice creuse du graphe web.

Transforme les arêtes SQL en matrice CSR exploitable par
Python et par l'exécutable C++.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from scipy.sparse import csr_matrix

    from engine.db.repository import PageRepository


class GraphBuilder:
    """Transforme les liens de la BDD en matrice creuse CSR."""

    def __init__(self, repository: PageRepository) -> None:
        """Reçoit le dépôt utilisé pour lire les arêtes du graphe.

        Args:
            repository: Accès à la table ``links`` et aux pages.
        """
        raise NotImplementedError("TODO: mémoriser le dépôt du graphe")

    def build_csr_matrix(self) -> tuple[csr_matrix, dict[int, int]]:
        """Construit la matrice de transition du graphe.

        Returns:
            Un couple ``(matrix, page_index)`` où ``matrix`` est la matrice
            creuse CSR et ``page_index`` associe chaque ``page_id`` SQL à son
            indice ``0..N-1`` dans la matrice.
        """
        # TODO: Récupérer les liens depuis la BDD.
        # TODO: Créer la table de correspondance page_id_sql <-> index 0..N-1.
        # TODO: Construire la matrice de transition creuse (scipy.sparse.csr_matrix).
        # TODO: Identifier les dangling nodes (pages sans lien sortant).
        raise NotImplementedError("TODO: construire la matrice CSR")

    def export_for_cpp(self, filepath: str) -> None:
        """Exporte le graphe dans un fichier lisible par le programme C++.

        Args:
            filepath: Chemin du fichier binaire à écrire.
        """
        # TODO: (Phase 4) Écrire num_nodes, indptr, indices, data et out_degree.
        # TODO: Documenter le format choisi pour que le C++ puisse le relire.
        raise NotImplementedError("TODO: exporter le graphe pour le C++")
