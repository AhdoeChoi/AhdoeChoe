import random
from pico2d import *

class ObstacleUp:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km/Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    image = None
    def __init__(self):
        self.x = 300 * random.randint(10,100)
        self.y = 380
        if ObstacleUp.image == None:
            ObstacleUp.image   = load_image('image\\obstacle.png')
    def draw(self):
        self.image.draw(self.x,self.y)
    def update(self,frame_time):
        distance = ObstacleUp.RUN_SPEED_PPS * frame_time
        self.x -= distance
    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())