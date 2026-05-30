import pygame

pygame.init()

screen = pygame.display.set_mode((500,600))

BLUE = (0,19,130)

running = True

while running:
	screen.fill(BLUE)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				print("chuột trái")
			if event.button == 2:
				print("chuột phải")

	pygame.display.flip()

pygame.quit()