-- 01_schema.sql
-- Structure des tables relationnelles.
--
-- Ce fichier ne contient volontairement aucune instruction DDL :
-- le schéma doit être écrit manuellement.

-- TODO: Créer la table 'pages'
-- Colonnes nécessaires : id (clé primaire), url (unique), domain (ex: 'gouv.bj'),
-- content_hash (empreinte SHA256 du texte pour détecter les doublons),
-- title, clean_text, doc_length (nombre de mots), status_code, crawled_at, pagerank (float).

-- TODO: Créer la table 'links' (le graphe orienté)
-- Colonnes nécessaires : source_id (référence pages.id), target_id (référence pages.id).
-- Clé primaire composite sur (source_id, target_id) pour éviter les doublons d'arêtes.

-- TODO: Créer la table 'inverted_index'
-- Colonnes nécessaires : word (texte), page_id (référence pages.id), term_freq (int : nombre d'apparitions).
-- Clé primaire sur (word, page_id).
