import game_framework
from pico2d import *


import main_state
import title_state

name = "RankingState"
image = None
font = None

def enter():
    global image, font #global 안해놓으면 내부에서 선언한 변수는 지역변수처럼 취급됨 (다른곳에서 사용하질 못함) 다른곳에서 사용하고싶으면 global해줘야함
    image = load_image('board.png')
    font = load_font('ENCR10B.TTF',40)

def exit():
    global image
    del(image)

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
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(title_state)



def update():
    pass

def bubble_sort(data):
    for i in range(0 , len(data)):
        for j in range(i+1 , len(data)):
            if data[i]['Coin'] < data[j]['Coin']:
                data[i], data[j] = data[j], data[i]

def draw_ranking():

    f = open('data.txt', 'r')
    score_data = json.load(f)
    f.close()

    bubble_sort(score_data)

    font.draw(300,500, '[RANKING]',(0,0,0))
    y = 0
    for score in score_data[:4]:
        font.draw(100,400-40*y, 'TIME: %4.1f, Coin:%3d, Hp:%3d' %
          (score['Time'],
           score['Coin'],
           score['Hp']), (255,255,255))
        y += 1

def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    draw_ranking()
    update_canvas()