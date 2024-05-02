# Iris Species Prediction

Ce projet est une application de prédiction des espèces d'iris, composée d'un backend et d'un frontend, permettant aux utilisateurs de prédire l'espèce d'iris en fonction de ses caractéristiques.

## Structure du Projet

- `src/backend`: Contient le code source du backend.
- `src/frontend`: Contient le code source du frontend.
- `compose.yaml`: Fichier de configuration Docker Compose pour exécuter les services backend et frontend ensemble.

## Configuration et Exécution

### Prérequis

Assurez-vous d'avoir Docker et Docker Compose installés sur votre système.

### Exécution avec Docker Compose

1. À la racine du projet, exécutez la commande suivante pour démarrer les services backend et frontend :

    ```bash
    docker-compose up
    ```

Cela va construire les images Docker nécessaires et démarrer les conteneurs pour le backend et le frontend.

## Utilisation

Une fois que les services backend et frontend sont en cours d'exécution, ouvrez votre navigateur et accédez à l'URL suivante :

- Frontend : http://localhost:8504

Vous serez accueilli par une interface utilisateur où vous pourrez définir les caractéristiques de l'iris à prédire à l'aide des curseurs. Une fois que vous avez défini les caractéristiques, vous obtiendrez le résultat de la prédiction.

Si aucune prediction n'apparait, aucun modèle n'est présent dans votre système. Rendez-vous sur la page "Retrain model" et cliquez sur le bouton "Re-Train Model".

Vous pouvez également accéder au backend directement à l'URL suivante :
- Backend : http://localhost:8084/docs

## Auteurs

- Louis Gabilly - Data Scientist
