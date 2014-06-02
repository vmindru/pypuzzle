#!/usr/bin/python

import pygame

screen_x=640
screen_y=480
pygame.init()
screen = pygame.display.set_mode((screen_x, screen_y))


class Game(object):
	def main(self, screen):

		image_x = 120
		image_y = 240
		image = pygame.image.load('apple.png')
		clock = pygame.time.Clock()

		while 1:
			clock.tick(30)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
				if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
					return
			screen.fill((200, 200, 200))
			print "spwaning at %i %i" % (image_x, image_y)
			screen.blit(image, (image_x, image_y))
			pygame.display.flip()

class Draw(Game):
	pass



if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode((640, 480))
	Draw().main(screen)
