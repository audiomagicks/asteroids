import pygame
from constants import *
from player import *
def main():
	pygame.init()
	clock = pygame.time.Clock()
	player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0, 0, 0))
		player.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
if __name__ == "__main__":
	main()
