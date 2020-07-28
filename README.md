# Aidez MacGyver à s'échapper !


## Installation du jeu MacGyver

- Créez un environnement virtuel `python3 -m virtualenv env`
- Activez l'environnement virtuel `./env/bin/activate`
- Installez les dépendances `pip install -r requirements.txt`
- Démarrez le jeu `python3 game.py`

## Démarche

### Introduction

### Choix de l'algorithme


### Difficultés rencontrées et les solutions trouvées


#### Les fichiers
Voici la liste des fichiers du jeu disponible sur GitHub https://github.com/shequet/MacGyver


|  Fichier | Description  | Exemples  |
|---|---|---|
| constant.py  |  Permet de modifier la configuration du jeu | Nom du jeu, taille de la fenêtre, nombre d'objects etc.. |
| game.py      |  Fichier de démarrage du jeu | Démarrez le jeu `python3 game.py`|
| labyrinth.py |  Fichier de gestion du labyrinthe | Chargement du niveau, placement des images etc..|
| player.py    |  Fichier de gestion de MacGyver | Gestion des déplacement, collision etc..|
| score.py     |  Fichier de gestion du score | Gestion du score et affichage|
| treasure.py  |  Fichier de gestion des objects | Placement de manière aléatoire des objects dans le labyrinthe|
| README.md  |  Documentation du projet | |
| requirements.txt  |  Fichier contenant les dépendances du jeu| Pour les installer `pip install -r requirements.txt` |
| /level/level1.map  |  Fichier comportant le positionnement des éléments du niveau un du jeu | |
| /images/ether.png  |  Image de l'objet Ether que MacGyver doit collecter | |
| /images/guardian.png  |  Image du gardien que Macgyver doit atteindre | |
| /images/needle.png  |  Image de l'objet Aiguille que MacGyver doit collecter| |
| /images/path.png  |  Image du chemin ou MacGyver peut bouger| |
| /images/pipe.png  |  Image de l'objet Tube de pvc que MacGyver doit collecter | |
| /images/syringe.png  |  Image de l'objet seringue que MacGyver doit collecter | |
| /images/ether.png  |  Image de l'objet mur que MacGyver ne peut pas marcher | |




#### Carte
- Chargement du niveau depuis le fichier level/level1.map
- Ajout de manière aléatoire de trois objects dans les cases accessible par MacGyver

#### MacGyver :
- Déplacement de MacGyver dans les qautre directions (haut, droite, bas, gauche)
- Gestion des collisions entre MacGyver et les murs
- Gestion de la capture des objets par MacGyver et incrémentation du score






Documentation de PyGame : https://www.pygame.org/docs/