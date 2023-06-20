import random
import sys
import pygame as pg

WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    bakudan = pg.Surface((20, 20))  #練習１
    pg.draw.circle(bakudan,(255, 0, 0),(10, 10), 10) 
    bakudan_x = random.randint(0, WIDTH)
    bakudan_y = random.randint(0,HEIGHT) 
    #爆弾surface(bakudan)から爆弾rectから抽出する 
    bakudan_rct = bakudan.get_rect()
    bakudan_rct.center = bakudan_x ,bakudan_y
    vx = 5  #練習２
    vy = 5  #練習２
    bakudan.set_colorkey((0, 0, 0))
    clock = pg.time.Clock()
    tmr = 0

    

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        bakudan_rct.move_ip(vx,vy)  #練習２
        screen.blit(bakudan,bakudan_rct)

        pg.display.update()
        tmr += 1
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()