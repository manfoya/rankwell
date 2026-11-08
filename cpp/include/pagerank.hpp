#pragma once

#include <vector>

#include "csr_matrix.hpp"

namespace rankwell {

/// Résultat d'un calcul de PageRank.
struct PageRankResult {
    std::vector<double> scores;
    int iterations{0};
    double error{0.0};
    double elapsed_ms{0.0};
};

/// Calcule le PageRank en parallèle.
///
/// Power Iteration avec produit matrice creuse x vecteur
/// parallélisé sur les lignes et réduction pour les dangling nodes.
///
/// \param matrix Graphe au format CSR.
/// \param damping Facteur d'amortissement (typiquement 0.85).
/// \param tol Seuil d'arrêt sur la norme L1.
/// \param max_iter Nombre maximal d'itérations.
/// \param num_threads Nombre de threads à utiliser.
/// \return Scores, nombre d'itérations, erreur finale et durée en millisecondes.
PageRankResult compute_pagerank_parallel(
    const CSRMatrix& matrix,
    double damping,
    double tol,
    int max_iter,
    int num_threads);

}  // namespace rankwell
