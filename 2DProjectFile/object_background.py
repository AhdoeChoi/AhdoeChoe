from pico2d import *
import random

class BackGround:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 0.2  # Km/Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    def __init__(self):
        self.image = load_image('image\\BackGround1.png')
        self.x = 0
        self.y = 0
    def draw(self):
        self.image.draw(400-self.x,300)
    def update(self,frame_time):
        distance = BackGround.RUN_SPEED_PPS * frame_time
        self.x += distance

        if (self.x > 250):
            self.x = 50