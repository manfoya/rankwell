"""Filtre de Bloom maison.

Structure probabiliste permettant de savoir si un élément a
"probablement déjà été vu", sans jamais produire de faux négatifs.
"""

from __future__ import annotations


class BloomFilter:
    """Filtre de Bloom fait maison avec un tableau de bits et k fonctions de hachage."""

    def __init__(self, expected_items: int, false_positive_rate: float = 0.01) -> None:
        """Prépare un filtre dimensionné pour un nombre d'éléments attendu.

        Args:
            expected_items: Nombre ``n`` d'éléments qui seront ajoutés.
            false_positive_rate: Probabilité ``p`` de faux positif souhaitée.
        """
        # TODO: Calculer la taille optimale du tableau de bits :
        #       m = - (n * ln(p)) / (ln(2)^2)
        # TODO: Calculer le nombre de fonctions de hachage :
        #       k = (m / n) * ln(2)
        # TODO: Initialiser un tableau de bits (par exemple bytearray) à zéro.
        raise NotImplementedError("TODO: dimensionner et allouer le filtre de Bloom")

    def _get_hash_positions(self, item: str) -> list[int]:
        """Génère les ``k`` positions de bits associées à ``item``.

        Args:
            item: Chaîne à hacher (URL, empreinte de contenu, etc.).

        Returns:
            Liste de ``k`` indices dans le tableau de bits.
        """
        # TODO: Combiner plusieurs hachages (par exemple hashlib) pour obtenir k positions.
        raise NotImplementedError("TODO: calculer les positions de hachage")

    def add(self, item: str) -> None:
        """Ajoute ``item`` au filtre.

        Args:
            item: Chaîne à marquer comme vue.
        """
        # TODO: Mettre à 1 les k bits correspondant aux positions de 'item'.
        raise NotImplementedError("TODO: ajouter un élément au filtre")

    def might_contain(self, item: str) -> bool:
        """Teste la présence probable de ``item``.

        Args:
            item: Chaîne à tester.

        Returns:
            ``True`` si tous les k bits sont à 1, sinon ``False``. Un ``False``
            est garanti : l'élément n'a jamais été ajouté.
        """
        # TODO: Retourner True si TOUS les k bits sont à 1, sinon False.
        raise NotImplementedError("TODO: tester la présence d'un élément")
