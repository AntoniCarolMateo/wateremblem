import pygame, sys 
from pygame.locals import *
from Map1 import *
from Player import *

pygame.init()

WHITE = [255, 255, 255]
BLACK = [0  , 0  , 0  ]
RED   = [255, 0, 0]
case  = 0


#GENERATING ALIES
Lyria   = Player('Liria',   'Sprites/lyn.png',    [0,6])
Pepa = Player('Pepa', "Sprites/lyn.png", [6,0])
listPLAYERS = [Lyria, Pepa]

# First player is default
PLAYER = listPLAYERS[0]
PLAYER_NAME = listPLAYERS[0].name
playerPos = listPLAYERS[0].position
facing = listPLAYERS[0].facing

new_coord = playerPos

Cursor = pygame.image.load('Sprites/cursor.png')
cursorPos = PLAYER.position


#WE BUILD THE SCREEN BASING IN OUR MAP DIMENSIONS
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))


while True:

	#Set initial mouse cord
	mouse_coord = [pygame.mouse.get_pos()[0]/TILESIZE, pygame.mouse.get_pos()[1]/TILESIZE]
	cursorPos = PLAYER.position


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	# Mouse inputs
		elif pygame.mouse.get_pressed()[0]:
				for player in listPLAYERS:
					if player.position == mouse_coord:
						PLAYER = player
						print(player.toString())


	#MOVECHARACTERS
		elif (event.type == KEYDOWN):
			if (event.key == K_RIGHT):
				player.move('RIGHT')
			elif (event.key ==K_UP):
				player.move('UP')
			elif (event.key == K_LEFT):
				player.move('LEFT')


				
			




	# Display map sprites
	for row in range(MAPWIDTH):
		for column in range(MAPHEIGHT):
			DISPLAYSURF.blit(textures[map[row][column]], (column*TILESIZE, row*TILESIZE))
	
	#RENDERING PLAYERS
	for player in listPLAYERS:
		DISPLAYSURF.blit(player.sprite,(player.position[0]*TILESIZE,player.position[1]*TILESIZE))

	pygame.display.update()