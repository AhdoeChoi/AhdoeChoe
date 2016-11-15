from pico2d import *
import random

class CoinUp:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km/Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None
    def __init__(self):
        self.x = 50*random.randint(1,400)
        self.y = 50*math.cos(3*self.x) + 430
        if CoinUp.image == None:
            CoinUp.image   = load_image('image\\coin.png')
    def update(self,frame_time):
        distance = CoinUp.RUN_SPEED_PPS * frame_time
        self.x -= distance

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())