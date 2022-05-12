import pygame as pg
import numpy as np

class App:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((800, 600))
        self.running = True
        pg.mouse.set_visible(False)
        self.clock = pg.time.Clock()
        self.hres = 120
        self.halfvres = 100 # half of vertical resolution
        self.mod = self.hres/60
        self.posx, self.posy, self.rot = 0,0,0
        self.floor = pg.surfarray.array3d(pg.image.load('floor.jpg'))
        self.kart = pg.surfarray.array3d(pg.image.load('MarioKart.png'))
        self.sky = pg.image.load('skybox.jpg')
        self.sky = pg.surfarray.array3d(pg.transform.scale(self.sky, (360, self.halfvres*2)))
        self.ns = self.halfvres/((self.halfvres+0.1-np.linspace(0, self.halfvres, self.halfvres)))# depth
        self.cos22 = np.cos(np.deg2rad(np.linspace(-30,30, self.hres)/self.mod)) # perspective correction
        self.shade = 0.4 + 0.6*(np.linspace(0, self.halfvres, self.halfvres)/self.halfvres)
        self.shade = np.dstack((self.shade, self.shade, self.shade)) 
        self.frame = np.ones([self.hres, self.halfvres*2, 3])
    
    def on_event(self):
        for event in pg.event.get():
            if event == pg.QUIT or pg.K_ESCAPE:
                self.running == False
            
    def movement(self):
        x, y = (self.posx, self.posy)
    
        p_mouse = pg.mouse.get_pos()
        self.rot = self.rot - 4*np.pi*(0.5-(p_mouse[0]-300)/6400)
        
        if self.pressed_keys[pg.K_UP] or self.pressed_keys[ord('w')]:
            x, y = (x + self.et*np.cos(self.rot), y + self.et*np.sin(self.rot))
            
        if self.pressed_keys[pg.K_DOWN] or self.pressed_keys[ord('s')]:
            x, y = (x - self.et*np.cos(self.rot), y - self.et*np.sin(self.rot))
            
        if self.pressed_keys[pg.K_LEFT] or self.pressed_keys[ord('a')]:
            x, y = (x + self.et*np.sin(self.rot), y - self.et*np.cos(self.rot))
            
        if self.pressed_keys[pg.K_RIGHT] or self.pressed_keys[ord('d')]:
            x, y = (x - self.et*np.sin(self.rot), y + self.et*np.cos(self.rot))
            
        self.posx, self.posy = (x, y)
                                                    
        return self.posx, self.posy, self.rot

    def on_loop(self):
        
        while self.running == True:
            self.on_event()
            for i in range(self.hres):
                self.rot_i = self.rot + np.deg2rad(i/self.mod - 30)
                sin, cos, cos2 = np.sin(self.rot_i), np.cos(self.rot_i), np.cos(np.deg2rad(i/self.mod-30))
                self.frame[i][:self.halfvres] = self.sky[int(np.rad2deg(self.rot_i)%360)][:self.halfvres]/255
                xs, ys = self.posx+self.ns*cos/cos2, self.posy+self.ns*sin/cos2
                xxs, yys = (xs/30%1*1023).astype('int'), (ys/30%1*1023).astype('int')
                self.frame[i][2*self.halfvres-len(self.ns):2*self.halfvres] = self.shade*self.kart[np.flip(xxs),np.flip(yys)]/255
            self.surf = pg.surfarray.make_surface(self.frame*255)
            self.surf = pg.transform.scale(self.surf,(800,600))
            self.screen.blit(self.surf,(0,0))
            pg.display.update()

            self.pressed_keys = pg.key.get_pressed()
            self.et = self.clock.tick()/500         
            self.posx, self.posy, self.rot = self.movement()
            pg.mouse.set_pos([300, 400])

            fps = int(self.clock.get_fps())
            pg.display.set_caption("Pycasting maze - FPS: " + str(fps))

            

 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_loop()
    pg.quit()
    
