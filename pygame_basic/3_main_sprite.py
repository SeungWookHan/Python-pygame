import pygame

pygame.init()  # 초기화

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("woogy_game")

background = pygame.image.load(
    "/Users/Han/programming/python-pygame/background.png")

# 스파라이트, 캐릭터 불러오기
character = pygame.image.load(
    "/Users/Han/programming/python-pygame/character.jpg")
character_size = character.get_rect().size  # 이미지 크기 구해오기
character_width = character_size[0]  # 캐릭터 가로
character_height = character_size[1]  # 캐릭터 세로
character_x_pos = (screen_width / 2) - \
    (character_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height  # 화면 세로 크기 가장 아래에 위치

# 이벤트 루프
running = True  # 게임의 진행 여부를 확인
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen.fill(())
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()

pygame.quit()
