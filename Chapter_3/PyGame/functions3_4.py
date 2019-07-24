import sys
import pygame
import random


def mind_check(stg, gui, record_label, answer):
    """функция проверки разума, основные расчёты"""
    def step(one):
        """функция шага ван оставил для ветвления"""
        stg.attempt += 1  # шаг прибавляем
        if one == 1:
            # поднимаем нижнию границу, что бы разброс был меньше
            stg.low = stg.rand_digit + one
        else:
            # прибавляем минус один :)
            stg.high = stg.rand_digit + one
        # делаем рондом, по новой
        stg.rand_digit = random.randint(stg.low, stg.high)
        # вписываем в четверный лейбл
        record_label(gui, f'это цыфра {stg.rand_digit}?', 3)

    if answer == 'Верно':
        stg.attempt += 1  # шаг прибавляем
        stg.run_two = False  # останавливаем игру и вписываем поздравления
        record_label(gui, 'Ура РС отгадал!', 0)
        record_label(gui, f'Всего за {stg.attempt} шагов.', 1)
        record_label(gui, 'Быстрый как i7.', 2)
        if stg.attempt > 5:  # шаги, есби больше 5 прибавляем надпись
            record_label(gui, 'Быстрый как i386.', 2)
    else:
        # проверка на что нажали, проверка что бы из пределов не выходить + шаг
        if answer == 'Больше':
            if stg.high > stg.rand_digit:
                step(1)
        if answer == 'Меньше':
            if stg.low < stg.rand_digit:
                step(-1)


def death_check(stg, gui, record_label):
    """главная функция смерти"""
    record_label(gui, f'{stg.answer}', 3)  # вписываем ответ пользователя
    if stg.attempt < 5:  # проверяем не потратили бы мы все попытки
        stg.attempt += 1  # шаг прибавляем
        if stg.answer == stg.rand_digit:  # сначало проверку, на отгдал или нет
            record_label(gui, f'Отсрочил смерть.', 0)
            record_label(gui, f'Действительно: {stg.rand_digit}', 1)
            record_label(gui, f'Попыток: {stg.attempt}', 2)
            record_label(gui, f'Я вернусь сюда.', 3)
        # тут всё ясно поровеки больше или меньше наш ответ
        if stg.answer < stg.rand_digit:
            record_label(gui, f'Значение больше!', 0)
            record_label(gui, f'попытка номер {stg.attempt}', 1)
        if stg.answer > stg.rand_digit:
            record_label(gui, f'Значение меньше.', 0)
            record_label(gui, f'попытка номер {stg.attempt}', 1)
    else:
        if stg.answer == stg.rand_digit:
            # если дал ответ и он верен был, но попытки кончились
            record_label(gui, f'Да это так...', 0)
            record_label(gui, f'Но ты опоздал', 1)
        else:
            # про каждого из нас скажут "ты был":)
            record_label(gui, f'Ты был...', 0)
            record_label(gui, f'Число было: {stg.rand_digit}', 1)
        stg.run = False  # активность первой игры ставим фолс
        record_label(gui, 'Ты проиграл.', 2)


def record_label(gui, msg='', j=777):
    """с помщю данной функции записываем лейблы
    принимает сообщение и номер строки-лейбла
    а так же очищает лейблы если 777"""
    for elm in gui.sprites():
        if elm.link == 'speech' and j == 0:
            elm.txt = msg
        if elm.link == 'speech1' and j == 1:
            elm.txt = msg
        if elm.link == 'speech2' and j == 2:
            elm.txt = msg
        if elm.link == 'speech3' and j == 3:
            elm.txt = msg
    if j == 777:
        for elm in gui.sprites():
            if elm.link == 'speech':
                elm.txt = msg
            if elm.link == 'speech1':
                elm.txt = msg
            if elm.link == 'speech2':
                elm.txt = msg
            if elm.link == 'speech3':
                elm.txt = msg
            if elm.link == 'speech4':
                elm.txt = msg


def pos_button(gui, mouse_x, mouse_y):
    """Проверяет находиться ли мышка над элементом
    и изменяет флаг"""
    for elm in gui.sprites():  # для каждой кнопки входяший в гуи
        button_pos = elm.rect.collidepoint(mouse_x, mouse_y)  # проверка на наличие коллизий(есть или нет 1:0)
        if button_pos:
            elm.hover = True  # если мышка над элементом то флаг переключается на тру
        else:
            elm.hover = False  # иначе флаг переключается на фолс


def choice_gm(stg, gui, v):
    """просто два вида для записи в лейблы
    в начале игры"""
    record_label(gui,)  # очищаем все лейблы
    if v == 'death':
        stg.run_game()
        # отмечаем запущинно то или иная игра
        stg.run = True
        stg.run_two = False
        record_label(gui, f'Я загадал число', 0)
        record_label(gui, f'от {stg.low} до {stg.high}', 1)
        record_label(gui, 'Каков Ответ?', 2)
    else:
        stg.run_game()
        stg.run_two = True
        stg.run = False
        record_label(gui, f'Загадай число', 0)
        record_label(gui, f'от {stg.low} до {stg.high}', 1)
        record_label(gui, '<--Нажимай ответ', 2)
        record_label(gui, f'это цыфра {stg.rand_digit}?', 3)


def clicked_label(stg, gui, elm,):
    """два варианта действия для старта
    и три варианта ответа для наставления андроида"""
    if elm.txt == 'Старт' and stg.death_active:
        choice_gm(stg, gui, 'death')
    elif elm.txt == 'Старт' and stg.droid_active:
        choice_gm(stg, gui, 'droid')
    # дроид отправляем проверку разума
    elif elm.txt == 'Больше' and stg.droid_active:
        mind_check(stg, gui, record_label, elm.txt)
    elif elm.txt == 'Меньше' and stg.droid_active:
        mind_check(stg, gui, record_label, elm.txt)
    elif elm.txt == 'Верно' and stg.droid_active:
        mind_check(stg, gui, record_label, elm.txt)


def check_gui(stg, gui, mouse_x, mouse_y, input_box,):
    """если колизия есть и она не с картинкой, то актив Тру,
    цвет, фон, обводка меняются, если нет, то фолс.
    """
    for elm in gui.sprites():
        if elm.rect.collidepoint(mouse_x, mouse_y) and elm.the != 'img':
            elm.active = True
        else:
            elm.active = False
    # НАМ НУЖНО ЧТО БЫ СНАЧАЛА АКТИВ ТРУ ПОЯВИЛОСЬ У ИНТЕРЕСУЮЩЕГО НАС ОБЪЕКТА
    # ТАК КАК ЕСЛИ ОН ТРУ ТО СРАБАТЫВАЕТ ДРУГОЙ ОБЪЕКТ ^_^
    for elm in gui.sprites():
        # проверка нажали ли на кнопку, если да, то узнаем что на ней написанно и отправляем gui дальше
        clicked = elm.rect.collidepoint(mouse_x, mouse_y)
        if clicked:
            if elm.the == 'lbl':
                # радиляй и влавствуй:)
                clicked_label(stg, gui, elm, )
            if elm.the == 'btn':
                # логика действия для нажатых кнопок дроида и смерти
                if elm.txt == 'Дроид':
                        record_label(gui,)  # запись лейблов
                        stg.revers(elm.txt)  # запуск одной игры и отключение другой(для отображения елмнтов)
                if elm.txt == 'Смерть':
                        record_label(gui,)
                        stg.revers(elm.txt)
                if stg.run:
                    if elm.txt == 'Сказать' and input_box.txt:
                        # если преобразование прошло, опусташаем инпут и в проверку смерти
                        try:
                            stg.answer = int(input_box.txt)
                            input_box.txt = ''
                            death_check(stg, gui, record_label)
                        except ValueError:
                            record_label(gui, f'Не пиши чушь.', 3)
                            input_box.txt = ''


def key_down_events(gui, event):
    """всё как обычно нажал кнопку, получи гранату,
    проверка на инпут, включаем бекспейс или записываем текст"""
    if event.key == pygame.K_ESCAPE:
        # ескейп и выходим
        sys.exit()
    if event.type == pygame.KEYDOWN:
        for elm in gui.sprites():
            # если активин элемент и он является инпутом
            if elm.active and elm.the == 'input':
                # если кей бэкспейс,то флаг Тру
                if event.key == pygame.K_BACKSPACE:
                    elm.backspace = True
                else:
                    # инече добовляем текст юникода а тхт
                    elm.txt += event.unicode
                # отрисовываем тхт
                elm.draw_txt()


def check_event(stg, gui, input_box,):
    """события: выхода, мышка над элементом, нажатие на мышку,
    нажатие на клавиши, подъём бэкспйса"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()  # просто два инта
            pos_button(gui, mouse_x, mouse_y)  # передаём гуи и позицию мышки
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_gui(stg, gui, mouse_x, mouse_y, input_box,)
        elif event.type == pygame.KEYDOWN:
            key_down_events(gui, event)
        elif event.type == pygame.KEYUP:
            for elm in gui.sprites():
                if elm.the == 'input':
                    if event.key == pygame.K_BACKSPACE:
                        # меняем его на лож, что бы не удалялось
                        elm.backspace = False


def update_screen(stg, screen, gui):
    # вставляем бэкграунд
    screen.fill(stg.bg_color)
    for elm in gui.sprites():
        # каждый элемент рисуем, хоть это и расточительно
        elm.draw()
        # если над элеменком мышка, то по особенному отрисовывается поверх прежних
        if elm.hover:
            elm.update_is_hover()
        # если активен(нажат) элемент, то по особому отрисовывается
        if elm.active:
            elm.update_is_active()
        # если инпут с активным бэкспейсом, то удаляем последней элемент
        if elm.the == 'input':
            if elm.backspace:
                # удаяем последний элемент, если бэкспйс есть
                elm.txt = elm.txt[:-1]
        # просто если картинка, то тоже собственый метод отрисовки
        if elm.the == 'img':
            elm.draw_img()
    pygame.display.flip()
