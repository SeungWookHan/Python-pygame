import pygame
####################################################################
# 기본 초기화(무조건 해야함)
pygame.init()  # 초기화

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("woogy_game")

# FPS
clock = pygame.time.Clock()
####################################################################

# 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 폰트 등 설정)


running = True
while running:
    dt = clock.tick(30)

    # 2. 키보드, 마우스 등 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기

    pygame.display.update()


# 종료
pygame.quit()
