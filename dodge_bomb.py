import random
import sys
import pygame as pg

WIDTH, HEIGHT = 1600, 900

delta = {
    pg.K_UP:(0, -5),
    pg.K_DOWN:(0, +5),
    pg.K_LEFT:(-5, 0),
    pg.K_RIGHT:(+5, 0)
}


def check_bound(rect):
    """
    こうかとんRect,爆弾rectが画面買い　or 画面内かを判定する関数
    因数：こうかとんRect or　爆弾Rect
    戻り値：横方向、縦方向の判定結果タプル (True:画面内/False:画面外)
    """
    yoko, tate = True, True
    if rect.left  < 0 or WIDTH < rect.right:
        yoko = False
    if rect.top < 0 or HEIGHT < rect.bottom:
        tate = False
    return yoko, tate


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img_zako = pg.image.load("ex02/fig/8.png")
    kk_img_zako = pg.transform.rotozoom(kk_img_zako, 0, 2.0)

    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_img_r =pg.transform.flip(kk_img,True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
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
    kk_muki = {
        (0, 0):pg.transform.rotozoom(kk_img,0,1.0),  #キーを動かしてないときの工科トンの向き
        (0, -5):pg.transform.rotozoom(kk_img_r,90,1.0),  #上に動かしているとき
        (-5, -5):pg.transform.rotozoom(kk_img,-45,1.0),  #左と上のキー動かしているとき
        (5, -5):pg.transform.rotozoom(kk_img_r,45,1.0),  #みぎと上のキーを押しているとき
        (5, 0):pg.transform.rotozoom(kk_img_r,0,1.0),  #右のキーを押しているとき
        (5, 5):pg.transform.rotozoom(kk_img_r,-45,1.0),  #右と下のキーを押しているとき
        (0, 5):pg.transform.rotozoom(kk_img_r,-90,1.0),  #下のキーを押しているとき
        (-5, 5):pg.transform.rotozoom(kk_img,45,1.0),  #左と下のキーを押しているとき
        (-5, 0):pg.transform.rotozoom(kk_img,0,1.0),  #左のキーを押しているとき
    }   #工科トンの進む方向と向きを決める。
    acs = [a for a in range(1, 11)]  #ボールの加速度の変更1－10まで
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        if kk_rct.colliderect(bakudan_rct):
            screen.blit(bg_img,[0, 0])
            screen.blit(kk_img_zako, kk_rct)  #なく画像に変更する
            pg.display.update()  #ディスプレイをアップデートする
            pg.time.delay(3000)  #3ビョウ間時を止める

            print("ゲームオーバー")
            return  #ゲームオーバー
        key_lst = pg.key .get_pressed()
        sum_mv = [0, 0]

        for k, mv in delta.items():  #ボールが動供養にする
            if key_lst[k]:
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        sum_mv_l = tuple(sum_mv)  #sum_mvをタプルにする


            
        
        

        kk_rct.move_ip(sum_mv)
        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
        avx, avy = vx*acs[min(tmr//500, 9)], vy*acs[min(tmr//500, 9)]

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_muki[sum_mv_l], kk_rct)
        bakudan_rct.move_ip(avx,avy)  #練習２
        yoko, tate = check_bound(bakudan_rct)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1

        screen.blit(bakudan,bakudan_rct)

        pg.display.update()
        tmr += 1
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()