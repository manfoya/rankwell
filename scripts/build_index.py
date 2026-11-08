"""Point d'entrée CLI de construction de l'index inversé.

Exemple d'utilisation future :
    python scripts/build_index.py
"""

from __future__ import annotations


def main() -> None:
    """Construit l'index inversé à partir des pages stockées en base."""
    # TODO: Charger la configuration avec engine.config.load_settings().
    # TODO: Construire DatabaseRouter et PageRepository.
    # TODO: Instancier Tokenizer puis InvertedIndexBuilder.
    # TODO: Appeler build_index_for_all_pages().
    raise NotImplementedError("TODO: implémenter le point d'entrée de l'indexation")


if __name__ == "__main__":
    main()
