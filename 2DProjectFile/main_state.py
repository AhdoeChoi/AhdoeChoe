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
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km/Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None
    def __init__(self):
        self.x = 50*random.randint(1,30)
        self.y = 130
        if CoinDown.image == None:
            CoinDown.image   = load_image('coin.png')

    def update(self,frame_time):

        distance = CoinDown.RUN_SPEED_PPS * frame_time
        self.x -=  distance

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class CoinUp:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km/Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None
    def __init__(self):
        self.x = 50*random.randint(1,30)
        self.y = 430
        if CoinUp.image == None:
            CoinUp.image   = load_image('coin.png')
    def update(self,frame_time):
        distance = CoinUp.RUN_SPEED_PPS * frame_time
        self.x -= distance
    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class ObstacleDown:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km/Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    image = None
    def __init__(self):
        self.x = 100 *random.randint(1,10)
        self.y = 80
        if ObstacleDown.image == None:
            ObstacleDown.image   = load_image('obstacle.png')
    def draw(self):
        self.image.draw(self.x,self.y)
    def update(self,frame_time):
        distance = ObstacleDown.RUN_SPEED_PPS * frame_time
        self.x -= distance
    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class ObstacleUp:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km/Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    image = None
    def __init__(self):
        self.x = 100 * random.randint(1,10)
        self.y = 380
        if ObstacleUp.image == None:
            ObstacleUp.image   = load_image('obstacle.png')
    def draw(self):
        self.image.draw(self.x,self.y)
    def update(self,frame_time):
        distance = ObstacleUp.RUN_SPEED_PPS * frame_time
        self.x -= distance
    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Grass:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km/Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.x = 0
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(1400-self.x,30)
        self.image.draw(1400-self.x,330)
    def update(self,frame_time):
        distance = Grass.RUN_SPEED_PPS * frame_time
        self.x += distance


class BackGround:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 1.0  # Km/Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    def __init__(self):
        self.image = load_image('BackGround1.png')
        self.x = 0
        self.y = 0
    def draw(self):
        self.image.draw(400-self.x,300)
    def update(self,frame_time):
        distance = BackGround.RUN_SPEED_PPS * frame_time
        self.x += distance

 #Charecter 객체
class Rupy:

    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 30.0  # Km/Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.x = 80
        self.y = 130
        self.frame = 0
        self.runimage = load_image('rupy_run.png')
        self.jumpimage = load_image('rupy_jump.png')
        self.attackimage = load_image('rupy_attack.png')
        self.crushimage = load_image('rupy_crush.png')
        self.i = 0

        self.state = 0 # 0은 달리기 1은 점프
        self.jumpstate = 0 #0이면 up 1이면 down
        self.attackstate = 0
        self.crushstate = 0
    def update(self,frame_time):
       distance = Rupy.RUN_SPEED_PPS * frame_time
       if(self.state == 0 ):
            self.frame = (self.frame+1) % 6
       elif(self.state == -1):
            self.frame = (self.frame+1) % 4
       elif (self.state == 1):
           self.frame = (self.frame + 1) % 4
           if (self.jumpstate == 0):  # 올라가고
               self.y += distance
           if (self.y > 230):
               self.jumpstate = 1
           if (self.jumpstate == 1):  # 내려가야함
               self.y -= distance
           if (self.y <= 130):
               self.jumpstate = 0
               self.state = 0
       elif (self.state == 2):
           self.frame = (self.frame + 1) % 6

    def drawrun(self):
        self.runimage.clip_draw(self.frame*150, 0, 120, 150, self.x, self.y)
    def drawjump(self):
       self.jumpimage.clip_draw(self.frame * 125, 0, 120, 200, self.x, self.y)
    def drawattack(self):
       self.attackimage.clip_draw(self.frame * 153,5,155,170,self.x,self.y+10)
    def drawcrush(self):
       self.crushimage.clip_draw(self.frame*125,0,125,150,self.x,self.y)


    def get_bb(self):
        return self.x - 30, self.y - 50, self.x + 30, self.y + 50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Joro:

    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 30.0  # Km/Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

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
    def update(self,frame_time):
        distance = Joro.RUN_SPEED_PPS * frame_time
        if (self.state == 0):
            self.frame = (self.frame + 1) % 6
        elif (self.state == -1):
            self.frame = (self.frame + 1) % 4
        elif (self.state == 1):
            self.frame = (self.frame + 1) % 4
            if (self.jumpstate == 0):  # 올라가고
                self.y += distance
            if (self.y > 530):
                self.jumpstate = 1
            if (self.jumpstate == 1):  # 내려가야함
                self.y -= distance
            if (self.y <= 430):
                self.jumpstate = 0
                self.state = 0
        elif (self.state == 2):
            self.frame = (self.frame + 1) % 6

    def drawrun(self):
        self.runimage.clip_draw(self.frame * 160, 0, 160, 150, self.x, self.y)
    def drawjump(self):
        self.jumpimage.clip_draw(self.frame * 175, 0, 150, 200, self.x, self.y)
    def drawattack(self):
        self.attackimage.clip_draw(self.frame * 188, 0, 180, 200, self.x+10, self.y+15)


    def get_bb(self):
        return self.x - 20, self.y - 50, self.x + 40, self.y + 50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

current_time = 0.0

def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time


def enter():
    global rupy, joro,background,grass,coinsdown,coinsup,obstaclesdown,obstaclesup
    rupy = Rupy()
    joro = Joro()
    background = BackGround()
    grass = Grass()
    coinsdown = [CoinDown() for i in range(30)]
    coinsup = [CoinUp() for i in range(30)]
    obstaclesdown = [ObstacleDown() for i in range(3)]
    obstaclesup = [ObstacleUp() for i in range(3)]

    #pass


def exit():
    global rupy, joro, background, grass,coinsdown
    del(rupy)
    del(joro)
    del(background)
    del(grass)
    del(coinsdown)
    del(coinsup)
    del(obstaclesdown)
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
    frame_time = get_frame_time()

    rupy.update(frame_time)
    joro.update(frame_time)
    background.update(frame_time)
    grass.update(frame_time)
    for coindown in coinsdown:
        coindown.update(frame_time)
    for coinup in coinsup:
        coinup.update(frame_time)
    for obstacledown in obstaclesdown:
        obstacledown.update(frame_time)
    for obstacleup in obstaclesup:
        obstacleup.update(frame_time)

    for coinup in coinsup:
        if collide(joro, coinup):
             #print("collision")
            coinsup.remove(coinup)

    for coindown in coinsdown:
        if collide(rupy, coindown):
             # print("collision")
            coinsdown.remove(coindown)

    for obstacleup in obstaclesup:
        if collide(joro, obstacleup):
            # print("collision")
            obstaclesup.remove(obstacleup)

    for obstacledown in obstaclesdown:
        if collide(rupy, obstacledown):
            # print("collision")
            obstaclesdown.remove(obstacledown)


    #pass

def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True


def draw():
    clear_canvas()

    background.draw()
    grass.draw()


    #루피 그리기
    if(rupy.state == 0):
        rupy.drawrun()
    if(rupy.state == 1):
        rupy.drawjump()

    if(rupy.state == 2):
        if(rupy.attackstate > 1):
            rupy.state = 0
            rupy.attackstate = 0
        else:
            rupy.attackstate += 0.1
        rupy.drawattack()

    if(rupy.state == -1):
        if(rupy.crushstate > 1):
            rupy.state = 0
            rupy.crushstate = 0
        else:
            rupy.crushstate += 0.1
        rupy.drawcrush()
    #여기까지 루피 그린거



    #조로 그리기
    if (joro.state == 0):
        joro.drawrun()  # 루피 다시그린다
    elif (joro.state == 1):
        joro.drawjump()
    if (joro.state == 2):
        if (joro.attackstate > 1):
            joro.state = 0
            joro.attackstate = 0
        else:
            joro.attackstate += 0.1
        joro.drawattack()

    #코인 클래스그리기기
    for coindown in coinsdown:
        coindown.draw()

    for coinup in coinsup:
         coinup.draw()

     #장애물 클래스 그리기
    for obstacledown in obstaclesdown:
        obstacledown.draw()

    for obstacleup in obstaclesup:
        obstacleup.draw()



     #충돌체크 박스 그리기

    rupy.draw_bb()
    joro.draw_bb()

    for coinup in coinsup:
        coinup.draw_bb()
    for coindown in coinsdown:
        coindown.draw_bb()
    for obstacleup in obstaclesup:
        obstacleup.draw_bb()
    for obstacledown in obstaclesdown:
        obstacledown.draw_bb()

    #충돌체크 박스 그리기 끝

    update_canvas()

    delay(0.05)
    #pass





