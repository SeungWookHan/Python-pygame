import pygame

pygame.init()  # 초기화

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("woogy_game")

# FPS
clock = pygame.time.Clock()

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

# 이동할 좌료
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 적 캐릭터
enemy = pygame.image.load(
    "/Users/Han/programming/python-pygame/enemy.jpg")
enemy_size = enemy.get_rect().size  # 이미지 크기 구해오기
enemy_width = enemy_size[0]  # 캐릭터 가로
enemy_height = enemy_size[1]  # 캐릭터 세로
enemy_x_pos = (screen_width / 2) - \
    (enemy_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치
enemy_y_pos = (screen_height / 2) - enemy_height  # 화면 세로 크기 가장 아래에 위치

# 이벤트 루프
running = True  # 게임의 진행 여부를 확인
while running:
    dt = clock.tick(60)

    #print("fps: " + str(clock.get_fps()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                to_x += character_speed
            if event.key == pygame.K_UP:
                to_y -= character_speed
            if event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    # screen.fill(())
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update()

pygame.quit()
