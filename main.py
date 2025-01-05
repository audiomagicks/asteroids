import pygame # type: ignore
from constants import *
from player import *
from asteroidfield import *
from shot import *
def main():
	pygame.init()
	clock = pygame.time.Clock()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	Asteroid.containers = (asteroids, updatable, drawable)
	Player.containers = (updatable, drawable)
	AsteroidField.containers = updatable
	Shot.containers = (shots, updatable, drawable)

	player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
	asteroidfield = AsteroidField()

	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		screen.fill((0, 0, 0))
		
		for object in updatable:
			object.update(dt)

		for object in asteroids:
			if object.collision(player):
				print("Game over!")
				exit()

		for object in drawable:
			object.draw(screen)
			
		pygame.display.flip()

		dt = clock.tick(60) / 1000
		

if __name__ == "__main__":
	main()
