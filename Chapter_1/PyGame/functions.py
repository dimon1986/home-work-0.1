import sys
import pygame


def check_keydown_events(event, input_boxes):
    """Реагирует на нажатие клавишь."""
    if event.key == pygame.K_ESCAPE:  # вместо enter привычнее esc:)
        sys.exit()
    if event.type == pygame.KEYDOWN:  # любая клавиша на клаве
        for input_box in input_boxes.sprites():  # для каждого бокса входящего в инпуты
            if input_box.active:  # если он активный
                if event.key == pygame.K_RETURN:  # нажимаем ввод и печатается текст который в инпуте
                    # можем допустим добавить имя в рекорды
                    print(input_box.txt)
                    input_box.txt = ''  # очищаем его, раз напечатали
                elif event.key == pygame.K_BACKSPACE:  # строка это последовательность, а раз так
                    input_box.txt = input_box.txt[:-1]  # удаляем последнее значение бэкспейсом
                else:
                    input_box.txt += event.unicode   # конкатенация
                # рендерим текст и отправляем на экран.
                input_box.txt_rect = input_box.font.render(input_box.txt, True, input_box.color)


def check_play_button(gui, image_all, input_boxes, mouse_x, mouse_y):
    """Проверяет нажатие кнопок и инпутбокса"""
    # для каждого бокса входящего в инпуты
    for input_box in input_boxes.sprites():
        # сразу на проверку коллизии
        if input_box.rect.collidepoint(mouse_x, mouse_y):
            # если да включаем флаг актив
            input_box.active = True
        else:
            input_box.active = False  # впротивном выключаем
        # интересный способсменить цвет, цвет меняется если активный и меняется на другой если не ативный
        input_box.color = input_box.COLOR_ACTIVE if input_box.active else input_box.COLOR_INACTIVE
    # для каждой кнопки входящий в гуи
    for button in gui.sprites():
        # до этого так делал, вдруг куда передать да иболе явно, хоть чуток длинне
        button_clicked = button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked:
            if button.msg == '#1':
                image_all.image = pygame.image.load(f"{image_all.dict_image['ice_b']}")
            elif button.msg == '#2':
                image_all.image = pygame.image.load(f"{image_all.dict_image['ice_c']}")
            elif button.msg == '#3':
                image_all.image = pygame.image.load(f"{image_all.dict_image['ice_ch']}")
            elif button.msg == '#4':
                image_all.image = pygame.image.load(f"{image_all.dict_image['ice_s']}")
            elif button.msg == 'Очистить':
                # очищаем текст
                for input_box in input_boxes.sprites():
                    input_box.txt = ''
                    # а затем обновляем рисунок текста на экране
                    input_box.txt_rect = input_box.font.render(input_box.txt, True, input_box.color)


def pos_button(gui, mouse_x, mouse_y):
    """Проверяет находиться ли мышка над клавишой
    и изменяет флаг"""
    for button in gui.sprites():  # для каждой кнопки входяший в гуи
        button_pos = button.rect.collidepoint(mouse_x, mouse_y)  # проверка на наличие коллизий(есть или нет 1:0)
        if button_pos:
            button.pos_button_hover = True  # если кнопка над мышкой то флаг переключается на тру
        else:
            button.pos_button_hover = False  # иначе флаг переключается на фолс


def check_events(gui, image_all, input_boxes):
    # Отслеживание событий клавиатуры и мыши.
    for event in pygame.event.get():
        # тут всё ясно, выходим если нажимаем на крестик
        if event.type == pygame.QUIT:
            sys.exit()
        # просто когда держим мышку над объектом
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()  # просто два инта
            pos_button(gui, mouse_x, mouse_y)  # для функции
        # если нажали на мышку
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()  # х и у её, улитают другой функции
            check_play_button(gui, image_all, input_boxes, mouse_x, mouse_y)
        # для проверки нажалили нужную кнопку клавиатуры
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, input_boxes)


def update_screen(ai_setting, screen, gui, image_all, input_boxes):
    """Обновляет изображения на экране и отображает новый экран."""
    # При каждом проходе цикла перерисоввывается экран
    screen.fill(ai_setting.bg_color)  # задник заливается
    for button in gui.sprites():
        button.draw_button()  # каждая кнопка отрисовывается
        if button.pos_button_hover:  # пороверяем кнопку на флаг
            button.update()  # если над кнопкой мышка, то по особенному отрисовывается
    for input_box1 in input_boxes.sprites():
        input_box1.draw()  # просто отрисовывается поле ввода
        if input_box1.active:
            input_box1.update()  # если оно активно, меняется цвет и текст
    # просто отрисовывается картинка
    image_all.blitme()
    # Отображение последнего прорисованного экрана, без него будет черный экран:)
    pygame.display.flip()
