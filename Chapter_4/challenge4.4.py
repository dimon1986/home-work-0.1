import random


def load_word():
    # забираем хорошую функцию из предыдущей игры:)
    # загрузим последовательность слов делаем выбор
    with open('WORDS.txt', 'r', encoding='utf-8') as f:
        WORDS = f.read().split()
        # случайным образом выберем из последовательности одно слово
        word = random.choice(WORDS)
        return word
# создадим переменную с которой будет затем сопоставлена версия игрока
enigma_word = load_word()


def hello(word):
    # просто приветствие и больше ничего
    print(f'Загадоно слово содержащие {len(word)} букв, попробуй отгадать его.'
          f'(\nДля выхода нажмите Enter, не вводя своей версии.)')
# просто вызов
hello(enigma_word)

star = '*' * len(enigma_word)  # по одной звёздочке на каждую букву, кторую надо отгадать
# мой ответ
attempt = None


def check_attempt(answer):
    # просто проверка ответа и соответственное ветвление
    if answer == '':
        # первым что бы выйти
        print('Не хотите играть - как хотите.')
    # проверка на вхождение объявляем стар глобал, что бы сохнанить новый вид
    elif answer in enigma_word:
        global star
        new = ''
        for i in range(len(enigma_word)):
            if attempt == enigma_word[i]:
                new += attempt
            else:
                new += star[i]
        star = new
        print('Входит в состав слова.')
        print('\nЗагаданное слово сейчас выглядит так:\n', star)
    # если не входить в состав слова
    else:
        print('К сожалению, вы не правы.')
        print('Не входит в состав слова.')
        print('\nЗагаданное слово сейчас выглядит так:\n', star)


while attempt != enigma_word and star != enigma_word and attempt != '':
    # бесконечный цыкл вопросов пока не случится что-то от сех^
    attempt = input('Какое это слово? или можешь угадать букву?\n')
    if attempt != enigma_word:
        check_attempt(attempt.lower())


def bye():
    if attempt == enigma_word:
        print(f'\nМои поздравления - это действительно {enigma_word.upper()}\n')
        print('\t\tСпасибо за игру!'.upper())
# просто говорим досвиданье и поздравления если отгодали
bye()

input('\n\nНажмите Enter, что бы выйти...')