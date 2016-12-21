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
from object_skillup import SkillUp
from object_skilldown import SkillDown

import game_framework
import title_state
import ranking_state
hp = 4
coin = 0
skillcnt = 3
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
        self.hp4 = load_image('image\\hp4.png')
        self.hp3 = load_image('image\\hp3.png')
        self.hp2 = load_image('image\\hp2.png')
        self.hp1 = load_image('image\\hp1.png')

    def update(self,frame_time):
        self.hpstate = hp

    def drawhp4(self):
        self.hp4.draw(self.x, self.y)
    def drawhp3(self):
        self.hp3.draw(self.x, self.y)
    def drawhp2(self):
        self.hp2.draw(self.x, self.y)
    def drawhp1(self):
        self.hp1.draw(self.x, self.y)

class SkillBar:
    global skillcnt
    image = None

    def __init__(self):
        self.x = 400
        self.y = 540
        self.skillstate = skillcnt
        self.skill0 = load_image('image\\skill_0.png')
        self.skill1 = load_image('image\\skill_1.png')
        self.skill2 = load_image('image\\skill_2.png')
        self.skill3 = load_image('image\\skill_3.png')


    def update(self, frame_time):
        self.skillstate = skillcnt


    def drawskill3(self):
        self.skill3.draw(self.x, self.y)

    def drawskill2(self):
        self.skill2.draw(self.x, self.y)

    def drawskill1(self):
        self.skill1.draw(self.x, self.y)

    def drawskill0(self):
        self.skill0.draw(self.x, self.y)


                #Charecter 객체


current_time = 0.0

def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time


def enter():
    global rupy, joro,background,grass,coinsdown,coinsup,obstaclesdown,obstaclesup,energysup,energysdown,dragonsup,dragonsdown,hpbar,skilsup,skilsdown,skillbar

    global font
    rupy = Rupy()
    joro = Joro()
    background = BackGround()
    grass = Grass()
    hpbar = HPBar()
    skillbar = SkillBar()
    coinsdown = [CoinDown() for i in range(100)]
    coinsup = [CoinUp() for i in range(100)]
    obstaclesdown = [ObstacleDown() for i in range(50)]
    obstaclesup = [ObstacleUp() for i in range(50)]
    energysup = [EnergyUp() for i in range(3)]
    energysdown = [EnergyDown() for i in range(3)]
    dragonsup = [DragonUp() for i in range(50)]
    dragonsdown = [DragonDown() for i in range(50)]
    skilsup = [SkillUp() for i in range(2)]
    skilsdown = [SkillDown() for i in range(2)]
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
    global skillcnt
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
                if(rupy.state != 1):
                    rupy.attack_sound()
                    rupy.state = 2 # 2는 공격
            elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
                # if(rupy.state != 1):
                if (rupy.state != 1):
                    if(skillcnt>0):
                        rupy.attack_sound()
                        rupy.state = 3  # 3는 스킬
                        skillcnt -= 1
            #여기 까지

            #조로 부분
            elif event.type == SDL_KEYDOWN and event.key == SDLK_w:
                joro.state = 1 #1은 점프
                joro.jump_sound()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
                if(joro.state !=1):
                    joro.attack_sound()
                    joro.state = 2  # 2는 공격
            elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
                # if(rupy.state != 1):
                if (rupy.state != 1):
                    if (skillcnt > 0):
                        #joro.skill_sound()
                        joro.state = 3  # 3는 스킬
                        skillcnt-=1


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

def collide_attack(a,b):

    left_a, bottom_a, right_a, top_a = a.get_bb_attack()
    left_b, bottom_b, right_b, top_b = b.get_bb()


    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True
def collide_skill(a,b):

    left_a, bottom_a, right_a, top_a = a.get_bb_skill()
    left_b, bottom_b, right_b, top_b = b.get_bb()


    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True
def update():
    global hp
    global coin
    global skillcnt
    frame_time = get_frame_time()


    if(hp < 1):
        game_framework.change_state(ranking_state)
    rupy.update(frame_time)
    joro.update(frame_time)
    background.update(frame_time)
    grass.update(frame_time)
    hpbar.update(frame_time)
    skillbar.update(frame_time)
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
    for skilup in skilsup:
        skilup.update(frame_time)
    for skildown in skilsdown:
        skildown.update(frame_time)

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
            if (joro.state != 3):
                joro.state = -1
                joro.jumpstate = 0
                hp -= 1
                joro.eat_obstacle()
                obstaclesup.remove(obstacleup)
        #if (joro.state == 2):
            #if collide_attack(joro, obstacleup):
                #joro.jumpstate = 0
                #joro.eat_obstacle()
                #obstaclesup.remove(obstacleup)
        if (joro.state == 3):
            if collide_skill(joro, obstacleup):
                joro.jumpstate = 0
                joro.eat_obstacle()
                obstaclesup.remove(obstacleup)

    for obstacledown in obstaclesdown:
        if collide(rupy, obstacledown):
            if (rupy.state != 3):
                rupy.state = -1
                rupy.jumpstate = 0
                hp -= 1
                rupy.eat_obstacle()
                obstaclesdown.remove(obstacledown)
        if (rupy.state == 2):
            if collide_attack(rupy, obstacledown):
                rupy.jumpstate = 0
                rupy.eat_obstacle()
                obstaclesdown.remove(obstacledown)
        if (rupy.state == 3):
            if collide_skill(rupy, obstacledown):
                rupy.jumpstate = 0
                rupy.eat_obstacle()
                obstaclesdown.remove(obstacledown)


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
        if (joro.state == 0 or 1):
            if collide(joro, dragonup):
                if (joro.state != 2):
                    joro.state = -1
                    joro.jumpstate = 0
                    hp -= 1
                    joro.eat_obstacle()
                    dragonsup.remove(dragonup)
        if (joro.state == 2):
            if collide_attack(joro, dragonup):
                joro.jumpstate = 0
                joro.eat_obstacle()
                dragonsup.remove(dragonup)
        if (joro.state == 3):
            if collide_skill(joro, dragonup):
                joro.jumpstate = 0
                joro.eat_obstacle()
                dragonsup.remove(dragonup)

    for dragondown in dragonsdown:
        if(rupy.state == 0 or 1):
            if collide(rupy, dragondown):
                if(rupy.state != 2):
                    rupy.state = -1
                    rupy.jumpstate = 0
                    hp -= 1
                    rupy.eat_obstacle()
                    dragonsdown.remove(dragondown)
        if(rupy.state == 2):
            if collide_attack(rupy, dragondown):
                    rupy.jumpstate = 0
                    rupy.eat_obstacle()
                    dragonsdown.remove(dragondown)
        if (rupy.state == 3):
            if collide_skill(rupy, dragondown):
                rupy.jumpstate = 0
                rupy.eat_obstacle()
                dragonsdown.remove(dragondown)

    #스킬게이지 충돌
    for skilup in skilsup:
        if collide(joro, skilup):
             # print("collision")
             skilsup.remove(skilup)
             skillcnt += 1
             #joro.skilgage += 1
             print(skillcnt)
             print("Joro")
    # 스킬게이지 충돌
    for skildown in skilsdown:
        if collide(rupy, skildown):
            # print("collision")
            skilsdown.remove(skildown)
            skillcnt += 1
            #rupy.skilgage += 1
            print(skillcnt)
            print("Rupy")
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

    if (rupy.state == 3):
        if (rupy.skillstate > 1):
            rupy.state = 0
            rupy.skillstate  = 0
        else:
            rupy.skillstate  += 0.1
        rupy.drawskill()

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
    if (joro.state == 3):
        if (joro.skillstate > 1):
            joro.state = 0
            joro.skillstate = 0
        else:
            joro.skillstate += 0.1
        joro.drawskill()

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

    #스킬up 클래스 그리기
    for skilup in skilsup:
        skilup.draw()
    #스킬down 클래스 그리기
    for skildown in skilsdown:
        skildown.draw()

    #체력바 클래스 그리기
    if(hpbar.hpstate > 4):
        hpbar.drawhp4()
    if (hpbar.hpstate == 4):
        hpbar.drawhp4()
    if (hpbar.hpstate == 3):
        hpbar.drawhp3()
    if (hpbar.hpstate == 2):
        hpbar.drawhp2()
    if (hpbar.hpstate == 1):
        hpbar.drawhp1()

    #스킬바 클래스 그리기
    if (skillbar.skillstate > 3):
        skillbar.drawskill3()
    if (skillbar.skillstate == 3):
        skillbar.drawskill3()
    if (skillbar.skillstate == 2):
        skillbar.drawskill2()
    if (skillbar.skillstate == 1):
        skillbar.drawskill1()
    if (skillbar.skillstate == 0):
        skillbar.drawskill0()
     #충돌체크 박스 그리기

    rupy.draw_bb()
    rupy.draw_bb_attack()
    rupy.draw_bb_skill()

    joro.draw_bb()
    joro.draw_bb_attack()
    joro.draw_bb_skill()
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





