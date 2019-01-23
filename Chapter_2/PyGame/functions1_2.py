import sys
import pygame


def print_word(input_boxes, labels):
    """опустошает лейбл со словами, создает новые слова и выводит их на экран"""
    for label in labels.sprites():
        if label.the == 'words':
            label.txt = ''
            for box in input_boxes.sprites():
                if box.the == 'word':
                    label.txt += box.txt
                    label.txt_rect = label.font.render(label.txt, True, (250, 180, 150))


def digit(input_boxes, label, number):
    """для каждого инпута, который диджит
    производит преобразование, расчёт и вывод на экран(рендер)"""
    label.txt = ''
    for box in input_boxes.sprites():
        if box.the == 'input_digit':
            try:
                num = int(box.txt)
                j = num * number
                label.txt += f'Итого за обед +{int(number*100)} % на чай : ' + str(num + j)
                label.txt_rect = label.font.render(label.txt, True, (250, 180, 150))
            except ValueError:
                label.txt += 'Ошибка ввода'
                label.txt_rect = label.font.render(label.txt, True, (250, 180, 150))


def print_int(input_boxes, labels):
    """дилигирует digit, передевая различные пораметры,
    в зависимости от the"""
    for label in labels.sprites():
        if label.the == 'digit':
            digit(input_boxes, label, 0.1)
        elif label.the == 'digit1':
            digit(input_boxes, label, 0.2)


def check_gui(input_boxes, buttons, labels, mouse_x, mouse_y):
    """регестрирует коллизии мышки с инпутом, кнопками
    и производит для них согласно их логики"""
    for box in input_boxes.sprites():
        if box.rect.collidepoint(mouse_x, mouse_y):
            box.active = True
        else:
            box.active = False
        box.color = box.COLOR_ACTIVE if box.active else box.COLOR_INACTIVE
    # для каждой кнопки входящий в гуи
    for button in buttons.sprites():
    # до этого так делал, вдруг куда передать да иболе явно, хоть чуток длинне
        button_clicked = button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked:
            if button.txt == 'СклеитьСтроки':
                print_word(input_boxes, labels)
            elif button.txt == 'Чаевые':
                print_int(input_boxes, labels)


def delete_txt(box):
    """функция удаляет текст и обновляет картинку"""
    box.txt = box.txt[:-1]
    box.txt_rect = box.font.render(box.txt, True, box.color)


def key_down_events(event, input_boxes):
    """проверяет какие клавиши нажаты на клаве
    и совершает определенные действия:выход, удаление, добавление тхт"""
    if event.key == pygame.K_ESCAPE:
        sys.exit()
    if event.type == pygame.KEYDOWN:
        for box in input_boxes.sprites():
            if box.active:
                if event.key == pygame.K_BACKSPACE:
                    box.backspace = True
                else:
                    box.txt += event.unicode
                box.txt_rect = box.font.render(box.txt, True, box.color)


def pos_button(buttons, mouse_x, mouse_y):
    """Проверяет находиться ли мышка над клавишой
    и изменяет флаг"""
    for button in buttons.sprites():  # для каждой кнопки входяший в гуи
        button_pos = button.rect.collidepoint(mouse_x, mouse_y)  # проверка на наличие коллизий(есть или нет 1:0)
        if button_pos:
            button.hover = True  # если кнопка над мышкой то флаг переключается на тру
        else:
            button.hover = False  # иначе флаг переключается на фолс


def check_event(input_boxes, buttons, labels):
    """события: выхода, мышка над кнопкой, нажатие на мышку,
    нажатие на клавиши, подъём клвиш"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()  # просто два инта
            pos_button(buttons, mouse_x, mouse_y)  # для функции
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_gui(input_boxes, buttons, labels, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            key_down_events(event, input_boxes)
        # решил не делать отдельной функции, так тоже не спагетти
        elif event.type == pygame.KEYUP:
            for box in input_boxes.sprites():
                if box.active:
                    if event.key == pygame.K_BACKSPACE:
                        box.backspace = False


def update_screen(stg, screen, input_boxes, buttons, labels):
    """просто обновление экрана, фон, инпуты, кнопки, лейблы"""
    screen.fill(stg.bg_color)
    for box in input_boxes.sprites():
        if box.backspace:
            # отправляем где будем удалять текст
            delete_txt(box)
        box.draw()
    for button in buttons.sprites():
        button.draw_button()
        if button.hover:  # пороверяем кнопку на флаг
            button.update()  # если над кнопкой мышка, то по особенному отрисовывается
    for label in labels.sprites():
        label.draw()
    pygame.display.flip()
