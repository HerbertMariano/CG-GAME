import pygame as pg
import numpy as np
import sys
from pygame.locals import *

weigth = 800
heigth = 600
size = (weigth,heigth)
hres = 120
halfvres = 100
mod = hres/60
posx, posy, rot = 0,0,0
ns = halfvres/((halfvres+0.1-np.linspace(0, halfvres, halfvres)))# depth
cos22 = np.cos(np.deg2rad(np.linspace(-30,30, hres)/mod)) # perspective correction
shade = 0.4 + 0.6*(np.linspace(0, halfvres, halfvres)/halfvres)
shade = np.dstack((shade, shade, shade))
floor = pg.surfarray.array3d(pg.image.load('floor.jpg'))
kart = pg.surfarray.array3d(pg.image.load('MarioKart.png'))
sky = pg.image.load('skybox.jpg')
sky = pg.surfarray.array3d(pg.transform.scale(sky, (360, halfvres*2)))
 
class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.frame = np.random.uniform(0,1,(80,60,3))
        self._running = True
        self.screen = pg.display.set_mode(size)
        
    
    def on_event(self):
        for event in pg.event.get():
            if event == pg.QUIT or pg.K_ESCAPE:
                self._running == False
            

    def on_loop(self):
        
        while self._running == True:
            self.on_event()
            for i in range(hres):
                rot_i = rot + np.deg2rad(i/mod - 30)
                sin, cos, cos2 = np.sin(rot_i), np.cos(rot_i), np.cos(np.deg2rad(i/mod-30))
                self.frame[i][:halfvres] = sky[int(np.rad2deg(rot_i)%360)][:halfvres]/255
                xs, ys = posx+ns*cos/cos2, posy+ns*sin/cos2
                xxs, yys = (xs/30%1*1023).astype('int'), (ys/30%1*1023).astype('int')
                self.frame[i][2*halfvres-len(ns):2*halfvres] = shade*kart[np.flip(xxs),np.flip(yys)]/255
            self.surf = pg.surfarray.make_surface(self.frame*255)
            self.surf = pg.transform.scale(self.surf,size)
            self.screen.blit(self.surf,(0,0))
            pg.display.update()
 

 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_loop()
    pg.quit()
    
