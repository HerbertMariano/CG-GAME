import pygame as pg
import numpy as np

class Game:
    def __init__(self) -> None:    
        pg.init()
        self.window = pg.display.set_mode((800,600))
        pg.display.set_caption("Game Raycasting")
        self.running = True

    def loop(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
        pg.display.update()

if __name__ == '__main__':
    
    x = Game()
    x.loop()
    pg.quit()