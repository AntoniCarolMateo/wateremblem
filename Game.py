import pygame, sys 
from pygame.locals import *
from Map1 import *
from Player import *
from PlayerInfo import *
from Combat import *

pygame.init()

WHITE = [255, 255, 255]
BLACK = [0  , 0  , 0  ]
RED   = [255, 0, 0]
case  = 0


#GENERATING ALIES
Lyria   = Player('Liria',   'Sprites/lyn.png',    [0,0])
listPLAYERS = [Lyria]

ezequiel = Player('Ezequiel', 'Sprites/mage.png', [0,6])
enemies = [ezequiel]


combat_log = ""

# First player is default
PLAYER = listPLAYERS[0]
PLAYER_NAME = listPLAYERS[0].name
playerPos = listPLAYERS[0].position
facing = listPLAYERS[0].facing

new_coord = playerPos

Cursor = pygame.image.load('Sprites/cursor.png')
cursorPos = PLAYER.position

Debug = True
#WE BUILD THE SCREEN BASING IN OUR MAP DIMENSIONS

if Debug:
	const = 120
	INVFONT = pygame.font.SysFont('FreeSans.tff',18)
else:
	cont = 0

DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE+const))

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
				for enemy in enemies:
					if enemy.position == player.position:
						battle = Combat(player, enemy)
						result = battle.encounter()
						print(result)
			elif (event.key ==K_UP):
				player.move('UP')
			elif (event.key == K_LEFT):
				player.move('LEFT')
			elif (event.key == K_DOWN):
				player.move('DOWN')
				for enemy in enemies:
					if enemy.position == player.position:
						battle = Combat(player, enemy)
						combat_log = battle.encounter()
						print(str(player.hp) + "    " + str(enemy.hp))
						



	# Display map sprites
	for row in range(MAPWIDTH):
		for column in range(MAPHEIGHT):
			DISPLAYSURF.blit(textures[map[row][column]], (column*TILESIZE, row*TILESIZE))
	
	#RENDERING PLAYERS
	for player in listPLAYERS:
		DISPLAYSURF.blit(player.sprite,(player.position[0]*TILESIZE,player.position[1]*TILESIZE))

	for enemy in enemies:
		DISPLAYSURF.blit(enemy.sprite,(enemy.position[0]*TILESIZE,enemy.position[1]*TILESIZE))
	


	if Debug:
		#player info
		radius = 40
		placePosition = 5

		playerImage = pygame.draw.circle(DISPLAYSURF,WHITE,(MAPWIDTH*TILESIZE-radius,0 + radius), radius, 5)
		
		Text_Char_Selected= INVFONT.render('Currently Selected: ' + PLAYER.name + '        ', True, WHITE, BLACK)
		DISPLAYSURF.blit(Text_Char_Selected,(placePosition, MAPHEIGHT*TILESIZE))

		current_terrain = terrains[map[PLAYER.position[1]][PLAYER.position[0]]]
		Text_Terrain = INVFONT.render('Terrain: ' + str(current_terrain) + (9*'  '), True, WHITE, BLACK)
		DISPLAYSURF.blit(Text_Terrain,(placePosition, MAPHEIGHT*TILESIZE+10))

		Combat_Log = INVFONT.render(combat_log,True, WHITE, BLACK)
		DISPLAYSURF.blit(Combat_Log,(placePosition, MAPHEIGHT*TILESIZE+50))


	pygame.display.update()