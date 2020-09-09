# 5. 모든 공을 없애면 게임 종료 (성공)
# 6. 캐릭터는 공에 닿으면 게임 종료 (실패)
# 7. 시간 제한 99초 초과 시 게임 종료 (실패)

import os
import pygame
####################################################################
# 기본 초기화(무조건 해야함)
pygame.init()  # 초기화

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Hana Love")

# FPS
clock = pygame.time.Clock()
####################################################################

# 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 폰트 등 설정)
current_path = os.path.dirname(__file__)  # 현재 파일의 위치를 반환
image_path = os.path.join(current_path, "images")

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.jpg"))

# 스테이지 만들기
# stage = pygame.image.load(os.path.join(image_path, "stage.png"))
# stage_size = stage.get_rect().size
# stage_height = stage_size[1]

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character-re.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width - 2)
character_y_pos = screen_height - character_height

# 캐릭터 이동 방향
character_to_x = 0

# 캐릭터 이동 속도
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한번에 여러번 발사 가능
weapons = []

# 무기 이동 속도
weapon_speed = 10

# 공 만들기(4개 크기에 대해 따로 처리)
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))
]

# 공 속도(공마다 달라야 함), 공 크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, -9]  # index 0, 1, 2, 3 즉 각각 공에 대한 속도

# 공들 정보
balls = []

# 최초 발생하는 큰 공 추가
balls.append({
    "pos_x": 50,  # 공의 x 좌표
    "pos_y": 50,  # 공의 y 좌표
    "img_idx": 0,
    "to_x": 3,  # 공의 x축 이동 방향
    "to_y": -6,  # 공의 y축 이동 방향
    "init_spd_y": ball_speed_y[0]  # y 최초 속도
})

# 공, 무기 없어지는 변수 추가(충돌시) - 사라진 무기와 공 정보 저장
weapon_to_remove = -1
ball_to_remove = -1

# 폰트 정의
game_font = pygame.font.Font(None, 40)
total_time = 100
start_ticks = pygame.time.get_ticks()  # 시작 시간 정의

# 게임 종료 메시지 / Timeout(시간 초과로 실패), Mission Complete(성공), Game Over(공에 맞아서 실패)
game_result = "Game Over"

running = True
while running:
    dt = clock.tick(30)

    # 2. 키보드, 마우스 등 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                # 무기 발사를 위한 무기 추가 (무기 발사 위치 등)
                weapon_x_pos = character_x_pos + \
                    (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 무기 위치 조정
    # 무기는 x좌표는 그대로 y좌료는 앞으로 나가야 하니
    # 예 100, 200 -> 180, 160, 140 ...(speed 만큼 차감)
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]  # 무기 위치를 위로 올림

    # 천장에 닿은 무기 없애기
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

    # 공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # 가로 위치 경계값
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            # 왼쪽으로 튕기면 오른쪽, 오른쪽으로 튕기면 왼쪽으로 변환 (가로벽)
            ball_val["to_x"] = ball_val["to_x"] * -1

        # 세로 위치
        # 스테이지에 튕겨서 올라가는 처리
        if ball_pos_y >= screen_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:  # 그 외에 모든 경우에는 속도 증가
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

    # 4. 충돌 처리

    # 캐릭터 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        # 공 rect 정보 업데이트
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        # 공과 캐릭터 충돌 처리
        if character_rect.colliderect(ball_rect):
            running = False
            break

        # 공과 무기의 충돌 처리
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            # 무기 rect 정보 업데이트
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            # 충돌 체크
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx  # 해당 무기 없애기 위한 값 설정
                ball_to_remove = ball_idx  # 해당 공 없애기 위한 값 설정

                # 가장 작은 크기의 공이 아니라면 다음 단계의 공으로 나눠주기
                if ball_img_idx < 3:
                    # 현재 공 크기 정보를 가지고 옮
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    # 나눠진 공 정보 구하기
                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                    # 왼쪽으로 튕겨나가는 작은 공
                    balls.append({
                        # 공의 x 좌표
                        "pos_x": ball_pos_x + (ball_width / 2) - (small_ball_width / 2),
                        # 공의 y 좌표
                        "pos_y": ball_pos_y + (ball_height / 2) - (small_ball_height / 2),
                        "img_idx": ball_img_idx + 1,  # 공의 이미지 인덱스
                        "to_x": -3,  # 공의 x축 이동 방향
                        "to_y": -6,  # 공의 y축 이동 방향
                        "init_spd_y": ball_speed_y[ball_img_idx + 1]  # y 최초 속도
                    })

                    # 오른쪽으로 튕겨나가는 작은 공
                    balls.append({
                        # 공의 x 좌표
                        "pos_x": ball_pos_x + (ball_width / 2) - (small_ball_width / 2),
                        # 공의 y 좌표
                        "pos_y": ball_pos_y + (ball_height / 2) - (small_ball_height / 2),
                        "img_idx": ball_img_idx + 1,  # 공의 이미지 인덱스
                        "to_x": 3,  # 공의 x축 이동 방향
                        "to_y": -6,  # 공의 y축 이동 방향
                        "init_spd_y": ball_speed_y[ball_img_idx + 1]  # y 최초 속도
                    })
                break
        else:  # 게임을 계속 진행
            continue  # 안쪽 for문 조건이 맞지 않으면 continue. 바깥 for 문 실행
        break  # 안쪽 for 문에서 break를 만나면 여기로 진입 하여 바깥 for 문도 나감

    # 충돌된 무기, 공 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    # 모든 공을 없앤 경우 게임 종료
    if len(balls) == 0:
        game_result = "Mission Complete"
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    # screen.blit(stage, (0, screen_height - stage_height))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(character, (character_x_pos, character_y_pos))

    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  # ms -> s
    timer = game_font.render("Time : {}".format(
        int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))  # 타이머 그려주기

    if total_time - elapsed_time <= 0:
        game_result = "Time Out"
        running = False

    pygame.display.update()

# 게임 오버 메시지
msg = game_font.render(game_result, True, (255, 255, 0))
msg_rect = msg.get_rect(
    center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()

pygame.time.delay(2000)  # 2초 정도 대기
# 종료
pygame.quit()
