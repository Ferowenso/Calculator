# импорт всего шо надо
import math, time, re, shelve, sys, random, os.path
try:
    import requests
except ModuleNotFoundError:
    print("У вас не установлен requests!")
    sys.exit()
try:
    from shoppy import shopping
except ModuleNotFoundError:
    print("У вас нет магазина! Скачать его вы можете здесь https://github.com/Ferowenso/Calculator")
    sys.exit()
items = []
class Main():
    def __init__(self, name=None, age=None, xp=0, money=0, lvl=0):
        self.name = name
        self.age = age
        self.xp = xp
        self.money = money
        self.lvl = lvl

    def __str__(self):
        return "Имя: {}, возраст: {}".format(calc.name, calc.age)

    def login(self):
        print("Каково же твое имя?")
        while 1:
            self.name = input('')
            if not self.name:
                print("Зачем мне пустой ответ?")
                continue
            elif len(self.name) > 30:
                print("Что-то слишком длинное имя....")
                continue
            elif re.findall(r'\d', self.name) == []:
                break
            else:
                print("Я спросил имя!")
        time.sleep(1)
        print("А сколько же тебе лет?")
        while 1:
            try:
                self.age = int(input(""))
                if self.age > 100:
                    print("Что-то слишком много..")
                    continue
                elif self.age < 1:
                    print("Что-то слишком мало")
                    continue
                break
            except ValueError:
                print("Мне нужны числа!")
                continue

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

    def date(self):
        print("Тут ты можешь узнать дату какого-либо события")
        event = input("Событие: ")
        day = random.randint(1, 31)
        moth = random.randint(1, 12)
        year = random.randint(2019, 2025)
        print("Дата {}: {}.{}.{}".format(event, day, moth, year))
        self.xp = self.xp + random.randint(1, 10)

    def chance():
        print("Тут ты можешь узнать вероятность какого-либо события")
        event = input("Событие: ")
        chance = random.randint(0, 100)
        print("Вероятность {}: {}%".format(event, chance))
        self.xp = self.xp + random.randint(1, 10)

    def valute(self):
        api = "https://www.cbr-xml-daily.ru/daily_json.js"
        print("Это курс валют!")
        r = requests.get(api)
        encode = r.json()
        usd = encode["Valute"]["USD"]["Value"]
        eur = encode["Valute"]["EUR"]["Value"]
        print("""Доллар: {} рубля
 Евро: {} рубля""".format(usd, eur))
        self.xp = self.xp + random.randint(1, 10)

    def weather(self):
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
                self.xp = self.xp + random.randint(1, 10)
            elif ent.lower() == "Выход".lower():
                break
            else:
                print("шо?")

    def calc():
    global xp
    print("Ты запустил калькулятор")
    while True:
        try:
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
                print("Вот твой результат, " + calc.name + ":{}".format(x + y))
                self.xp = self.xp + random.randint(1, 10)
            elif encalc.lower() == "Вычитание".lower():
                print("Вот твой результат, " + calc.name + ":{}".format(x - y))
                self.xp = self.xp + random.randint(1, 10)
            elif encalc.lower() == "Умножение".lower():
                print("Вот твой результат, " + calc.name + ":{}".format(x * y))
                self.xp = self.xp + random.randint(1, 10)
            elif encalc.lower() == "Степень".lower():
                print("Вот твой результат, " + calc.name + ":{}".format(x ** y))
                self.xp = self.xp + random.randint(1, 10)
            elif encalc.lower() == "Деление".lower():
                if x or y == 0:
                    print("Оставь вселенную в покое")
                else:
                    print("Вот твой результат, " + calc.name + ": {}".format(x / y))
                    self.xp = self.xp + random.randint(1, 10)
            elif encalc.lower() == "Корень".lower():
                print("Вот твой результат, " + calc.name + ": {} и {}".format(math.sqrt(x), math.sqrt(y)))
                self.xp = self.xp + random.randint(1, 10)
            elif encalc.lower() == "Синус".lower():
                print("Вот твой результат, " + calc.name + ":{} и {}".format(math.sin(x), math.sin(y)))
                self.xp = self.xp + random.randint(1, 10)
            elif encalc.lower() == "Косинус".lower():
                print("Вот твой результат, " + calc.name + ":{} и {}".format(math.cos(x), math.cos(y)))
                self.xp = self.xp + random.randint(1, 10)
            elif encalc.lower() == "Выход".lower():
                print("Выходим")
                time.sleep(1)
                break
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
<<<<<<< HEAD
memory = os.path.isfile("log")
if memory:
    with shelve.open("log") as stat:
        money = stat["денюжки"]
        money = money
        shop = stat["магаз"]
        items = shop
        level = stat["уровень"]
        calc = stat["ты"]
=======
if platform == "win32":
    memory = os.path.isfile("log.dat")
else:
    memory = os.path.isfile("log")
if memory:
    with shelve.open("log") as stat:
        calc = stat["калк"]
>>>>>>> b8f08a7708a2309df25062dab8462607ed035d79
        print("Здравствуй, {}".format(calc.name))
if memory == False:
    calc = Main()
    calc.login()
    calc = Main(name=calc.name, age=calc.age)
<<<<<<< HEAD
    money = money
    shop = items[:]
=======
    with shelve.open("log") as stat:
        stat["калк"] = calc
def mem():
    global g
    global money
    global shop
    global xp
    global level
>>>>>>> b8f08a7708a2309df25062dab8462607ed035d79
    with shelve.open("log") as stat:
        state["ты"] = calc
        stat["денюжки"] = money
        stat["магаз"] = shop
        stat["уровень"] = level
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
        enter = input(calc.name + "," " введи что тебе нужно: ")
        if enter.lower() == "Калькулятор".lower():
            calc()
        elif enter.lower() == "Шансы".lower():
            chance()
        elif enter.lower() == "дата":
            calc.date()
        elif enter.lower() == "Число".lower():
            randomn()
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
        elif enter.lower() == "погода":
            calc. weather()
        elif enter.lower() == "Курс".lower():
            valute()
        elif enter.lower() == "Удача".lower():
            luck()
        else:
            print("Не понимаю!")
#выход через ctrl+c
except KeyboardInterrupt:
    print("Выходим");time.sleep(1);sys.exit
