import sys
import pygame


def price_car(input_box, image):
    """подставляем нужную картинку из словаря"""
    try:
        num = int(input_box.txt)
        if num >= 400000:
            image.image = pygame.image.load(f"{image.dict_image['car_c']}")
        elif num >= 200000:
            image.image = pygame.image.load(f"{image.dict_image['car_b']}")
        elif num > 10000 < 50000:
            image.image = pygame.image.load(f"{image.dict_image['car_a']}")
    except ValueError:
        image.image = pygame.image.load(f"{image.dict_image['car']}")


def digit(input_box, label, number):
    """сам главный расчёт всех такс, чтение инпута"""
    label.txt = label.default  # считываем текст по умолчанию
    try:
        num = int(input_box.txt)  # считываем ввод
        j = num * number  # умножаем на чило которое мы передали
        #  isinstance -специально создана для проверки принадлежности данных определенному типу
        if isinstance(number, float) and label.the != 'tax_all':
            # прибавляем к тексту, число которое мы передали + число которое у нас получилось!
            label.txt += f'{int(number*100)} % : ' + str(int(j))
        elif isinstance(number, int):
            # если номер инт, преобразуем и конкатенацыя
            label.txt += str(number)
        else:
            # все расчёты, как есть
            label.txt += str(int(num + j + 2500))
        # вывод на экран, рендер текста
        label.txt_rect = label.font.render(label.txt, True, (250, 250, 250))
    except ValueError:
        label.txt += 'Ошибка ввода'
        label.txt_rect = label.font.render(label.txt, True, (250, 180, 150))


def print_int(input_box, labels):
    """проверяем значение the и передеём с заданнами параметрами
    в digit"""
    for label in labels.sprites():
        if label.the == 'tax':
            digit(input_box, label, 0.13)
        elif label.the == 'reg_fee':
            digit(input_box, label, 0.20)
        elif label.the == 'agency_fee':
            digit(input_box, label, 2000)
        elif label.the == 'delivery':
            digit(input_box, label, 500)
        elif label.the == 'tax_all':
            digit(input_box, label, 0.33)


def check_gui(input_box, button, labels, image, mouse_x, mouse_y):
    """вкл/отк активность у инпута, меняет ему цвет, проверяет нажимали кнопку
    если так меняем цену, картинку"""
    if input_box.rect.collidepoint(mouse_x, mouse_y):
        input_box.active = True
    else:
        input_box.active = False
    input_box.color = input_box.COLOR_ACTIVE if input_box.active else input_box.COLOR_INACTIVE
    button_clicked = button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        print_int(input_box, labels)
        price_car(input_box, image)


def pos_button(button, mouse_x, mouse_y):
    """Проверяет находиться ли мышка над клавишой
    и изменяет флаг"""
    button_pos = button.rect.collidepoint(mouse_x, mouse_y)  # проверка на наличие коллизий(есть или нет 1:0)
    if button_pos:
        button.hover = True  # если кнопка над мышкой то флаг переключается на тру
    else:
        button.hover = False  # иначе флаг переключается на фолс


def delete_txt(input_box):
    """функция удаляет текст и обновляет картинку"""
    input_box.txt = input_box.txt[:-1]
    input_box.txt_rect = input_box.font.render(input_box.txt, True, input_box.color)


def key_down_events(event, input_box):
    """всё как обычно нажал кнопку, получи гранату, (рендеринг)текста если напсисал"""
    if event.key == pygame.K_ESCAPE:
        sys.exit()
    if event.type == pygame.KEYDOWN:
        if input_box.active:
            if event.key == pygame.K_BACKSPACE:
                input_box.backspace = True
            else:
                input_box.txt += event.unicode
            input_box.txt_rect = input_box.font.render(input_box.txt, True, input_box.color)


def check_event(input_box, button, labels, image):
    """выход, мышь над, нажата мышь, нажата кнопка, поднята кнопка"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()  # просто два инта
            pos_button(button, mouse_x, mouse_y)  # для функции
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_gui(input_box, button, labels, image, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            key_down_events(event, input_box)
        # решил не делать отдельной функции, так тоже не спагетти
        elif event.type == pygame.KEYUP:
            if input_box.active:
                    if event.key == pygame.K_BACKSPACE:
                        input_box.backspace = False


def update_screen(stg, screen, input_box, button, labels, image):
    """обновляем бэкграунд, инпут, кнопку, лейблы, картинку и просто флип дисплея"""
    screen.fill(stg.bg_color)
    if input_box.backspace:
        delete_txt(input_box)
    input_box.draw()
    button.draw_button()
    if button.hover:  # пороверяем кнопку на флаг
        button.update()  # если над кнопкой мышка, то по особенному отрисовывается
    for label in labels.sprites():
        label.draw()
    image.blitme()
    pygame.display.flip()