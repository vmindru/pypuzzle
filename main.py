#!/usr/bin/python

import pygame

screen_x=640
screen_y=480
pygame.init()
screen = pygame.display.set_mode((screen_x, screen_y))


class Game(object):
	def main(self, screen):

		self.running = 1
		self.puzzle_image = pygame.image.load('tux.png')
		self.puzzle_image = pygame.transform.scale(self.puzzle_image,(screen_x,screen_y))
		self.clock = pygame.time.Clock()
		self.pos_x = 0
		self.pos_y = 0
		print self.pos_x
		print self.pos_y
		self.main_while()

	def main_while(self):
		while self.running:
			self.clock.tick(30)
			self.event_handler()
			screen.fill((200, 200, 200))
			screen.blit(self.puzzle_image, (self.pos_x, self.pos_y))
			pygame.display.flip()
	
	def event_handler(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = 0
				return
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				self.running = 0
				return

if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode((640, 480))
	Game().main(screen)
