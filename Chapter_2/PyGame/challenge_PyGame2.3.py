import pygame
from M_Dawson_Home_Work.Chapter_2.PyGame.settings3 import *
import M_Dawson_Home_Work.Chapter_2.PyGame.functions3 as f

from pygame.sprite import Group


def run_main():
    clock = pygame.time.Clock()
    pygame.init()
    stg = Settings()
    pygame.display.set_caption('Автодилер')
    screen = pygame.display.set_mode((stg.screen_width, stg.screen_height))
    # групирую по порядку как на экране
    label = Label(screen, 'Сколько денег на авто?', x=10, y=10, width=300)
    input_box = InputBox(screen, the='word', y=70)
    label1 = Label(screen, 'Налог : ', the='tax',  x=10, y=130, width=370)
    label2 = Label(screen, 'НДФЛ : ', the='reg_fee', x=10, y=190, width=370)
    label3 = Label(screen, 'Агентский сбор : ', the='agency_fee',  x=10, y=250, width=370)
    label4 = Label(screen, 'Доставка : ', the='delivery',  x=10, y=310, width=370)
    label5 = Label(screen, 'Итого : ', the='tax_all', x=10, y=370, width=370)
    # отдельностоящая кнопка
    button = Button(screen, 'Составить договор')
    # все лэйблы группа
    labels = Group()
    labels.add(label, label1, label2, label3, label4, label5)
    image = Image(screen)

    while True:
        f.check_event(input_box, button, labels, image)
        f.update_screen(stg, screen, input_box, button, labels,image)
        # желаемое число кадров в секунду
        clock.tick(20)

if __name__ == '__main__':
    run_main()