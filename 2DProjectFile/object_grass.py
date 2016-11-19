from pico2d import *


class Grass:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km/Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.x = 0
        self.image = load_image('image\\grass.jpg')
        self.bgm = load_music('bgm\\PlayMusick.mp3')
        self.bgm.set_volume(34)
        self.bgm.repeat_play()
    def draw(self):
        self.image.draw(1400-self.x,30)
        self.image.draw(1400-self.x,330)
    def update(self,frame_time):
        distance = Grass.RUN_SPEED_PPS * frame_time
        self.x += distance
        if (self.x > 1700):
            self.x = 0