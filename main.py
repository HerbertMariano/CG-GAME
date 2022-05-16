import pygame as pg
import numpy as np

pg.init()
window = pg.display.set_mode((500,500))
pg.display.set_caption("Game Raycasting")
running = True

if __name__ == '__main__':
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        pg.display.update()
    
    pg.quit()