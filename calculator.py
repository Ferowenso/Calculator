
# импорт всего шо надо
import math
import time
import re
import shelve
import os.path
import sys
import random
try:
    import requests
except:
    print("У вас не установлен requests!")
    sys.exit()
try:
    from shoppy import shopping
except:
    print("У вас нет магазина! Скачать его вы можете здесь https://github.com/Ferowenso/Calculator")
    sys.exit()
items = []
class Main():
    def __init__(self, name=None, age=None, xp=0):
        self.name = name
        self.age = age
        self.xp = xp

    def randomn(self):
        while True:
            try:
                print("Рандомное число из заданного диапазона")
                x = int(input("Первое число: "))
                y = int(input("Второе число: "))
                global rand
                rand = random.randint(x, y)
                print("Число: {}".format(rand))
                self.xp = self.xp + random.randint(1, 10)
                break
            except ValueError:
                print("Число!")
                continue

def login():
    print("Каково же твое имя?")
    while 1:
        global name
        name = input('')
        if not name:
            print("Зачем мне пустой ответ?")
            continue
        elif len(name) > 30:
            print("Что-то слишком длинное имя....")
            continue
        elif re.findall(r'\d', name) == []:
            break
        else:
            print("Я спросил имя!")
    time.sleep(1)
    print("А сколько же тебе лет?")
    while 1:
        try:
            global age
            age = int(input(""))
            if age > 100:
                print("Что-то слишком много..")
                continue
            elif age < 1:
                print("Что-то слишком мало")
                continue
            break
        except ValueError:
            print("Мне нужны числа!")
            continue
#рандомное число
def randomn():
    global xp
    while True:
        try:
            print("Рандомное число из заданного диапазона")
            x = int(input("Первое число: "))
            y = int(input("Второе число: "))
            global rand
            rand = random.randint(x, y)
            print("Число: {}".format(rand))
            xp = xp + random.randint(1, 10)
            break
        except ValueError:
            print("Число!")
            continue
#дата чего-либо
def date():
    global xp
    print("Тут ты можешь узнать дату какого-либо события")
    event = input("Событие: ")
    day = random.randint(1, 31)
    moth = random.randint(1, 12)
    year = random.randint(2019, 2025)
    print("Дата {}: {}.{}.{}".format(event, day, moth, year))
    xp = xp + random.randint(1, 10)
    with shelve.open("log") as stat:
        stat["опыт"] = xp
#шансы чего-либо
def chance():
    global xp
    print("Тут ты можешь узнать вероятность какого-либо события")
    event = input("Событие: ")
    chance = random.randint(0, 100)
    print("Вероятность {}: {}%".format(event, chance))
    xp = xp + random.randint(1, 10)
    with shelve.open("log") as stat:
        stat["опыт"] = xp
#удаление данных
def delete():
    global yesorno
    print("Ты точно хочешь удалить данные?")
    while True:
        yesorno = input("Да или Нет: ")
        if yesorno.lower() == "Да".lower():
            os.remove("log")
            print("Удаление...")
            time.sleep(1)
            exit(0)
        elif yesorno.lower() == "Нет".lower():
            print("Ну и зачем ты тогда сюда заходил?")
            break
        else:
            print("Да/Нет")
            continue
def luck():
    global money
    while True:
        with shelve.open ("log") as stat:
            try:
                money = stat["денюжки"]
            except KeyError:
                stat["денюжки"] = money
        print("""Это игра на удачу
1 игра - 100 монет
Если 2 числа совпадут - +500 монет
Если 3 числа совпадут - +1000 монет
Вы хотите продолжить? Да/Нет""")
        entcas = input("")
        if entcas.lower() == "Да".lower():
            if money >= 100:
                money = money -100
                with shelve.open ("log") as stat:
                    stat["магаз"] = items
                    stat["денюжки"] = money
                first = random.randint(1, 9)
                second = random.randint(1,9)
                third = random.randint(1,9)
                print("Числа: {}, {}, {}".format(first, second, third))
                if first == second or first == third or second == third:
                    money = money + 500
                    print("Два числа совпали! +500 монет")
                    print("Ваш баланс {}".format(money))
                    with shelve.open ("log") as stat:
                          stat["денюжки"] = money
                elif first == second == third:
                    money = money + 1000
                    print("Три числа совпали! +1000 монет")
                    with shelve.open ("log") as stat:
                        stat["денюжки"] = money
                else:
                    print("Вы проиграли D:")
            else:
                print("Недостаточно денег!")
        elif entcas.lower() == "Нет".lower():
            break
        else:
            print("шо?")
#работа
money = 0
def jobmain():
    global money
    while True:
        with shelve.open ("log") as stat:
            try:
                money = stat["денюжки"]
            except KeyError:
                stat["денюжки"] = money
        print("""Напишите \"Работать\", чтобы работать
\"Выход\", чтобы выйти""")
        jobtest = input()
        if jobtest.lower() == "работать".lower():
            if level == 0:
                money = money + random.randint(1, 5)
                print("Ваш баланс {}".format(money))
                with shelve.open ("log") as stat:
                    stat["денюжки"] = money
            elif level == 1:
                    money = money + random.randint(5, 30)
                    print("Ваш баланс {}".format(money))
                    with shelve.open ("log") as stat:
                        stat["денюжки"] = money
            elif level == 2:
                money = money + random.randint(25, 55)
                print("Ваш баланс {}".format(money))
                with shelve.open ("log") as stat:
                    stat["денюжки"] = money
            elif level == 3:
                money = money + random.randint(50, 90)
                print("Ваш баланс {}".format(money))
                with shelve.open ("log") as stat:
                    stat["денюжки"] = money
        elif jobtest.lower() == "выход".lower():
            break
        else:
            print("шо?")
#курс валют
def valute():
    global xp
    api = "https://www.cbr-xml-daily.ru/daily_json.js"
    print("Это курс валют!")
    r = requests.get(api)
    encode = r.json()
    usd = encode["Valute"]["USD"]["Value"]
    eur = encode["Valute"]["EUR"]["Value"]
    print("""Доллар: {} рубля
 Евро: {} рубля""".format(usd, eur))
    xp = xp + random.randint(1, 10)
    with shelve.open("log") as stat:
        stat["опыт"] = xp
#прогноз погоды
def weather():
    global xp
    while True:
        print("Введите \'Продолжить\' или \'Выход\'")
        ent = input("")
        if ent.lower() == "Продолжить".lower():
            apiurl = "http://api.openweathermap.org/data/2.5/find"
            print("Введите название города на английском")
            q = input("")
            q = q.lower()
            appid = '22c7bf8e593c47b0cf88f390e8e5376a'
            params = {
                    'q': q,
                    'appid': appid,
                    'units': 'metric',
                    'lang': 'ru'
            }
            r = requests.get(apiurl, params=params)
            encode = r.json()
            try:
                w = encode['list'][0]['weather'][0]['description']
                temp = encode["list"][0]["main"]["temp"]
                vlaga = encode["list"][0]["main"]["humidity"]
                wind = encode["list"][0]["wind"]["speed"]
            except:
                print("что ты черт побери такое несешь? нет такого города")
                continue
            print("""Город: {}
            Погода: {}
            Температура: {}°
            Влажность: {}
            Скорость ветра: {}м/с""".format(q, w, temp, vlaga, wind))
            xp = xp + random.randint(1, 10)
            with shelve.open("log") as stat:
                stat["опыт"] = xp
        elif ent.lower() == "Выход".lower():
            break
        else:
            print("шо?")
#профиль
def profile():
    print("""Ваше имя: {}
Ваш возраст: {}
Ваш баланс: {}$
Ваши предметы: {}
Ваш опыт: {}xp
Ваш уровень: {} """.format(name, age, money, items, xp, level))
level = 0
#уровни
def levelup():
    global xp
    global level
    while True:
        with shelve.open("log") as stat:
            try:
                xp = stat["опыт"]
                level = stat["уровень"]
            except KeyError:
                stat["опыт"] = xp
                stat["уровень"] = level
        print("""Тут ты можешь повысить свой уровень!
1 Уровень - 75xp
2 Уровень - 150xp
3 Уровень - 300xp
для повышения напишите цифру
для выхода напишите \"Выход\"""")
        lvbuy = input("")
        if lvbuy == "1":
            if level >= 1:
                print("Ты не можешь этого сделать!")
                continue
            else:
                if xp >= 75:
                    print("Вы апнули уровень до 1!")
                    level = 1
                    with shelve.open ("log") as stat:
                        stat["уровень"] = level
                else:
                    print("Недостаточно xp!")
        elif lvbuy == "2":
            if level >= 2:
                print("Ты не можешь этого сделать!")
                continue
            else:
                if xp >= 150:
                    print("Вы апнули уровень до 2!")
                    level = 2
                    with shelve.open ("log") as stat:
                        stat["уровень"] = level
                else:
                    print("Недостаточно xp!")
        elif lvbuy == "3":
            if level >= 3:
                print("Ты не можешь этого сделать!")
                continue
            else:
                if xp >= 300:
                    print("Вы апнули уровень до 3!")
                    level = 3
                    with shelve.open ("log") as stat:
                        stat["уровень"] = level
                else:
                    print("Недостаточно xp!")
        elif lvbuy.lower() == "Выход".lower():
            break
        else:
            print("шо?")
# калькулятор
def calc():
    global xp
    print("Ты запустил калькулятор")
    while True:
        with shelve.open("log") as stat:
            try:
                xp = stat["опыт"]
                x = float(input("Первое значение: "))
                y = float(input("Второе значение: "))
            except KeyError:
                stat["опыт"] = xp
            except ValueError:
                print("Цифорками!")
                continue
            else:
                encalc = input("""Введи что тебе нужно:
• Сложение
• Вычитание
• Умножение
• Деление
• Степень
• Корень
• Синус
• Косинус
• Выход
""")
                if encalc.lower() == "Сложение".lower():
                    print("Вот твой результат, " + name + ":{}".format(x + y))
                    xp = xp + random.randint(1, 10)
                    with shelve.open("log") as stat:
                        stat["опыт"] = xp
                elif encalc.lower() == "Вычитание".lower():
                    print("Вот твой результат, " + name + ":{}".format(x - y))
                    xp = xp + random.randint(1, 10)
                    with shelve.open("log") as stat:
                        stat["опыт"] = xp
                elif encalc.lower() == "Умножение".lower():
                    print("Вот твой результат, " + name + ":{}".format(x * y))
                    xp = xp + random.randint(1, 10)
                    with shelve.open("log") as stat:
                        stat["опыт"] = xp
                elif encalc.lower() == "Степень".lower():
                    print("Вот твой результат, " + name + ":{}".format(x ** y))
                    xp = xp + random.randint(1, 10)
                    with shelve.open("log") as stat:
                        stat["опыт"] = xp
                elif encalc.lower() == "Деление".lower():
                    if x or y == 0:
                        print("Оставь вселенную в покое")
                    else:
                        print("Вот твой результат, " + name + ": {}".format(x / y))
                        xp = xp + random.randint(1, 10)
                    with shelve.open("log") as stat:
                        stat["опыт"] = xp
                elif encalc.lower() == "Корень".lower():
                    print("Вот твой результат, " + name + ": {} и {}".format(math.sqrt(x), math.sqrt(y)))
                    xp = xp + random.randint(1, 10)
                    with shelve.open("log") as stat:
                        stat["опыт"] = xp
                elif encalc.lower() == "Синус".lower():
                    print("Вот твой результат, " + name + ":{} и {}".format(math.sin(x), math.sin(y)))
                    xp = xp + random.randint(1, 10)
                    with shelve.open("log") as stat:
                        stat["опыт"] = xp
                elif encalc.lower() == "Косинус".lower():
                    print("Вот твой результат, " + name + ":{} и {}".format(math.cos(x), math.cos(y)))
                    xp = xp + random.randint(1, 10)
                    with shelve.open("log") as stat:
                        stat["опыт"] = xp
                elif encalc.lower() == "Выход".lower():
                    print("Выходим")
                    time.sleep(1)
                    break
#фихня нужная для запоминания имени
def memory():
    memory = os.path.isfile("log")
    if memory:
        with shelve.open("log") as stat:
            global name
            global age
            global g
            global money
            global shop
            global items
            global xp
            global level
            g = stat["г"]
            name = g[0]
            age = g[1]
            money = stat["денюжки"]
            money = money
            shop = stat["магаз"]
            items = shop
            xp = stat["опыт"]
            level = stat["уровень"]
            level = level
            print("Здравствуй, {}".format(name))
            print(xp)
    if memory == False:
        xp = 0
        login()
        g = name, age
        money = money
        shop = items[:]
        level = level
        with shelve.open("log") as stat:
            stat["г"] = g
            stat["денюжки"] = money
            stat["магаз"] = shop
            stat["опыт"] = xp
            stat["уровень"] = level
def mem():
    global g
    global money
    global shop
    global xp
    global level
    with shelve.open("log") as stat:
        stat["г"] = g
        g = stat["г"]
        stat["денюжки"] = money
        money = stat["денюжки"]
        stat["магаз"] = shop
        shop = stat["магаз"]
        stat["опыт"] = xp
        xp = stat["опыт"]
        stat["уровень"] = level
        level = stat["уровень"]
memory()
mem()
#начало хы
try:
    print("Ладно, начнем-с")
    time.sleep(1)
    while True:
        print("""Функции этой прекрасной программы:
            1) Калькулятор
            2) Шансы
            3) Дата
            4) Число
            5) Удалить данные
            6) Работа
            7) Профиль
            8) Магазин
            9) Уровень
            10) Погода
            11) Курс""")
        enter = input(name + "," " введи что тебе нужно: ")
        if enter.lower() == "Калькулятор".lower():
            calc()
            memory()
        elif enter.lower() == "Шансы".lower():
            chance()
            memory()
        elif enter.lower() == "Дата".lower():
            date()
            memory()
        elif enter.lower() == "Число".lower():
            randomn()
            memory()
        elif enter.lower() == "Удалить данные".lower():
            delete()
        elif enter.lower() == "Работа".lower():
            jobmain()
        elif enter.lower() == "Профиль".lower():
            profile()
        elif enter.lower() == "Магазин".lower():
            shopping()
            memory()
        elif enter.lower() == "Уровень".lower():
            levelup()
            memory()
        elif enter.lower() == "Погода".lower():
            weather()
            memory()
        elif enter.lower() == "Курс".lower():
            valute()
            memory()
        elif enter.lower() == "Удача".lower():
            luck()
            memory()
        else:
            print("Не понимаю!")
#выход через ctrl+c
except KeyboardInterrupt:
    with shelve.open("log") as stat:
        stat["опыт"] = xp
    print("Выходим");time.sleep(1);sys.exit
