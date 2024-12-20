import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    flip_bg_img = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load(("fig/3.png"))
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()
    tmr = 0
    kk_rct.center = 300, 200
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        X = tmr%3200
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP] or key_lst[pg.K_DOWN] or key_lst[pg.K_RIGHT]:
            if key_lst[pg.K_UP]:
                move_num = (1, -1)
            elif key_lst[pg.K_DOWN]:
                move_num = (1, 1)
            elif key_lst[pg.K_RIGHT]:
                move_num = (1, 0)
        else:
            move_num = (-1, 0)
        kk_rct.move_ip(move_num)
        screen.blit(bg_img, [-X, 0])
        screen.blit(flip_bg_img, [-X+1600, 0])
        screen.blit(bg_img, [-X+3200, 0])
        screen.blit(flip_bg_img, [-X+4800, 0])
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()