import game_framework
import main_state
from pico2d import *


name = "TitleState"
image = None
class TitleMusick:
    def __init__(self):
        self.x = 0
        self.image = load_image('image\\grass.jpg')
        self.bgm = load_music('bgm\\TitleMusick.mp3')
        self.bgm.set_volume(34)
        self.bgm.repeat_play()


def enter():
    global image,titlemusick
    image = load_image('image\\title.jpg')
    titlemusick = TitleMusick()

    #pass


def exit():
    global image
    del(image)
    #pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)
    #pass


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
    #pass







def update():
    pass


def pause():
    pass


def resume():
    pass






