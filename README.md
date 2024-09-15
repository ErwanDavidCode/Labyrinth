# Presentation
This Python project generates a random maze and solves it very quickly and efficiently.

# Installation
- Install Python libraries
```sh
pip install -r requirements.txt
```

# Algorithm configuration
The internal values used for the algorithm can be modified in the `labyrinthe_resolution.py` file.
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
|largeur|int|Maze width in number of squares|
|hauteur|int|Maze height in number of squares|
|ligne_entree|int|x<sub>entry</sub>|
|colonne_entree|int|y<sub>entry</sub>|
|ligne_sortie|int|x<sub>exit</sub>|
|colonne_sortie|int|y<sub>exit</sub>|
|pas|int|The step size of the maze generation random walk|
|pad_width|str|The size of the outer contour of the labyrinth|

**Notes**: All values must be modified with full knowledge of the facts. Values are not checked for consistency.
For example: the values _ligne_entree_, _colonne_entree_, _ligne_sortie_, _colonne_sortie_ must be smaller than the size of the maze.

# Examples
Here's an image of a maze, with its solution, generated with this code in less than a second:
![Screenshot of a labyrinth](/pictures/labyrinth01.png)