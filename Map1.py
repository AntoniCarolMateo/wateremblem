import pygame, sys

GRASS = 0

terrains = {
	0 : 'GRASS'
	
}
textures = {
	GRASS : pygame.image.load('Texturas/grass.png')
}
#MAPA BASED ON MATRIX; GRID TYPE MAP
map = [
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0]
	]


# Game Dimensions
TILESIZE = 32
MAPWIDTH = 7
MAPHEIGHT = 7