"""PageRank en Python.

Algorithmes itératifs matriciels : Power Iteration, Jacobi et
mesures de mémoire.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import numpy as np
    from scipy.sparse import csr_matrix


class PageRankPython:
    """Algorithmes itératifs matriciels pour le calcul du PageRank."""

    def power_iteration(
        self,
        matrix_csr: csr_matrix,
        damping: float = 0.85,
        tol: float = 1e-6,
        max_iter: int = 200,
    ) -> tuple[np.ndarray, list[float]]:
        """Calcule le PageRank par la méthode des puissances.

        Formule visée :
        ``r^(k+1) = d * P^T * r^(k) + (d * masse_puisards / N) + (1 - d) / N``

        Args:
            matrix_csr: Matrice de transition creuse au format CSR.
            damping: Facteur d'amortissement ``d``.
            tol: Seuil d'arrêt sur la norme L1 de la différence.
            max_iter: Nombre maximal d'itérations.

        Returns:
            Un couple ``(scores, errors)`` contenant le vecteur final et
            l'historique des erreurs pour les graphiques de convergence.
        """
        # TODO: 1. Initialiser le vecteur de scores r avec 1/N partout.
        # TODO: 2. Calculer la masse perdue dans les dangling nodes à chaque itération.
        # TODO: 3. Faire le produit matrice-vecteur creux et ajouter la téléportation.
        # TODO: 4. Calculer ||r^(k+1) - r^(k)||_1 et l'ajouter dans 'errors'.
        # TODO: 5. S'arrêter quand l'erreur < tol et retourner (scores, errors).
        raise NotImplementedError("TODO: implémenter Power Iteration")

    def jacobi_method(
        self,
        matrix_csr: csr_matrix,
        damping: float = 0.85,
        tol: float = 1e-6,
        max_iter: int = 200,
    ) -> tuple[np.ndarray, list[float]]:
        """Calcule le PageRank en résolvant le système linéaire par Jacobi.

        Phase 4 : résout ``(I - d * P^T) * r = ((1 - d) / N) * 1``.

        Args:
            matrix_csr: Matrice de transition creuse au format CSR.
            damping: Facteur d'amortissement ``d``.
            tol: Seuil d'arrêt sur la norme L1 de la différence.
            max_iter: Nombre maximal d'itérations.

        Returns:
            Un couple ``(scores, errors)`` pour comparer la convergence avec
            Power Iteration.
        """
        # TODO: Implémenter Jacobi et retourner (scores, errors).
        raise NotImplementedError("TODO: implémenter la méthode de Jacobi")

    def compare_memory_sparse_vs_dense(self, matrix_csr: csr_matrix) -> dict[str, int]:
        """Compare la mémoire occupée par une matrice CSR et une matrice pleine.

        Phase 4.

        Args:
            matrix_csr: Matrice creuse à mesurer.

        Returns:
            Dictionnaire contenant au minimum ``sparse_bytes`` et
            ``dense_bytes``.
        """
        # TODO: Calculer data + indices + indptr pour la CSR.
        # TODO: Calculer N * N * 8 octets pour la matrice dense NumPy.
        raise NotImplementedError("TODO: comparer la mémoire CSR et dense")
