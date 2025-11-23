# UE19-LAB-05 : generateur de blagues 

Ce projet est une simple application Python 3 qui utilise la librairie `requests` pour interroger l'API JokesAPI (https://v2.jokeapi.dev/) et afficher une blague aléatoire en français.



# Comment le lancer (Localement)

1.  **Clonez le dépôt :**
    ```bash
    git clone [https://github.com/](https://github.com/)[VOTRE_NOM_UTILISATEUR]/ue19-lab-05.git
    cd ue19-lab-05
    ```

2.  **Installez les dépendances :**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Exécutez le script :**
    ```bash
    python3 app.py
    ```

#Comment le lancer (avec Docker)

1.  **Construisez l'image Docker :**
    (Assurez-vous d'être à la racine du projet)
    ```bash
    docker build -t blague-app .
    ```

2.  **Exécutez l'application dans un conteneur :**
    ```bash
    docker run --rm blague-app
    ```
