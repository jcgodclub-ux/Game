import random
import time

def gen_task(level):
    """
    Функция создаём математический пример
    level - уровень сложности
    возвращает текст примера и правильный ответ
    """
    if level == 1:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        op = random.choice(["+", "-"])

        if op == '+':
            answer = a + b
        else:
            answer = a - b
        return f"{a} {op} {b}", answer

    if level == 2:
        op = random.choice(["+", "-", "*"])
        if op == "*":
            a = random.randint(2, 9)
            b = random.randint(2, 9)
            answer = a * b
        if op == '+':
            a = random.randint(1, 30)
            b = random.randint(1, 30)
            answer = a + b
        if op == '-':
            a = random.randint(1, 30)
            b = random.randint(1, 30)
            answer = a - b
        return f"{a} {op} {b}", answer

def ask_int(text):
    """
    Функция для безопасного ввода числа
    Не позволяет ввести текст вместо числа
    """
    while True:
        value = input(text)
        try:
            return int(value)
        except:
            print("Введите число!")

def run_quiz():
    print("Математический квиз")
    print("Отвечайте на вопросы и набирайте очки")
    print()
    # Выбор уровня сложности
    level = ask_int("Выберите уровень сложности (1-3): ")
    if level < 1 or level > 3:
        level = 1

    # Количество вопросов
    rounds = ask_int("Сколько вопросов будет в игре: ")
    if rounds <= 0:
        rounds = 10

    # Время на ответ
    time_limit = ask_int("Сколько секунд на ответ: ")
    if time_limit <= 0:
        time_limit = 7

    lives = 3 # количество жизней
    score = 0 # очки игрока

    print('\nИгра начинается!\n')

    # Основной игровой цикл
    for i in range(1, rounds+1):

        # генерируем пример
        task, right_answer = gen_task(level)

        print(f'Вопрос {i}/{rounds}')
        print(f"Очки: {score} Жизни: {lives}")
        print(f"Пример:", task)

        # Засекаем время
        start_time = time.time()
        user_input = input('Ваш ответ: ')
        spent_time = time.time() - start_time

        # Проверка время
        if spent_time > time_limit:
            lives -= 1
            print("Время вышло!")
            print("Правильный ответ:", right_answer)
            print()
        else:
            try:
                user_answer = int(user_input)
                if user_answer == right_answer:
                    score += 1
                    print('Верно')
                else:
                    lives -= 1
                    print("Неверно!")
                    print("Правильный ответ:", right_answer)
                print()
            except Exception as e:
                print(e)