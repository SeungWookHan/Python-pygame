import pygame

pygame.init()  # 초기화

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("woogy_game")

background = pygame.image.load(
    "/Users/Han/programming/python-pygame/background.png")
running = True  # 게임의 진행 여부를 확인

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen.fill(())
    screen.blit(background, (0, 0))
    pygame.display.update()

pygame.quit()
