import pygame
from Player import *
from random import randrange



class Combat():

	def __init__(self, player, enemy):

		self.player = player
		self.enemy = enemy

	def encounter(self):
		string = ""
		random_player = randrange(10)
		random_enemy = randrange(10)


		if random_player > random_enemy:
			self.enemy.hp -= 2
			string += "Player has won the battle!"
		else:
			self.player.hp -= 2
			string = "Enemy won the battle :("

		return string


			
