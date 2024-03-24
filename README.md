# Presentation
Ce projet en Python génère un labyrinthe aléatoire et le résout de manière très rapide et efficace.

# Installation
- Installer les librairies Python
```sh
pip install -r requirements.txt
```

# Configuration de l'algorithme
Les valeurs internes utilisées pour l'algorithme peuvent être modifiés dans le fichier `labyrinthe_resolution.py`.
```python
carte = labyrinthe(
    largeur=101,
    hauteur=101, 
    ligne_entree="auto", 
    colonne_entree="auto", 
    ligne_sortie="auto", 
    colonne_sortie="auto", 
    pas=2, 
    pad_width=1)
```

|argument|type|description|
|-|-|-|
|largeur|int|La largeur du labyrinthe en nombre de cases|
|hauteur|int|La hauteur du labyrinthe en nombre de cases|
|ligne_entree|int|x<sub>entrée</sub>|
|colonne_entree|int|y<sub>entrée</sub>|
|ligne_sortie|int|x<sub>sortie</sub>|
|colonne_sortie|int|y<sub>sortie</sub>|
|pas|int|La taille du pas de la marche aléaoire de génération du labyrinthe|
|pad_width|str|La taille du contour extérieur du labyrinthe|


**Remarques** : Toutes les valeurs doivente être modifiées en connaissance de cause. Aucune vérification n'est effectuée sur la cohérence des valeurs.
Par exemple : les valeurs _ligne_entree_, _colonne_entree_, _ligne_sortie_, _colonne_sortie_ doivent être inférieure à la taille du labyrinthe.

# Exemples
Voici une image de labyrinthe, avec sa solution, généré grâce à ce code en moins d'une seconde :
![Screenshot of a labyrinth](/pictures/labyrinth01.png)