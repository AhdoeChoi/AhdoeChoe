import random
import json
import os
import math

from pico2d import *


from object_rupy import Rupy
from object_joro import Joro
from object_dragondown import DragonDown
from object_dragonup import DragonUp
from object_energydown import EnergyDown
from object_energyup import EnergyUp
from object_coindown import CoinDown
from object_coinup import CoinUp
from object_obstacledown import ObstacleDown
from object_obstacleup import ObstacleUp
from object_grass import Grass
from object_background import BackGround

import game_framework
import title_state
import ranking_state
hp = 8
coin = 0

name = "MainState"

rupy = None
grass = None
joro = None
Background = None

class HPBar:
    global hp
    image = None

    def __init__(self):
        self.x = 400
        self.y = 570
        self.hpstate = hp
        self.hp8 = load_image('image\\hp8.png')
        self.hp7 = load_image('image\\hp7.png')
        self.hp6 = load_image('image\\hp6.png')
        self.hp5 = load_image('image\\hp5.png')
        self.hp4 = load_image('image\\hp4.png')
        self.hp3 = load_image('image\\hp3.png')
        self.hp2 = load_image('image\\hp2.png')
        self.hp1 = load_image('image\\hp1.png')

    def update(self,frame_time):
        self.hpstate = hp

    def drawhp8(self):
        self.hp8.draw(self.x,self.y)
    def drawhp7(self):
        self.hp7.draw(self.x, self.y)
    def drawhp6(self):
        self.hp6.draw(self.x, self.y)
    def drawhp5(self):
        self.hp5.draw(self.x, self.y)
    def drawhp4(self):
        self.hp4.draw(self.x, self.y)
    def drawhp3(self):
        self.hp3.draw(self.x, self.y)
    def drawhp2(self):
        self.hp2.draw(self.x, self.y)
    def drawhp1(self):
        self.hp1.draw(self.x, self.y)




 #Charecter 객체


current_time = 0.0

def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time


def enter():
    global rupy, joro,background,grass,coinsdown,coinsup,obstaclesdown,obstaclesup,energysup,energysdown,dragonsup,dragonsdown,hpbar
    global font
    rupy = Rupy()
    joro = Joro()
    background = BackGround()
    grass = Grass()
    hpbar = HPBar()
    coinsdown = [CoinDown() for i in range(70)]
    coinsup = [CoinUp() for i in range(70)]
    obstaclesdown = [ObstacleDown() for i in range(50)]
    obstaclesup = [ObstacleUp() for i in range(50)]
    energysup = [EnergyUp() for i in range(3)]
    energysdown = [EnergyDown() for i in range(3)]
    dragonsup = [DragonUp() for i in range(20)]
    dragonsdown = [DragonDown() for i in range(20)]
    font = load_font('ENCR10B.TTF')
    #pass


def exit():
    global rupy, joro, background, grass,coinsdown , font,hp

    #print('TIME: %4.1f, Coin:%3d, Hp:%3d' %
         # (rupy.life_time, coin, hp))

    f = open('data.txt', 'r')
    score_data = json.load(f)
    f.close()

    if(hp<0):
        hp=0
    score_data.append({"Time": rupy.life_time, "Coin": coin, "Hp": hp})
    #print(score_data)

    f = open('data.txt', 'w')
    json.dump(score_data, f)
    f.close()
   # del(rupy)
   # del(joro)
   # del(background)
  #  del(grass)
   # del(coinsdown)
   # del(coinsup)
   # del(obstaclesdown)
    #del(energysup)
   # del(energysdown)
    #del(dragonsup)
    #del(dragonsdown)
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
        else:
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            if (event.type, event.key) == (SDL_KEYDOWN,SDLK_q):
                game_framework.change_state(ranking_state)
            #루피 부분
            elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
                rupy.state = 1
                rupy.jump_sound()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
                    rupy.attack_sound()
                    rupy.state = 2 # 2는 공격

            #여기 까지

            #조로 부분
            elif event.type == SDL_KEYDOWN and event.key == SDLK_w:
                joro.state = 1 #1은 점프
                joro.jump_sound()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
                joro.attack_sound()
                joro.state = 2  # 2는 공격
            #여기 까지
                #pass

def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()


    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True


def update():
    global hp
    global coin
    frame_time = get_frame_time()
    print(hpbar.hpstate)

    if(hp < 1):
        game_framework.change_state(ranking_state)
    rupy.update(frame_time)
    joro.update(frame_time)
    background.update(frame_time)
    grass.update(frame_time)
    hpbar.update(frame_time)
    for coindown in coinsdown:
        coindown.update(frame_time)
    for coinup in coinsup:
        coinup.update(frame_time)
    for obstacledown in obstaclesdown:
        obstacledown.update(frame_time)
    for obstacleup in obstaclesup:
        obstacleup.update(frame_time)
    for energyup in energysup:
        energyup.update(frame_time)
    for energydown in energysdown:
        energydown.update(frame_time)
    for dragonup in dragonsup:
        dragonup.update(frame_time)
    for dragondown in dragonsdown:
        dragondown.update(frame_time)



    for coinup in coinsup:
        if collide(joro, coinup):
             #print("collision")
            coinsup.remove(coinup)
            coin +=1
            joro.eat_coin()
    for coindown in coinsdown:
        if collide(rupy, coindown):
             # print("collision")
            coinsdown.remove(coindown)
            coin += 1
            rupy.eat_coin()
    for obstacleup in obstaclesup:
        if collide(joro, obstacleup):
            # print("collision")
            obstaclesup.remove(obstacleup)
            joro.state = -1
            hp -= 1
            joro.eat_obstacle()
            joro.jumpstate = 0


    for obstacledown in obstaclesdown:
        if collide(rupy, obstacledown):
            # print("collision")
            obstaclesdown.remove(obstacledown)

            rupy.state = -1
            hp -= 1
            rupy.eat_obstacle()
            rupy.jumpstate = 0



    for energyup in energysup:
        if collide(joro, energyup):
            energysup.remove(energyup)
            hp +=1
            joro.eat_hp()
    for energydown in energysdown:
        if collide(rupy, energydown):
            energysdown.remove(energydown)
            hp += 1
            rupy.eat_hp()

    for dragonup in dragonsup:
        if collide(joro,dragonup):
            if(joro.state !=2):
                joro.state = -1
                joro.jumpstate = 0
                hp -= 1
                joro.eat_obstacle()
                dragonsup.remove(dragonup)
            if(joro.state ==2):
                dragonsup.remove(dragonup)
    for dragondown in dragonsdown:
        if collide(rupy, dragondown):
            if(rupy.state != 2):
                rupy.state = -1
                rupy.jumpstate = 0
                hp -= 1
                rupy.eat_obstacle()
                dragonsdown.remove(dragondown)
            if(rupy.state == 2):
                dragonsdown.remove(dragondown)


    #Dragon 장애물

    #pass

    #print(rupy.life_time)
    #print("joro State :  ", joro.state)

def draw():
    global hp
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
        if(rupy.crushstate > 0.5):
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

    if (joro.state == -1):
        if (joro.crushstate > 0.5):
            joro.state = 0
            joro.crushstate = 0

        else:
            joro.crushstate += 0.1
        joro.drawcrush()
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

    #에너지 클래스 그리기
    for energyup in energysup:
        energyup.draw()

    for energydown in energysdown:
        energydown.draw()

    #드래곤 클래스 그리기
    for dragonup in dragonsup:
        dragonup.draw()

    for dragondown in dragonsdown:
        dragondown.draw()

    #체력바 클래스 그리기
    if(hpbar.hpstate > 8):
        hpbar.drawhp8()
    if(hpbar.hpstate == 8):
        hpbar.drawhp8()
    if (hpbar.hpstate == 7):
         hpbar.drawhp7()
    if (hpbar.hpstate == 6):
        hpbar.drawhp6()
    if (hpbar.hpstate == 5):
        hpbar.drawhp5()
    if (hpbar.hpstate == 4):
        hpbar.drawhp4()
    if (hpbar.hpstate == 3):
        hpbar.drawhp3()
    if (hpbar.hpstate == 2):
        hpbar.drawhp2()
    if (hpbar.hpstate == 1):
        hpbar.drawhp1()

     #충돌체크 박스 그리기

    rupy.draw_bb()
    rupy.draw_bb_attack()

    joro.draw_bb()
    joro.draw_bb_attack()

    for coinup in coinsup:
        coinup.draw_bb()
    for coindown in coinsdown:
        coindown.draw_bb()
    for obstacleup in obstaclesup:
        obstacleup.draw_bb()
    for obstacledown in obstaclesdown:
        obstacledown.draw_bb()
    for dragondown in dragonsdown:
        dragondown.draw_bb()
    for dragonup in dragonsup:
        dragonup.draw_bb()
    #충돌체크 박스 그리기 끝

    update_canvas()

    delay(0.05)
    #pass





