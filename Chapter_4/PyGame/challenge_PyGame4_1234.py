from pygame.sprite import Group
from M_Dawson_Home_Work.Chapter_4.PyGame.settings1234 import *
import M_Dawson_Home_Work.Chapter_4.PyGame.functions1234 as f


def run_main():
    pygame.init()  # инициируем пайгейм
    clock = pygame.time.Clock()  # создаём для нужно чистаты кадров
    stg = Settings()  # обект для актуальных состояний игры, значений
    pygame.display.set_caption('Посчитать & Анаграммы & Отгадай')
    screen = pygame.display.set_mode((stg.screen_width, stg.screen_height))
    # разделил на три группы
    deem_gui = Group()
    anagram_gui = Group()
    guess_gui = Group()
    # периключаем игры и запускаем их если возможно
    button0 = Button(screen, txt='Посчитать',)
    button1 = Button(screen, txt='Анаграммы', x=185,)
    button2 = Button(screen, txt='Отгадай', x=295, )
    # инпут для реверса и ответа в двух играх
    input_box0 = InputBox(screen, link=0, size=14, x=420, y=300, height=50)
    # кнопка которая совершает отправку и проверку
    button3 = Button(screen, txt='Сказать', x=420, y=350, width=200,)
    # посчитать
    button4 = Button(screen, txt='Старт', x=420, y=400, width=200, )
    # лейблы - посути строки, текст эдит
    label0 = Label(screen, link='label0', txt='Начальное (по умолчанию 0)', y=70)
    label1 = Label(screen, link='label1', y=95)
    label2 = Label(screen, link='label2', txt='Конечное (по умолчанию 10)', y=120)
    label3 = Label(screen, link='label3',  y=145)
    label4 = Label(screen, link='label4', txt='Шаг (по умолчанию 1)', y=170)
    label5 = Label(screen, link='label5',  y=195)
    label6 = Label(screen, link='label6',  y=220)
    # три инпута вместо лейбл1 лейбл3 лейбл5
    input_box1 = InputBox(screen, link=1, y=105, )
    input_box2 = InputBox(screen, link=2, y=155, )
    input_box3 = InputBox(screen, link=3, y=205, )

    # одна картинка, просто белый квадрат
    image0 = Image(screen, x=70, width=545, )
    # в данном исполнеение, по слоям отрисовывается
    # так что первое раньше отрисовывается
    deem_gui.add(button0, button1, button2, button3, button4, image0,

                 input_box1, input_box2, input_box3, input_box0,
                 label0,  label2,  label4,  label6, )
    # так что первое раньше отрисовывается
    anagram_gui.add(button0, button1, button2, button3, input_box0, image0,
                  label0, label1, label2, label3, label4, label5, label6, )
    # отрисовывается если активна загадка
    guess_gui.add(button0, button1, button2, button3, input_box0, image0,
                  label0, label1, label2, label3, label4, label5, label6, )

    stg.dict_element['deem_gui']=deem_gui
    stg.dict_element['anagram_gui'] = anagram_gui
    stg.dict_element['guess_gui'] = guess_gui

    while True:
        gui = stg.who_gui()
        # проверка событий
        f.check_event(stg, input_box0, gui,)
        # обновление экрана
        f.update_screen(stg, screen, gui,)
        # данная функция более точна, хотя чуть больше использует процессор
        clock.tick_busy_loop(30)

if __name__ == '__main__':
    run_main()
