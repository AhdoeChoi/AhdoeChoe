import random
from pico2d import *
class EnergyUp:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km/Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None
    def __init__(self):
        self.x = 500*random.randint(1,30)
        self.y = 430
        if EnergyUp.image == None:
            EnergyUp.image  = load_image('image\\energy.png')
    def update(self,frame_time):
        distance = EnergyUp.RUN_SPEED_PPS * frame_time
        self.x -= distance

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())