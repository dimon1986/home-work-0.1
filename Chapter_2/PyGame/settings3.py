import pygame
from pygame.sprite import Sprite
import os


class Settings(object):
    """Обычный калсс для хранения размеров экрана"""
    def __init__(self):
        self.screen_width = 640
        self.screen_height = 490
        self.bg_color = (110, 90, 125)


class InputBox(Sprite):
    """Класс для ввода цены на машину"""
    def __init__(self, screen, txt='', the='',
                 x=10, y=10, width=300, height=50):
        super(InputBox, self).__init__()
        self.screen = screen
        self.rect_scr = screen.get_rect()
        self.COLOR_INACTIVE = (245, 115, 130)
        self.COLOR_ACTIVE =(250, 250, 250)
        self.color = self.COLOR_INACTIVE
        self.active = False
        self.backspace = False
        self.the = the
        self.font = pygame.font.SysFont('arial', 28)
        self.txt = txt
        self.txt_rect = self.font.render(txt, True, (250, 250, 250))
        self.rect = pygame.Rect(x, y, width, height)

    def update(self):
        self.screen.blit(self.txt_rect, (self.rect.left + 5, self.rect.top + 10))
        pygame.draw.rect(self.screen, self.color, self.rect, 2)

    def draw(self):
        if len(self.txt) > 10:
            self.txt = self.txt[:-1]
            self.update()
        self.update()


class Label(Sprite):
    """Просто надпись"""
    def __init__(self, screen, txt='', the='',
                 x=10, y=120, width=620, height=50):
        super(Label, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.color = (245, 115, 130)
        self.the = the
        # дефаут - это начальное название лейбла
        self.default = txt
        self.font = pygame.font.SysFont('arial', 24)
        # а txt будет разный, отображается на экране
        self.txt = txt
        self.txt_rect = self.font.render(txt, True, (250, 250, 250))
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        self.screen.fill((190, 110, 130), self.rect)
        self.screen.blit(self.txt_rect, (self.rect.left + 5, self.rect.top + 10))
        pygame.draw.rect(self.screen, self.color, self.rect, 2)


class Image(Sprite):
    """Класс для картинки, 
    и словарь с сылками на изображения"""
    def __init__(self, screen):
        super(Image, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        # блин почему раньше не сказали про такой путь очень удобно!
        self.dict_image={'car': os.path.abspath('data//car.png'),
                         'car_a': os.path.abspath('data//car_a.png'),
                         'car_b': os.path.abspath('data//car_b.png'),
                         'car_c': os.path.abspath('data//car_c.png')}
        # загрузка изображениий мороженного
        self.image = pygame.image.load(f"{self.dict_image['car']}")
        # получаем примоугольник картинки
        self.rect = self.image.get_rect()
        # задаём значения где должен быть центор его
        # и где его низ будет всё относительно экрана
        self.rect.right = self.screen_rect.right-30
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """рисует картинку в тикущей позиции"""
        self.screen.blit(self.image, self.rect)


class Button(Sprite):
    """Класс кнопки, 
    наверно как-то более красиво можно сделать."""
    def __init__(self, screen, txt,
                 x=380, y=40, width=230, height=50,):
        super(Button, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.COLOR_BUTTON = (250, 180, 150)  # основной цвет кнопки
        self.HOVER_BUTTON = (50, 95, 125)  # цвет:hover кнопки
        self.txt_color = (255, 255, 255)  # основной цвет текста
        self.font = pygame.font.SysFont('arial', 28)  # Размер и шрифт
        # флаг для переключения состояния кнопки
        self.hover = False
        # Построение объекта rect кнопки и выравнивание где нам нада.
        self.rect = pygame.Rect(x, y, width, height)
        # Сообщение кнопки создается только один раз.
        self.prep_msg(txt)

    def prep_msg(self, txt):
        """Преобразует msg в прямоугольник и выравнивает текст по центру.
        просто прямоуголник с цветом и текстом-картинкой"""
        self.txt = txt  # нужна для определения, хранит стринг
        # рендерим текст
        self.txt_image = self.font.render(txt, True, self.txt_color)
        # создаем прямоугольник текста и его центр становиться центром кнопки
        self.txt_rect = self.txt_image.get_rect()
        self.txt_rect.center = self.rect.center

    def update(self):
        # меняем цвет кавадрата вокруг кнопки
        self.screen.fill(self.HOVER_BUTTON, self.rect)
        self.screen.blit(self.txt_image, self.txt_rect)
        pygame.draw.rect(self.screen, (245, 115, 130), self.rect, 2)  # последний аргумент ширина border!

    def draw_button(self):
        # Отображение пустой кнопки и вывод сообщения поверх неё.
        self.screen.fill(self.COLOR_BUTTON, self.rect)
        self.screen.blit(self.txt_image, self.txt_rect)
        pygame.draw.rect(self.screen, (245, 115, 130), self.rect, 2)