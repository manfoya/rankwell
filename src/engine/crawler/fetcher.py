"""Téléchargement HTTP poli et respect de ``robots.txt``.

Le crawler doit s'identifier clairement et limiter sa charge.
"""

from __future__ import annotations


class PoliteFetcher:
    """Télécharge les pages web en respectant les règles éthiques du crawl."""

    def __init__(self, user_agent: str, delay_seconds: float = 1.0) -> None:
        """Prépare le client HTTP et les caches nécessaires.

        Args:
            user_agent: Chaîne envoyée dans l'en-tête ``User-Agent``.
            delay_seconds: Délai minimal entre deux requêtes vers un même domaine.
        """
        # TODO: Stocker le user_agent et le délai.
        # TODO: Mémoriser l'heure de la dernière requête par domaine.
        # TODO: Prévoir un cache des fichiers robots.txt déjà lus (urllib.robotparser).
        raise NotImplementedError("TODO: initialiser le fetcher poli")

    def can_fetch(self, url: str) -> bool:
        """Vérifie si ``robots.txt`` autorise l'exploration de ``url``.

        Args:
            url: URL absolue à tester.

        Returns:
            ``True`` si l'URL est autorisée pour le User-Agent courant.
        """
        # TODO: Télécharger et lire robots.txt du domaine s'il n'est pas en cache.
        # TODO: Vérifier l'autorisation avec urllib.robotparser.RobotFileParser.
        raise NotImplementedError("TODO: vérifier robots.txt")

    def fetch(self, url: str) -> tuple[int, str | None]:
        """Télécharge une page de manière polie.

        Args:
            url: URL absolue à télécharger.

        Returns:
            Un couple ``(status_code, html)``. ``html`` vaut ``None`` si la
            page n'est pas autorisée ou si le téléchargement échoue.
        """
        # TODO: 1. Vérifier can_fetch(url).
        # TODO: 2. Attendre si la dernière requête sur ce domaine est trop récente.
        # TODO: 3. Faire la requête HTTP avec le User-Agent et un timeout.
        # TODO: 4. Retourner (status_code, html_content).
        raise NotImplementedError("TODO: télécharger une page")
