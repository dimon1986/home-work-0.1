import sys
import pygame


def help_w(stg, gui, record_label):
    # отнимаем очки, если взяли подсказку
    # всего 2раза отнимаем, что бы 5 осталось:)
    if stg.tip == 15:
        record_label(gui, {4: f'Взял подсказку. Певая буква слова:',
                           5: f'{stg.correct[0]}{stg.long[1:]}'})
        stg.tip -= 5
    elif stg.tip == 10:
        record_label(gui, {4: f'Взял подсказку. Последняя буква слова:',
                           5: f'{stg.correct[0]}{stg.long[2:]}{stg.correct[-1:]}'})
        stg.tip -= 5
    else:
        record_label(gui, {6: f'Ты израсходовал все подсказки, что тебе ещё надо?'})


def record_label(gui, data, clean=None, ):
    """функция НЕ очищает лейблы поумолчанию
    принимает номер строки-лейбла и сообщение, 
    и их записывает"""
    if clean == 'clean':
        for i, elm in enumerate(gui.sprites()):
            # по умолчанию линк нан, поэтому проверяю тип и сравниваю
            if isinstance(elm.link, str):
                if elm.link[0:5] == f'label':
                    elm.txt = ''
    # разбивает словарь на номер строки и сообщение, вписывая его
    for number, msg in data.items():
        for elm in gui.sprites():
            if elm.link == f'label{number}':
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


def choice_gm(stg, v=''):
    """функция проверяет какое сейчас гуи отображать,
    выводит приветствия в лейблы-текстэдит"""
    gui = stg.who_gui()
    if v == 'anagram':
        # просто выводим текст в импровезированный текс эдит
        record_label(gui, {0: f'Добро пожаловать в игру Анаграммы!!',
                           1: f'Надо переставить буквы так, чтобы получилось слово.',
                           2: f'Если нужна помощь так и пишите.',
                           3: f'Вот анаграмма: {stg.jumble}'},
                     clean='clean')
    else:
        record_label(gui, {0: f'Добро пожаловать в игру Отгадай Слово!!',
                           1: f'Если нужна помощь так и пишите.',
                           2: f'Вот длинна слова: {len(stg.correct)}',
                           3: f'Его вид {stg.long}'},
                     clean='clean')


def check_deem(default_v, value):
    """функция просто проверяет на корректность значения старта,конца и шага"""
    try:  # если степ введён, то его читаем, инече по умолчанию
        deem_value = int(value)
    except ValueError:
        deem_value = default_v
    return deem_value


def deem_run(gui, record_label, start=0, end=10, step=1, ):
    """по сути просто range только с интерактивностью"""
    for elm in gui.sprites():
        if elm.the == 'input' and elm.link != 0:
            if elm.link == 1:
                start = check_deem(start, elm.txt)
            elif elm.link == 2:
                end = check_deem(end, elm.txt)
            elif elm.link == 3:
                step = check_deem(step, elm.txt)
    try:
        # если конец меньше начала, то шаг делаем отрицательный
        if end < start:
            step = - step
        # порядок всех чисел - генерируем список
        order = [i for i in range(start, end, step)]
        # меняю тип на строку
        msg = str(order)
        # удаляю скобки
        msg = msg[1:-1]
        # если длиннее 60 символов сокращаю
        order_print = msg[:60]
        # вносим в лейбл номер 6
        record_label(gui, {6: f'{order_print}'})
        # если не то ввели
    except ValueError:
        record_label(gui, {6: f'Введи целочисленное значение!'})


def guess_check(txt, stg, gui, record_label):
    """проверка на входит ли, поздравления если выиграл
    вызов помощи и вывод сообщения если не входит"""
    guess = txt.lower()
    # проверяет вдотит ли буква, то изменяем лонг, что бы звезды стали буквами
    if guess in stg.correct:
        new = ''
        for i in range(len(stg.correct)):
            if guess == stg.correct[i]:
                new += guess
            else:
                new += stg.long[i]
        stg.long = new
        # говорим входит и новый вид слова
        record_label(gui, {3: f'Входит в состав слова.',
                           4: f'Загаданное слово сейчас выглядит так: {stg.long}'},)
    # если ответ равен коретку или лонг корректу то конец и поздравления
    if guess == stg.correct or stg.long == stg.correct:
        record_label(gui, {0: f'Да, именно так! Вы отгадали!',
                           1: f'Слово было: {stg.correct.upper()}',
                           2: f'Вы набрали {stg.tip} очков.',
                           3: f'Можете потратить их на поёздку на море.',
                           4: f'Спасибо за игру.'},
                     clean='clean')
    elif guess == 'помощь':  # всё как обычно помощь
        help_w(stg, gui, record_label)
    elif guess not in stg.correct:  # если не входит
        record_label(gui, {5: f'К сожалению, такой буквы нет.'},)


def anagram_check(txt, stg, gui, record_label):
    """проверка на коррект, если да то поздравляем,
    вызов помощи и надпись что вы не правы"""
    guess = txt.lower()
    if guess == stg.correct:
        record_label(gui, {0: f'Да, именно так! Вы отгадали!',
                           1: f'Слово было: {stg.correct.upper()}',
                           2: f'Вы набрали {stg.tip} очков.',
                           3: f'Можете потратить их на поёздку на море.',
                           4: f'Спасибо за игру.'},
                     clean='clean')
    if guess == 'помощь':
        help_w(stg, gui, record_label)
    elif guess != stg.correct:
        record_label(gui, {4: f'К сожалению, вы не правы.'})


def default_lbl(gui):
    """сушествует для единственного действия
    вернуть лейблам названия по умолчанию
    используется в Посчитать"""
    for elm in gui.sprites():
        if elm.the == 'lbl':
            elm.txt = elm.default


def check_gui(stg, gui, mouse_x, mouse_y, input_box0,):
    """если колизия есть и она не с картинкой, то актив Тру,
    цвет, фон, обводка меняются, если нет, то фолс."""
    for elm in gui.sprites():
        if elm.rect.collidepoint(mouse_x, mouse_y) and elm.the != 'img':
            elm.active = True
        else:
            elm.active = False
    # не нравиться мне фор, вдруг памяти всех обходить -много, думаю словарь попробывать
    for elm in gui.sprites():
        # проверка нажали ли на кнопку, если да, то узнаем что на ней написанно
        # далее совершаем соответствующие функции
        clicked = elm.rect.collidepoint(mouse_x, mouse_y)
        if clicked and elm.the == 'btn':
            # логика действия для нажатых кнопок дроида и смерти
            if elm.txt == 'Посчитать':
                stg.revers(elm.txt)  # запуск одной игры и отключение другой(для отображения елмнтов)
                default_lbl(gui)
            elif elm.txt == 'Анаграммы':
                stg.revers(elm.txt)
                stg.load_word()
                stg.create_jumble_word(stg.correct)
                choice_gm(stg, 'anagram')
            elif elm.txt == 'Отгадай':
                stg.revers(elm.txt)
                stg.load_word()
                choice_gm(stg,)
            elif elm.txt == 'Сказать' and input_box0.txt and stg.deem_active:
                # просто отзеркаливаем
                record_label(gui, {6: input_box0.txt[::-1]})
            elif elm.txt == 'Сказать' and input_box0.txt and stg.anagram_active:
                # функция проверки ввода
                anagram_check(input_box0.txt, stg, gui, record_label)
            elif elm.txt == 'Сказать' and input_box0.txt and stg.guess_active:
                # функция проверки ввода
                guess_check(input_box0.txt, stg, gui, record_label)
            elif elm.txt == 'Старт' and stg.deem_active:
                # расчёт
                deem_run(gui, record_label)


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


def check_event(stg, input_box0, gui,):
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
            check_gui(stg, gui, mouse_x, mouse_y, input_box0,)
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
        # каждый элемент рисуем, хоть это и расточительно(наверно)
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
