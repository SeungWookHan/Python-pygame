import random
import pygame
####################################################################
# 기본 초기화(무조건 해야함)
pygame.init()  # 초기화

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Quiz - 똥 피하기")

# FPS
clock = pygame.time.Clock()
####################################################################

# 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 폰트 등 설정)
# 배경 만들기
background = pygame.image.load(
    '/Users/Han/programming/python-pygame/background.png')

# 캐릭터 만들기
character = pygame.image.load(
    '/Users/Han/programming/python-pygame/character.jpg')
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 이동 위치
to_x = 0
character_speed = 10

# 적 만들기
enemy = pygame.image.load('/Users/Han/programming/python-pygame/enemy.jpg')
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)  # x는 랜덤
enemy_y_pos = 0

enemy_speed = 10

running = True
while running:
    dt = clock.tick(30)

    # 2. 키보드, 마우스 등 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
                print(to_x)
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
                print(to_x)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x

    #  경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0

    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 적(똥) 위치 정의
    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    pygame.display.update()


# 종료
pygame.quit()
