import pygame, sys
from pygame.locals import *
from time import *
from Map1 import *


class Player:

	def __init__(self, name, image, position):
		self.name = name
		self.sprite = pygame.image.load(image)
		self.position = position
		self.facing = 'UP'
		self.hp = 12
		self.action_made = False

	#TODO : IMPLEMENTAR TOTS ELS MOVIMENTS
	def move(self, dir):
		if dir == 'RIGHT':
			self.facing = dir
			increment = 1
			new_coord = [self.position[0]+1, self.position[1]]
			if new_coord[0] not in range(MAPWIDTH):
				increment = 0
			else:
				if new_coord == self.position:
					increment = 0			
			self.position[0]  += increment
			self.action_made = True
		if dir == 'LEFT':
			self.facing = dir
			increment = 1
			new_coord = [self.position[0]-1, self.position[1]]
			if new_coord[0] not in range(MAPWIDTH):
				increment = 0
			else:
				if new_coord == self.position:
					increment = 0			
			self.position[0]  -= increment
			self.action_made = True
		elif dir == 'UP':
			self.facing = dir
			increment = 1
			new_coord = [self.position[0], self.position[1]-1]
			if new_coord[1] not in range(MAPHEIGHT):
				increment = 0
			else:
				if new_coord == self.position:
					increment = 0
			self.position[1] -= increment
			self.action_made = True
		elif dir == 'DOWN':
			self.facing = dir
			increment = 1
			new_coord = [self.position[0], self.position[1]+1]
			if new_coord[1] not in range(MAPHEIGHT):
				increment = 0
			else:
				if new_coord == self.position:
					increment = 0
			self.position[1] += increment
			self.action_made = True

		



	def toString(self):
		return "Player : " + self.name + ", position :" + format(self.position) + \
				", facing to : " + self.facing + "."
		
			



	