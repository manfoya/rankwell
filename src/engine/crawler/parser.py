"""Extraction du texte, des liens et normalisation des URLs.

Le parser transforme le HTML brut en données exploitables.
"""

from __future__ import annotations

from typing import Any


class HTMLParser:
    """Extrait le texte propre et les liens d'une page HTML."""

    def normalize_url(self, base_url: str, link: str) -> str | None:
        """Convertit un lien trouvé dans une page en URL absolue normalisée.

        Args:
            base_url: URL de la page contenant le lien.
            link: Valeur brute de l'attribut ``href``.

        Returns:
            L'URL absolue normalisée, ou ``None`` si le lien doit être ignoré
            (``mailto:``, ``javascript:``, schéma non HTTP, etc.).
        """
        # TODO: Convertir un lien relatif en absolu avec urllib.parse.urljoin.
        # TODO: Supprimer le fragment (#section) et normaliser le schéma/hôte en minuscule.
        # TODO: Filtrer les liens non-HTTP et les URLs vides.
        raise NotImplementedError("TODO: normaliser une URL")

    def parse(self, base_url: str, html: str) -> dict[str, Any]:
        """Analyse une page HTML.

        Args:
            base_url: URL de la page, utilisée pour résoudre les liens relatifs.
            html: Contenu HTML brut.

        Returns:
            Dictionnaire contenant au minimum :
            ``title`` (str), ``text`` (str), ``content_hash`` (str) et
            ``links`` (list[str]).
        """
        # TODO: Utiliser BeautifulSoup pour extraire le <title>.
        # TODO: Supprimer <script> et <style>, puis extraire le texte propre.
        # TODO: Calculer le hash SHA-256 du texte propre.
        # TODO: Extraire et normaliser tous les liens <a href="...">.
        raise NotImplementedError("TODO: analyser une page HTML")
