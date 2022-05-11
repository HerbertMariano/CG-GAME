import pygame as pg
import numpy as np
from pygame.locals import *
 
def main():
    pg.init()
    screen = pg.display.set_mode((800,600))
    running = True
    
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                runnin = False

        frame = np.random.uniform(0,1,(80,60,3))

        surf = pg.surfarray.make_surface(frame*255)
        surf = pg.transform.scale(surf,(800,600))
        screen.blit(surf,(0,0))
        pg.display.update()

if __name__ == "__main__" :
    main()
    pg.quit()