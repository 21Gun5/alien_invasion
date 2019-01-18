import sys
import pygame

class Panda:
	def __init__(self, screen):
		self.screen = screen
		self.image = pygame.image.load("panda.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery

	def blitme(self):
		self.screen.blit(self.image, self.rect)



def run_game():
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	pygame.display.set_caption("just 4 try")
	panda = Panda(screen)
	while True:
		screen.fill((255,255,255))
		panda.blitme()
		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

run_game()