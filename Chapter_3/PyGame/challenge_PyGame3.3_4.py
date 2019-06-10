from pygame.sprite import Group
from M_Dawson_Home_Work.Chapter_3.PyGame.settings3_4 import *
import M_Dawson_Home_Work.Chapter_3.PyGame.functions3_4 as f
# можно добавить анимацию, но нужно уметь рисовать
images = ((0, 'data//death.png'),)
images1 = ((0, 'data//droid.png'),)


def run_main():
    pygame.init()  # инициируем пайгейм
    clock = pygame.time.Clock()  # создаём для нужно чистаты кадров
    stg = Settings()  # обект для актуальных состояний игры, значений
    pygame.display.set_caption('Смерть & Дроид')
    screen = pygame.display.set_mode((stg.screen_width, stg.screen_height))
    # разделил на две группы, хочешь одну отображаешь, хочешь вторую
    death_gui = Group()
    droid_gui = Group()
    # надписи сверху, может быть лишние
    label = Label(screen, txt_color='white', txt='Смерть', x=270)
    label0 = Label(screen, txt_color='white', txt='Дроид', x=270)
    # периключаем игры
    button = Button(screen, txt='Смерть',)
    button0 = Button(screen, txt='Дроид', y=350,)
    # ввод и отплавка ссобщения
    input_box = InputBox(screen, x=420, y=300, width=150, )
    button1 = Button(screen, txt='Сказать', x=420, y=350, width=150,)
    # лейблы для взаимодействия с "загадочником"
    label1 = Label(screen,  hover_txt_color='orange_light', txt='Больше', x=70, y=70)
    label2 = Label(screen, txt_color='black', hover_txt_color='orange_light', txt='Меньше', x=70, y=120)
    label3 = Label(screen,  hover_txt_color='orange_light', txt='Верно', x=70, y=170)
    # отображается всюду для начала любой игры
    label4 = Label(screen,  hover_txt_color='orange_light', txt='Старт', x=70, y=220)
    # лейблы строк, где будут появляться слова
    label5 = Label(screen, link='speech',  x=370, y=70)
    label6 = Label(screen, link='speech1', x=370, y=120)
    label7 = Label(screen, link='speech2', x=370, y=170)
    label8 = Label(screen, link='speech3', x=370, y=220)
    # картинки и сам фон для неё
    image = Image(screen, x=70, width=500, images=images)
    image1 = Image(screen, x=70, width=500, images=images1)
    # в данном исполнеение, по слоям отрисовывается
    # так что первое раньше отрисовывается
    death_gui.add(button, button0, button1, label, input_box, image, label4,
                  label5, label6, label7, label8,)
    # отрисовывается если активен дроид
    droid_gui.add(button, button0, label0, image1, label1, label2, label3, label4,
                  label5, label6, label7, label8,)

    while True:
        # не уверен что данная проверка не замедляет цыкл
        if stg.death_active:
            gui = death_gui
        else:
            gui = droid_gui
        # проверка событий
        f.check_event(stg, gui, input_box,)
        # обновление экрана
        f.update_screen(stg, screen, gui,)
        # данная функция более точна, хотя чуть больше использует процессор
        clock.tick_busy_loop(20)

if __name__ == '__main__':
    run_main()
