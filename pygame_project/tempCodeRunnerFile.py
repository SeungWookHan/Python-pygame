
    # for ball_idx, ball_val in enumerate(balls):
    #     ball_pos_x = ball_val["pos_x"]
    #     ball_pos_y = ball_val["pos_y"]
    #     ball_img_idx = ball_val["img_idx"]

    #     # 공 rect 정보 업데이트
    #     ball_rect = ball_images[ball_img_idx].get_rect()
    #     ball_rect.left = ball_pos_x
    #     ball_rect.top = ball_pos_y

    #     # 공과 캐릭터 충돌 처리
    #     if character_rect.colliderect(ball_rect):
    #         running = False
    #         break