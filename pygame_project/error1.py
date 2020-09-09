# 공과 무기가 충돌할때 2중 for문 중 안쪽만 나오게 되는 현상

# 예
balls = [1, 2, 3, 4]
weapons = [11, 22, 3, 44]

for ball_idx, ball_val in enumerate(balls):
    print("balls: ", ball_val)
    for weapon_idx, weapon_val in enumerate(weapons):
        print("weapons:", weapon_val)
        if ball_val == weapon_val:
            print("충돌했습니다")
            break  # 여기 break에서 두개의 for문을 모두 나가고 싶지만 안 쪽 for문만 나가면서 생기는 문제
    else:
        continue
    break  # 바깥쪽 for문을 탈출
