#pragma once

#include <string>
#include <vector>

namespace rankwell {

/// Matrice creuse au format CSR (Compressed Sparse Row).
///
/// Cette structure est remplie à partir du fichier
/// binaire exporté par `GraphBuilder.export_for_cpp`.
struct CSRMatrix {
    int num_nodes{0};
    std::vector<int> indptr;
    std::vector<int> indices;
    std::vector<double> data;
    std::vector<int> out_degree;
};

/// Charge une matrice CSR depuis le fichier exporté par Python.
///
/// \param filepath Chemin du fichier binaire.
/// \return La matrice chargée.
/// \throws std::runtime_error Si le fichier est absent ou invalide.
CSRMatrix load_csr_matrix(const std::string& filepath);

}  // namespace rankwell
