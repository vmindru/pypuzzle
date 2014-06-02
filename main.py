#!/usr/bin/python

import pygame

screen_x=640
screen_y=480
pygame.init()
screen = pygame.display.set_mode((screen_x, screen_y))


class Game(object):
	def main(self, screen):

		image = pygame.image.load('tux.png')
		clock = pygame.time.Clock()
		
		pos_x = 0
		pos_y = 0
		print self.position()

		
		while 1:
			clock.tick(30)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
				if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
					return
			screen.fill((200, 200, 200))
			screen.blit(image, (pos_x, pos_y))
			pygame.display.flip()
	
	def position(self):
		super(
		return (self.pos_x,self.pos_y)

class Draw(Game):
	pass




if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode((640, 480))
	Draw().main(screen)
