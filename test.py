import pygame
import sys
import random

def main():
    pygame.init()
    pygame.display.set_caption("弾を打つ練習")
    screen = pygame.display.set_mode((1400, 720))
    clock = pygame.time.Clock()

    # プレイヤーの設定
    pcolor=0
    player = {"x": 270, "y": 600, "width": 100, "height": 50, "color": (pcolor,255, 0)}

    # 弾丸の設定
    pcolor=0
    font=pygame.font.SysFont("arial",50)
    score_font=pygame.font.SysFont("Calibri",56) 
    score=0
    t=60
    bullets = []
    bullet_width = 10
    bullet_height = 20
    bullet_speed = 5.5 
    enemies=[]
    enemy_width=50
    enemy_height=50
    enemy_speed=4
    enemies2=[]
    enemy_width2=50
    enemy_height2=50
    enemy_speed2=6
    enemies3=[]
    enemy_width3=50
    enemy_height3=50
    enemy_speed3=8
    spawn_interval=60
    frame_count=0
    while True:
        # イベント処理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # プレイヤー操作
        keys = pygame.key.get_pressed()
        if score<250:
            pcolor=255
        if keys[pygame.K_j]:
            t = 1
        if keys[pygame.K_h]:
            t = 0
        if keys[pygame.K_n]:
            t = 60
        if keys[pygame.K_m]:
            t += 1
        if keys[pygame.K_b]:
            t -=1
        if keys[pygame.K_d] and player["x"] < 1350 - player["width"]:
            player["x"] += 10
        if keys[pygame.K_a] and player["x"] > 0:
            player["x"] -= 10
        if keys[pygame.K_LEFT] and player["x"] > 0:
            player["x"] -= 10
        if keys[pygame.K_RIGHT] and player["x"] < 1350 - player["width"]:
            player["x"] += 10
        if keys[pygame.K_DOWN]and player["y"] < 700 - player["width"]:
            player["y"] += 10
        if keys[pygame.K_UP]> 0:
            player["y"] -= 10
        if keys[pygame.K_SPACE]:  # スペースキーで弾丸を発射
          bullets.append({"x": player["x"] + player["width"] // 2 - bullet_width // 2, 
                            "y": player["y"],"rect":pygame.Rect(player["x"]+ player["width"]//2-bullet_width//2,player["y"],bullet_width,bullet_height)})
        
        def draw_score(score):
            score_text=score_font.render(f"score:{score}",True,(255,255,255))
            screen.fill((0,0,0))
            screen.blit(score_text,(1300,600))

        # 弾丸の移動

        for bullet in bullets:
            bullet["y"] -= bullet_speed
            bullet["rect"].y=bullet["y"]
        frame_count+=1
        if frame_count % spawn_interval == 0:
            enemy_x=random.randint(0,1300-enemy_width)
            enemies.append({"x":enemy_x,"y":0,"rect":pygame.Rect(enemy_x,0,enemy_width,enemy_height)})
        for enemy in enemies:
            enemy["y"]+=enemy_speed
            enemy["rect"].y=enemy["y"]

        for bullet in bullets:
            bullet["y"] -= bullet_speed
            bullet["rect"].y=bullet["y"]
        frame_count+=1
        if frame_count % spawn_interval == 0:
            enemy2_x=random.randint(0,1300-enemy_width2)
            enemies2.append({"x":enemy2_x,"y":0,"rect":pygame.Rect(enemy2_x,0,enemy_width2,enemy_height2)})
        for enemy2 in enemies2:
            enemy2["y"]+=enemy_speed2
            enemy2["rect"].y=enemy2["y"]

        for bullet in bullets:
            bullet["y"] -= bullet_speed
            bullet["rect"].y=bullet["y"]
            frame_count+=1
        if frame_count % spawn_interval == 0:
            enemy3_x=random.randint(0,1250-enemy_width3)
            enemies3.append({"x":enemy3_x,"y":0,"rect":pygame.Rect(enemy3_x,0,enemy_width3,enemy_height3)})
        for enemy3 in enemies3:
            enemy3["y"]+=enemy_speed3
            enemy3["rect"].y=enemy3["y"]

        # 画面外の弾丸を削除
        bullets = [bullet for bullet in bullets if bullet["y"] > 0]
        enemies=[enemy for enemy in enemies if enemy["y"]<730]

        # 描画
        
        new_enemies=[]
        for enemy in enemies:
            hit=False
            for bullet in bullets:
                if enemy["rect"].colliderect(bullet["rect"]):
                    score+=1
                    bullets.remove(bullet)
                    hit=True
                    break
            if not hit:
                new_enemies.append(enemy)
        enemies=new_enemies

        new_enemies2=[]
        for enemy2 in enemies2:
            hit=False
            for bullet in bullets:
                if enemy2["rect"].colliderect(bullet["rect"]):
                    score+=2
                    bullets.remove(bullet)
                    hit=True
                    break
            if not hit:
                new_enemies2.append(enemy2)
        enemies2=new_enemies2

        new_enemies3=[]
        for enemy3 in enemies3:
            hit=False
            for bullet in bullets:
                if enemy3["rect"].colliderect(bullet["rect"]):
                    score+=3
                    bullets.remove(bullet)
                    hit=True

                    break
            if not hit:
                new_enemies3.append(enemy3)
        enemies3=new_enemies3

        screen.fill((0, 0, 0))  # 背景を黒に
        pygame.draw.rect(screen, player["color"], (player["x"], player["y"], player["width"], player["height"]))  # プレイヤー
        for bullet in bullets:
            pygame.draw.rect(screen, (0, 255, 200), (bullet["x"], bullet["y"], bullet_width, bullet_height))  # 弾丸
        for enemy in enemies:
            pygame.draw.rect(screen, (0, 0, 255), (enemy["x"], enemy["y"], enemy_width, enemy_height)) 
        for enemy2 in enemies2:
            pygame.draw.rect(screen, (0, 255, 0), (enemy2["x"], enemy2["y"], enemy_width2, enemy_height2)) 
        for enemy3 in enemies3:
            pygame.draw.rect(screen, (255, 0, 0), (enemy3["x"], enemy3["y"], enemy_width3, enemy_height3)) 
        
        text=font.render(f"score:{score}",True,(255,255,255))
        screen.blit(text,[20,100])
        text=font.render(f"t:{t}",True,(255,255,255))
        screen.blit(text,[5,5])
        pygame.display.update()
        clock.tick(t)
        draw_score(score)

if __name__ == "__main__":
    main()
