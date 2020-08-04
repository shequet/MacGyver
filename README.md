# Aidez MacGyver à s'échapper !
Voici la présentation du Projet 3 de la formation Développeur d'application - Python

## Installation et exécution du jeu

#### Pré requis
Le jeu fonctionne sous Windows, Mac et linux, cependant il est nécessaire d'avoir installé Python 3.

#### Installation
- Il est préférable de créer un environnement virtuel `python3 -m virtualenv env`
- Activez votre environnement virtuel `./env/bin/activate`
- Installez les dépendances `pip install -r requirements.txt`

#### Paramétrage du jeu

Le jeu est paramétrable via un fichier de Python constant.py, il est possible de modifier les éléments suivants :

|  Variable | Description  | Exemples  |
|---|---|---|
| DISPLAY_GAME_TITLE  |  Titre du jeu dans la fenêtre | MacGyver Game |
| DISPLAY_MODE  |  Taille du jeu en pixel [x, y] | [480, 480] |
| TILE_HEIGHT  | Hauteur des images en pixel | 32 |
| TILE_WIDTH  |  Largeur des images en pixel | 32 |
| ITEM_TOTAL  |  Nombre d'objet à collecter| 3 |

#### Les fichiers
Voici la liste des fichiers du jeu disponible sur GitHub https://github.com/shequet/MacGyver

|  Fichier | Description  | Exemples  |
|---|---|---|
| constant.py  |  Permet de modifier la configuration du jeu | Nom du jeu, taille de la fenêtre, nombre d'objects etc.. |
| game.py      |  Fichier de démarrage du jeu | Démarrez le jeu `python3 game.py`|
| labyrinth.py |  Fichier de gestion du labyrinthe | Chargement du niveau, placement des images etc..|
| player.py    |  Fichier de gestion de MacGyver | Gestion des déplacement, collision etc..|
| score.py     |  Fichier de gestion du score | Gestion du score et affichage|
| item.py  |  Fichier de gestion des objects | Placement de manière aléatoire des objects dans le labyrinthe|
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
