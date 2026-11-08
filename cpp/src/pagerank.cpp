#include "pagerank.hpp"

#include <stdexcept>

namespace rankwell {

PageRankResult compute_pagerank_parallel(
    const CSRMatrix& matrix,
    double damping,
    double tol,
    int max_iter,
    int num_threads) {
    (void)matrix;
    (void)damping;
    (void)tol;
    (void)max_iter;
    (void)num_threads;
    // TODO: Initialiser le vecteur de scores à 1/N.
    // TODO: Paralléliser la somme des pages sans lien sortant (réduction).
    // TODO: Paralléliser le produit matrice creuse x vecteur sur les lignes.
    // TODO: Calculer l'erreur L1 et s'arrêter sous la tolérance.
    // TODO: Mesurer la durée avec <chrono>.
    throw std::logic_error("TODO: implémenter le PageRank parallèle");
}

}  // namespace rankwell
