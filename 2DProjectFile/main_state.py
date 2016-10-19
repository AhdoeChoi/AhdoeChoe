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

class CoinDown:
    image = None
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = 130
        if CoinDown.image == None:
            CoinDown.image   = load_image('coin.png')
    def update(self):
        self.x -= 5
    def draw(self):
        self.image.draw(self.x, self.y)


class CoinUp:
    image = None
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = 430
        if CoinUp.image == None:
            CoinUp.image   = load_image('coin.png')
    def update(self):
        self.x -= 5
    def draw(self):
        self.image.draw(self.x, self.y)


class Grass:
    def __init__(self):
        self.x = 0
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400-self.x,30)
        self.image.draw(400-self.x,330)
    def update(self):
        self.x+=3;

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
        self.x = 80
        self.y = 130
        self.frame = 0
        self.runimage = load_image('rupy_run.png')
        self.jumpimage = load_image('rupy_jump.png')
        self.attackimage = load_image('rupy_attack.png')

        self.state = 0 # 0은 달리기 1은 점프
        self.jumpstate = 0 #0이면 up 1이면 down
        self.attackstate = 0
   def update(self):
        self.frame = (self.frame+1) % 6
   def drawrun(self):
        self.runimage.clip_draw(self.frame*150, 0, 120, 150, self.x, self.y)
   def drawjump(self):
       self.jumpimage.clip_draw(self.frame * 125, 0, 120, 200, self.x, self.y)
   def drawattack(self):
       self.attackimage.clip_draw(self.frame * 153,5,155,170,self.x,self.y+10)

class Joro:
    def __init__(self):
        self.x = 80
        self.y = 430
        self.frame = 0
        self.runimage = load_image('joro_run.png')
        self.jumpimage = load_image('joro_jump.png')
        self.attackimage = load_image('joro_attack.png')

        self.state = 0 # 0은 달리기 1은 점프
        self.jumpstate = 0
        self.attackstate = 0
    def update(self):
        self.frame = (self.frame + 1) % 6
    def drawrun(self):
        self.runimage.clip_draw(self.frame * 160, 0, 160, 150, self.x, self.y)
    def drawjump(self):
        self.jumpimage.clip_draw(self.frame * 175, 0, 150, 200, self.x, self.y)
    def drawattack(self):
        self.attackimage.clip_draw(self.frame * 188, 0, 180, 200, self.x+10, self.y+15)





def enter():
    global rupy, joro,background,grass,coinsdown,coinsup
    rupy = Rupy()
    joro = Joro()
    background = BackGround()
    grass = Grass()
    coinsdown = [CoinDown() for i in range(10)]
    coinsup = [CoinUp() for i in range(10)]

    #pass


def exit():
    global rupy, joro, background, grass,coinsdown
    del(rupy)
    del(joro)
    del(background)
    del(grass)
    del(coinsdown)
    del(coinsup)
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
        #루피 부분
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            rupy.state = 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            if rupy.state != 1:
                rupy.state = 2 # 2는 공격
        #여기 까지

        #조로 부분
        elif event.type == SDL_KEYDOWN and event.key == SDLK_w:
            joro.state = 1 #1은 점프
        elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
            if joro.state != 1:
                joro.state = 2  # 2는 공격
        #여기 까지
            #pass


def update():
    rupy.update()
    joro.update()
    background.update()
    grass.update()
    for coindown in coinsdown:
        coindown.update()
    for coinup in coinsup:
        coinup.update()
    #pass


def draw():
    clear_canvas()

    background.draw()
    grass.draw()

    #루피 그리기
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

    if(rupy.state == 2):
        if(rupy.attackstate > 1):
            rupy.state = 0
            rupy.attackstate = 0
        else:
            rupy.attackstate += 0.1
        rupy.drawattack()
    #여기까지 루피 그린거

    #조로 그리기
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
    if (joro.state == 2):
        if (joro.attackstate > 1):
            joro.state = 0
            joro.attackstate = 0
        else:
            joro.attackstate += 0.1
        joro.drawattack()

    #코인 클래스처리
    for coindown in coinsdown:
        if(coindown.x > rupy.x + 10):
            coindown.draw()

    for coinup in coinsup:
        if(coinup.x > joro. x +10):
            coinup.draw()
    update_canvas()

    delay(0.05)
    #pass





