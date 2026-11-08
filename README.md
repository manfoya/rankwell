# RankWell

Moteur de recherche : crawler web, stockage PostgreSQL, index inversé,
PageRank et interface web.

> **État actuel : squelette uniquement.** Les signatures, docstrings et TODO
> sont en place, mais aucun algorithme n'est encore implémenté.

## Modules

| Dossier | Rôle |
|---|---|
| `src/engine/crawler/` | Bloom, frontière, fetcher, parser, worker |
| `src/engine/db/` | Connexions, sharding, requêtes SQL |
| `src/engine/indexer/` | Tokenizer et index inversé |
| `src/engine/graph/` | CSR, PageRank Python, pont C++, analyse |
| `src/engine/search/` | BM25 et fusion avec PageRank |
| `src/engine/web/` | Interface Flask sans JavaScript |
| `cpp/` | PageRank parallèle en C++ |

## Prérequis

- Python 3.11 ou plus récent
- [uv](https://docs.astral.sh/uv/) pour l'environnement Python
- Docker et Docker Compose pour PostgreSQL
- CMake 3.20+ et un compilateur C++20 pour la partie C++

## Installation

```bash
cp .env.example .env
make sync          # uv sync --extra dev
make up            # démarre db_main, db_shard_1 et db_shard_2
```

Les fichiers `sql/*.sql` ne contiennent volontairement que des TODO : les
bases démarrent donc sans tables tant que le schéma n'est pas écrit.

## Commandes utiles

```bash
make help          # liste des cibles
make test          # pytest
make lint          # ruff check
make fmt           # ruff format
make build-cpp     # configure et compile build/pagerank_cpp
make crawl         # squelette du crawler
make index         # squelette de l'indexation
make pagerank      # squelette du PageRank
make run-web       # squelette de l'interface Flask
make down          # arrête les bases
make reset         # supprime aussi les volumes PostgreSQL
```

## Structure

```text
rankwell/
├── sql/            # schéma et index PostgreSQL (TODO)
├── src/engine/     # code Python du moteur
├── cpp/            # accélérateur C++ (stubs)
├── scripts/        # CLI et benchmarks
├── tests/          # tests unitaires (skip tant que non implémentés)
└── data/           # exports de graphes et scores (ignoré par git)
```

## Configuration

Toutes les valeurs sont centralisées dans `src/engine/config.py` et lues depuis
l'environnement. Les variables disponibles sont documentées dans `.env.example`.

## Prochaines étapes

1. Écrire `sql/01_schema.sql` et `sql/02_indexes.sql`.
2. Implémenter le filtre de Bloom, la frontière et le tokenizer.
3. Construire le graphe CSR, puis PageRank en Python.
4. Ajouter BM25 et la fusion avec PageRank.
5. Comparer avec NetworkX, puis accélérer en C++.
