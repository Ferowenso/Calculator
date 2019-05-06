
# импорт всего шо надо
import math, time, re, shelve, sys, random, os.path, json
from sys import platform
try:
    import requests
except ModuleNotFoundError:
    print("У вас не установлен requests!")
    sys.exit()
#items = []
class Main():
    def __init__(self, name=None, age=None, xp=0, money=0, lvl=0, items=[]):
        self.name = name
        self.age = age
        self.xp = xp
        self.money = money
        self.lvl = lvl
        self.items = items

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
                self.xp += random.randint(1, 10)
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

    def chance(self):
        print("Тут ты можешь узнать вероятность какого-либо события")
        event = input("Событие: ")
        test = randomorgmain(0, 100)
        print("Шанс {} {}%" .format(event, test))
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
                try:
                    r = requests.get(apiurl, params=params, timeout=5)
                    encode = r.json()
                except:
                    print("Чота у вас с инетом или еще какие-то проблемы, мы тут ничо сделать не можем")
                    sys.exit()
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
#тест
#ыыыыы
    def calcc(self):
        print("Ты запустил калькулятор")
        while True:
            try:
                x = float(input("Первое значение: "))
                y = float(input("Второе значение: "))
            except ValueError:
                    print("Цифорками!")
                    continue
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
            if encalc.lower() == "сложение":
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

    def profile(self):
        with shelve.open ("log") as stat:
            try:
                self.money = stat["денюжки"]
            except KeyError:
                stat["денюжки"] = self.money
        print("""Ваше имя: {}
Ваш возраст:{}
Ваш баланс:{}$
Ваши предметы: {}
Ваш опыт: xp {}
Ваш уровень:{}  """.format(self.name, self.age, self.money, self.items, self.xp, self.lvl))
    def jobmain(self):
        while True:
            with shelve.open ("log") as stat:
                try:
                    self.money = stat["денюжки"]
                except KeyError:
                    stat["денюжки"] = self.money
            print("""Напишите \"Работать\", чтобы работать
\"Выход\", чтобы выйти""")
            jobtest = input()
            if jobtest.lower() == "работать".lower():
                if self.lvl == 0:
                    self.money = self.money + random.randint(1, 5)
                    print("Ваш баланс {}".format(self.money))
                    with shelve.open ("log") as stat:
                        stat["денюжки"] = self.money
                elif self.lvl == 1:
                        self.money = self.money + random.randint(5, 30)
                        print("Ваш баланс {}".format(self.money))
                        with shelve.open ("log") as stat:
                            stat["денюжки"] = self.money
                elif self.lvl == 2:
                    self.money = self.money + random.randint(25, 55)
                    print("Ваш баланс {}".format(self.money))
                    with shelve.open ("log") as stat:
                        stat["денюжки"] = self.money
                elif self.lvl == 3:
                    self.money = self.money + random.randint(50, 90)
                    print("Ваш баланс {}".format(self.money))
                    with shelve.open ("log") as stat:
                        stat["денюжки"] = self.money
            elif jobtest.lower() == "выход".lower():
                break
            else:
                print("шо?")
    def levelup(self):
        while True:
            print("""Тут ты можешь повысить свой уровень!
1 Уровень - 75xp
2 Уровень - 150xp
3 Уровень - 300xp
для повышения напишите цифру
для выхода напишите \"Выход\"""")
            lvbuy = input("")
            if lvbuy == "1":
                if self.lvl >= 1:
                    print("Ты не можешь этого сделать!")
                    continue
                else:
                    if calc.xp >= 75:
                        print("Вы апнули уровень до 1!")
                        self.lvl = 1
                    else:
                        print("Недостаточно xp!")
            elif lvbuy == "2":
                if self.lvl >= 2:
                    print("Ты не можешь этого сделать!")
                    continue
                else:
                    if calc.xp >= 150:
                        print("Вы апнули уровень до 2!")
                        self.lvl = 2
                    else:
                        print("Недостаточно xp!")
            elif lvbuy == "3":
                if self.lvl >= 3:
                    print("Ты не можешь этого сделать!")
                    continue
                else:
                    if calc.xp >= 300:
                        print("Вы апнули уровень до 3!")
                        self.lvl = 3
                    else:
                        print("Недостаточно xp!")
            elif lvbuy.lower() == "Выход".lower():
                break
            else:
                print("шо?")

    def shopping(self):
        while True:
            print("""Для покупки напишите цифру:
1) Шапка-ушанка - 10$
2) Мерч Хесуса - 50$
3) Электрогитара - 75$
4) АААААААААААвтомобиль - 150$
5) Ракета SpaceX - 500$
6) Кошкодевочка от Tesla - 1500$
7) Вейп Братишкина - 2250$
8) Футболка \"КиШ\" - 300$
9) ПК от ZyperPC - 1000$
Напишите \"Выход\", чтобы выйти""")
            buy = input("")
            if buy == "1":
                if "Шапка-ушанка" in self.items:
                    print("У тебя есть этот предмет!")
                    continue
                else:
                    if self.money >= 10:
                        print("Вы купили Шапку-ушанку!")
                        self.items.append("Шапка-ушанка")
                        self.money - 10
                    else:
                        print("Недостаточно денег!")
            elif buy == "2":
                if "Мерч Хесуса" in calc.items:
                    print("У тебя есть этот предмет!")
                    continue
                else:
                    if calc.money >= 50:
                        print("Вы купили Мерч Хесуса!")
                        calc.items.append("Мерч Хесуса")
                        calc.money = calc.money -50
                    else:
                        print("Недостаточно денег!")
            elif buy == "3":
                if "Электрогитара" in calc.items:
                    print("У тебя есть этот предмет!")
                    continue
                else:
                    if calc.money >= 75:
                        print("Вы купили Электрогитару!")
                        calc.items.append("Электрогитара")
                        calc.money = calc.money -75
                    else:
                        print("Недостаточно денег!")
            elif buy == "4":
                if "АААААААААААвтомобиль" in calc.items:
                    print("У тебя есть этот предмет!")
                    continue
                else:
                    if calc.money >= 150:
                        print("Вы купили АААААААААААвтомобиль!")
                        calc.items.append("АААААААААААвтомобиль")
                        calc.money = calc.money -150
                    else:
                        print("Недостаточно денег!")
            elif buy == "5":
                if "Ракета SpaceX" in calc.items:
                    print("У тебя есть этот предмет!")
                    continue
                else:
                    if calc.money >= 500:
                        print("Вы купили Ракету SpaceX!")
                        calc.items.append("Ракета SpaceX")
                        calc.money = calc.money -500
                    else:
                        print("Недостаточно денег!")
            elif buy == "6":
                if "Кошкодевочка от Tesla" in calc.items:
                    print("У тебя есть этот предмет!")
                    continue
                else:
                    if calc.money >= 1500:
                        print("Вы купили Кошкодевочку от Tesla!")
                        calc.items.append("Кошкодевочка от Tesla")
                        calc.money = calc.money -1500
                    else:
                        print("Недостаточно денег!")
            elif buy == "7":
                if "Вейп Братишкина" in calc.items:
                    print("У тебя есть этот предмет!")
                    continue
                else:
                    if calc.money >= 2500:
                        print("Вы купили Вейп Братишкина!")
                        calc.items.append("Вейп Братишкина")
                        calc.money = calc.money -2250
                    else:
                        print("Недостаточно денег!")
            elif buy == "8":
                if "Футболка \"КиШ\"" in calc.items:
                    print("У тебя есть этот предмет!")
                    continue
                else:
                    if calc.money >= 300:
                        print("Вы купили Футболку \"КиШ\"!")
                        calc.items.append("Футболка \"КиШ\"")
                        calc.money = calc.money -300
                    else:
                        print("Недостаточно денег!")
            elif buy == "9":
                if "ПК от ZyperPC" in calc.items:
                    print("У тебя есть этот предмет!")
                    continue
                else:
                    if calc.money >= 1000:
                        print("Вы купили ПК от ZyperPC!")
                        calc.items.append("ПК от ZyperPC")
                        calc.money = calc.money -1000
                    else:
                        print("Недостаточно денег!")
            elif buy.lower() == "Выход".lower():
                with shelve.open("log") as stat:
                    stat["денюжки"] = self.money
                break
            else:
                print("Не понимаю!")

# Кое чо из моего калькулятора, чо лень писать снова, но очень пиздато работает
def randomorgmain(random1, random2):
    url = "https://api.random.org/json-rpc/2/invoke"
    mykey = "cb5861a7-60c0-4513-af5b-f8df81aa8e7e"
    headers = {'content-type': 'application/json'}
    data = {'jsonrpc':'2.0',
           'method':'generateIntegers','params':
           {'apiKey':mykey,
           'n':1
           ,'min':random1
           ,'max':random2}
          ,'id':24565}
    params = json.dumps(data)
    try:
        r = requests.post(url, params, headers=headers, timeout=5)
        encode = r.json()
        rrandom = encode["result"]["random"]["data"][0]
    except:
        print("Рандом орг чота не работает или не может прислать рандом  в ответ. Мы тада используем программный")
        rrandom = random.randint(random1, random2)
    return rrandom

def clrclear():
    if platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
def delete():
    global yesorno
    print("Ты точно хочешь удалить данные?")
    while True:
        yesorno = input("Да или Нет: ")
        if yesorno.lower() == "Да".lower():
            if platform == "win32":
                os.remove("log.dat")
                os.remove("log.bak")
                os.remove("log.dir")
            else:
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

#фихня нужная для запоминания имени
memory = os.path.isfile("log")
if memory:
    with shelve.open("log") as stat:
        calc = stat["калк"]
        print("Здравствуй, {}".format(calc.name))
if memory == False:
    calc = Main()
    calc.login()
    calc = Main(name=calc.name, age=calc.age)
    with shelve.open("log") as stat:
        stat["калк"] = calc
#начало хы
helpme = """Функции этой прекрасной программы:
        0) Очистить
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
        11) Курс
        12) Хелп"""
try:
    print("Ладно, начнем-с")
    print(helpme)

    time.sleep(1)
    while True:
        enter = input(calc.name + "," " введи что тебе нужно: ")
        if enter.lower() == "Калькулятор".lower():
            calc.calcc()
        elif enter.lower() == "Шансы".lower():
            calc.chance()
        elif enter.lower() == "дата":
            calc.date()
        elif enter.lower() == "Число".lower():
            calc.randomn()
        elif enter.lower() == "Удалить данные".lower():
            delete()
        elif enter.lower() == "Работа".lower():
            calc.jobmain()
        elif enter.lower() == "Профиль".lower():
            calc.profile()
        elif enter.lower() == "Магазин".lower():
            #shop.shopping()
            calc.shopping()
        elif enter.lower() == "Уровень".lower():
            calc.levelup()
        elif enter.lower() == "погода":
            calc.weather()
        elif enter.lower() == "Курс".lower():
            calc.valute()
        elif enter.lower() == "Удача".lower():
            luck()
        elif enter.lower() == "очистить":
            clrclear()
        elif enter.lower() == "хелп":
            print(helpme)
        else:
            print("Не понимаю!")
#выход через ctrl+c
except KeyboardInterrupt:
    print("Выходим")
    with shelve.open("log") as stat:
        stat["калк"] = calc
    sys.exit()
