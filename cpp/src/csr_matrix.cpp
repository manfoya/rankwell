#include "csr_matrix.hpp"

#include <stdexcept>

namespace rankwell {

CSRMatrix load_csr_matrix(const std::string& filepath) {
    (void)filepath;
    // TODO: Ouvrir le fichier en binaire.
    // TODO: Lire num_nodes, indptr, indices, data et out_degree.
    // TODO: Vérifier la cohérence des tailles et lever std::runtime_error sinon.
    throw std::logic_error("TODO: charger la matrice CSR depuis un fichier");
}

}  // namespace rankwell
