import pygame
from M_Dawson_Home_Work.Chapter_2.PyGame.settings1_2 import *
import M_Dawson_Home_Work.Chapter_2.PyGame.functions1_2 as f

from pygame.sprite import Group


def run_main():
    clock = pygame.time.Clock()
    pygame.init()
    stg = Settings()
    pygame.display.set_caption('Два блюда & цена')
    screen = pygame.display.set_mode((stg.screen_width, stg.screen_height))
    # инициация всех объектов
    label = Label(screen, 'Впишите блюда', x=10, y=10, width=300)
    input_box = InputBox(screen, the='word', y=70)
    input_box1 = InputBox(screen, the='word', y=130)
    label1 = Label(screen, the='words', y=190)
    # the - не очень нравитья, но лучше не придумал
    label2 = Label(screen, 'Сколько будем тратить?', x=10, y=250, width=300)
    input_box2 = InputBox(screen, the='input_digit', y=310)
    input_boxes = Group()
    input_boxes.add(input_box, input_box1, input_box2)
    # числовые лейблы
    label3 = Label(screen, the='digit', y=370)
    label4 = Label(screen, the='digit1', y=430)

    gui = Group()
    button = Button(screen, 'СклеитьСтроки', x=375, y=70, width=200)
    button1 = Button(screen, 'Чаевые', x=375, y=310, width=200)
    gui.add(button, button1)

    labels = Group()
    labels.add(label, label1, label2, label3, label4)

    while True:
        f.check_event(input_boxes, gui, labels)
        f.update_screen(stg, screen, input_boxes, gui, labels)
        # желаемое число кадров в секунду
        clock.tick(20)

if __name__ == '__main__':
    run_main()
