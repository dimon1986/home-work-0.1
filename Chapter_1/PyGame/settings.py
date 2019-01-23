import pygame.font
import os
from pygame.sprite import Sprite


class Settings(object):
    """Класс для хранения ширины высоты и цвета экрана"""
    def __init__(self):
        """Инициализирует настройки игры."""
        self.screen_width = 640  # можно передавать другие значения и расширение меняется
        self.screen_height = 480
        self.bg_color = (20, 40, 140)


class Image(Sprite):
    """Класс для картинки, 
    и словарь с сылками на изображения"""
    def __init__(self, screen):
        super(Image, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        # блин почему раньше не сказали про такой путь очень удобно!
        self.dict_image = {'ice_b': os.path.abspath('data//ice_b.png'),
                           'ice_c': os.path.abspath('data//ice_c.png'),
                           'ice_ch': os.path.abspath('data//ice_ch.png'),
                           'ice_s': os.path.abspath('data//ice_s.png')}
        # загрузка изображениий мороженного
        self.image = pygame.image.load(f"{self.dict_image['ice_b']}")
        # получаем примоугольник картинки
        self.rect = self.image.get_rect()
        # задаём значения где должен быть центор его
        # и где его низ будет всё относительно экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """рисует картинку в тикущей позиции"""
        self.screen.blit(self.image, self.rect)


class InputBox(Sprite):
    """Класс поля ввода, принимает текст и преобразовывае его в картинку,
    ширина по х и высота по у, далее 2шт позиции на экране"""
    def __init__(self, screen, txt='',
                 x=10, y=10, width=620, height=50):
        super(InputBox, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # два значения цвета и актуальный цвет
        self.COLOR_INACTIVE = (235, 215, 115)
        self.COLOR_ACTIVE = (255, 255, 255)
        self.color = self.COLOR_INACTIVE
        # флаг для переключения цвета.
        self.active = False
        # Шрифт и его размер
        self.font = pygame.font.SysFont(None, 24)
        # принимаем проаметр текст далее его рендерим
        self.txt = txt
        self.txt_rect = self.font.render(txt, True, self.color)
        # создаем собствено сам квадрат, передав где находиться и широту и высоту
        self.rect = pygame.Rect(x, y, width, height)

    def update(self):
        # Если текст слишком длинный увеличиваем ширину поля ввода
        width_update = max(620, self.txt_rect.get_width() + 10)
        self.rect.width = width_update

    def draw(self):
        # передаем экрану рисунок текста
        self.screen.blit(self.txt_rect, (self.rect.left+5, self.rect.top+15))
        # вывод на экран инпут бокса
        pygame.draw.rect(self.screen, self.color, self.rect, 2)  # последний аргумент ширина border!


class Button(Sprite):
    """Класс кнопки, 
    наверно как-то более красиво можно сделать."""
    def __init__(self, screen, msg,  x=590, y=430,
                 width=50, height=50,):
        super(Button, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.COLOR_BUTTON = (235, 215, 115)  # основной цвет кнопки
        self.HOVER_BUTTON = (50, 0, 105)  # цвет:hover кнопки
        self.text_color = (255, 255, 255)  # основной цвет текста
        self.font = pygame.font.SysFont(None, 32)  # Размер и шрифт
        # флаг для переключения состояния кнопки
        self.pos_button_hover = False
        # Построение объекта rect кнопки и выравнивание где нам нада.
        self.rect = pygame.Rect(x, y, width, height)
        # Сообщение кнопки создается только один раз.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Преобразует msg в прямоугольник и выравнивает текст по центру.
        просто прямоуголник с цветом и текстом-картинкой"""
        self.msg = msg  # нужна для определения, хранит стринг
        # рендерим текст
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.COLOR_BUTTON)
        # создаем прямоугольник текста и его центр становиться центром кнопки
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def update(self):
        # Перерисовываем кнопки
        pygame.draw.rect(self.screen, self.HOVER_BUTTON, self.rect, 1)  # последний аргумент ширина border!
        self.screen.fill(self.HOVER_BUTTON, self.rect, 1)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def draw_button(self):
        # Отображение пустой кнопки и вывод сообщения поверх неё.
        self.screen.fill(self.COLOR_BUTTON, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
