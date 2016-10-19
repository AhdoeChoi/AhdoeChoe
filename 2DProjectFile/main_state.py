import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"

rupy = None
grass = None
joro = None
Background = None



class Grass:
    def __init__(self):
        self.x = 0
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400-self.x,30)
        self.image.draw(400-self.x,330)
    def update(self):
        self.x+=0.5

class BackGround:
    def __init__(self):
        self.image = load_image('BackGround1.png')
        self.x = 0
        self.y = 0
    def draw(self):
        self.image.draw(400-self.x,300)
    def update(self):
        self.x += 0.5

 #Charecter 객체
class Rupy:
   def __init__(self):
        self.x = 60
        self.y = 130
        self.frame = 0
        self.runimage = load_image('rupy_run.png')
        self.jumpimage = load_image('rupy_jump.png')

        self.state = 0 # 0은 달리기 1은 점프
        self.jumpstate = 0 #0이면 up 1이면 down
   def update(self):
        self.frame = (self.frame+1) % 6
   def drawrun(self):
        self.runimage.clip_draw(self.frame*150, 0, 120, 150, self.x, self.y)
   def drawjump(self):
       self.jumpimage.clip_draw(self.frame * 125, 0, 120, 200, self.x, self.y)

class Joro:
    def __init__(self):
        self.x = 60
        self.y = 430
        self.frame = 0
        self.runimage = load_image('joro_run.png')
        self.jumpimage = load_image('joro_jump.png')

        self.state = 0 # 0은 달리기 1은 점프
        self.jumpstate = 0
    def update(self):
        self.frame = (self.frame + 1) % 6
    def drawrun(self):
        self.runimage.clip_draw(self.frame * 160, 0, 160, 150, self.x, self.y)
    def drawjump(self):
        self.jumpimage.clip_draw(self.frame * 175, 0, 150, 200, self.x, self.y)





def enter():
    global rupy, joro,background,grass
    rupy = Rupy()
    joro = Joro()
    background = BackGround()
    grass = Grass()

    #pass


def exit():
    global rupy, joro, background, grass
    del(rupy)
    del(joro)
    del(background)
    del(grass)
    #pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            rupy.state = 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_w:
            joro.state = 1

            #pass


def update():
    rupy.update()
    joro.update()
    background.update()
    grass.update()
    #pass


def draw():
    clear_canvas()

    background.draw()
    grass.draw()

    if(rupy.state == 0):
        rupy.drawrun()
    if(rupy.state == 1):
        if (rupy.jumpstate == 0):  # 올라가고
            rupy.y += 25
        if (rupy.y > 230):
            rupy.jumpstate = 1
        if (rupy.jumpstate == 1):  # 내려가야함
            rupy.y -= 25
        if (rupy.y <= 130):
            rupy.jumpstate = 0
            rupy.state = 0
        rupy.drawjump()

    if (joro.state == 0):
        joro.drawrun()  # 루피 다시그린다
    elif (joro.state == 1):
        if (joro.jumpstate == 0):  # 올라가고
            joro.y += 25
        if (joro.y > 530):
            joro.jumpstate = 1
        if (joro.jumpstate == 1):  # 내려가야함
            joro.y -= 25
        if (joro.y <= 430):
            joro.jumpstate = 0
            joro.state = 0
        joro.drawjump()
    update_canvas()

    delay(0.05)
    #pass





