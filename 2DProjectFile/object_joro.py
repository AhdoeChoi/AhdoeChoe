
from pico2d import *
class Joro:

    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 30.0  # Km/Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.hp = 10
        self.skilgage = 0
        self.x = 80
        self.y = 440
        self.frame = 0
        self.runimage = load_image('image\\joro_run.png')
        self.jumpimage = load_image('image\\joro_jump.png')
        self.attackimage = load_image('image\\joro_attack.png')
        self.crushimage = load_image('image\\joro_crush.png')
        self.skillimage = load_image('image\\joro_skill.png')
        self.state = 0 # 0은 달리기 1은 점프
        self.jumpstate = 0
        self.attackstate = 0
        self.crushstate = 0
        self.skillstate = 0

        self.eat_hp_sound = load_wav('bgm\\eat_hp.wav')
        self.eat_hp_sound.set_volume(50)

        self.eat_coin_sound = load_wav('bgm\\eat_coin.wav')
        self.eat_coin_sound.set_volume(50)

        self.eat_obstacle_sound = load_wav('bgm\\crush.wav')
        self.eat_obstacle_sound.set_volume(50)


        self.atk_sound = load_wav('bgm\\attack.wav')
        self.atk_sound.set_volume(50)

        self.jmp_sound = load_wav('bgm\\jump.wav')
        self.jmp_sound.set_volume(50)

        self.skill_sound = load_music('bgm\\joro_skill.mp3')
        self.skill_sound.set_volume(50)

    def update(self,frame_time):
        distance = Joro.RUN_SPEED_PPS * frame_time
        if (self.state == 0):
            if (self.y > 440):
                self.y = 440
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
            if (self.y <= 440):
                self.jumpstate = 0
                self.state = 0
        elif (self.state == 2):
            self.frame = (self.frame + 1) % 6
        elif (self.state == 3):  # 스킬
            self.frame = (self.frame + 1) % 6
        elif (self.state == -1):
            self.frame = (self.frame + 1) % 4

    def drawrun(self):
        self.runimage.clip_draw(self.frame * 160, 0, 160, 150, self.x, self.y)
    def drawjump(self):
        self.jumpimage.clip_draw(self.frame * 175, 0, 150, 200, self.x, self.y)
    def drawattack(self):
        self.attackimage.clip_draw(self.frame * 188, 0, 180, 200, self.x+10, self.y+15)
    def drawcrush(self):
       self.crushimage.clip_draw(self.frame*172,0,172,140,self.x,self.y)
    def drawskill(self):
        self.skillimage.clip_draw(self.frame*250,0,250,167,self.x,self.y)

    def get_bb(self):
        return self.x - 10, self.y - 40, self.x + 30, self.y + 50

    def get_bb_attack(self):
        if(self.state == 2):
            return self.x-10,self.y-20, self.x+80,self.y+50
    def get_bb_skill(self):
        if(self.state == 3):
            return self.x-10,self.y-100, self.x+450,self.y+200


    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw_bb_attack(self):
        if (self.state == 2):
            draw_rectangle(*self.get_bb_attack())

    def draw_bb_skill(self):
        if (self.state == 3):
            draw_rectangle(*self.get_bb_skill())


    def eat_hp(self):
        self.eat_hp_sound.play()

    def eat_coin(self):
        self.eat_coin_sound.play()

    def eat_obstacle(self):
        self.eat_obstacle_sound.play()

    def attack_sound(self):
        self.atk_sound.play()
    def jump_sound(self):
        self.jmp_sound.play()
    def skill_sound(self):
        self.skill_sound.play()