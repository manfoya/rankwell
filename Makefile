.DEFAULT_GOAL := help

COMPOSE := docker compose
UV := uv
POSTGRES_USER ?= rankwell
POSTGRES_DB ?= rankwell

.PHONY: help sync up down reset logs psql test lint fmt build-cpp crawl index pagerank run-web clean

help: ## Affiche cette aide
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-14s\033[0m %s\n", $$1, $$2}'

sync: ## Installe les dépendances Python avec uv
	$(UV) sync --extra dev

up: ## Démarre les trois bases PostgreSQL
	$(COMPOSE) up -d

down: ## Arrête les bases sans supprimer les volumes
	$(COMPOSE) down

reset: ## Arrête les bases et supprime leurs données
	$(COMPOSE) down -v

logs: ## Suit les logs PostgreSQL
	$(COMPOSE) logs -f

psql: ## Ouvre psql sur la base principale
	$(COMPOSE) exec db_main psql -U $(POSTGRES_USER) -d $(POSTGRES_DB)

test: ## Lance pytest
	$(UV) run pytest

lint: ## Vérifie le style et les erreurs statiques
	$(UV) run ruff check .

fmt: ## Formate le code Python
	$(UV) run ruff format .

build-cpp: ## Configure et compile l'exécutable C++
	cmake -S . -B build
	cmake --build build -j

crawl: ## Lance le crawler (squelette)
	$(UV) run python scripts/run_crawl.py

index: ## Construit l'index inversé (squelette)
	$(UV) run python scripts/build_index.py

pagerank: ## Calcule le PageRank (squelette)
	$(UV) run python scripts/run_pagerank.py

run-web: ## Lance l'interface web Flask (squelette)
	$(UV) run flask --app "engine.web.app:create_app" run --debug

clean: ## Supprime les artefacts locaux
	rm -rf build .pytest_cache .ruff_cache .coverage htmlcov
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
