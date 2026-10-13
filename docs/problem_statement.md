# Problem Statement

## Contexte
Sur le marché tunisien de l'occasion, les prix varient fortement d'une annonce
à l'autre et évoluent avec le contexte économique.

## Utilisateurs et décision
- Acheteur : savoir si une annonce est surévaluée.
- Vendeur : fixer un prix réaliste.

## Objectif ML
Prédire le prix d'une voiture à partir de ses caractéristiques
(marque, modèle, année, kilométrage, carburant, boîte, région).

## Critères de succès
- Qualité : MAPE < 12 % sur un jeu de validation figé
- Service : latence API p95 < 200 ms
- MLOps : réentraînement automatique si dérive détectée, déploiement sans
  intervention manuelle, tout modèle reproductible (code + données + params)

## Risques
- Dérive des prix (inflation) / changement de structure des annonces
- Données bruitées (prix fantaisistes, doublons)
