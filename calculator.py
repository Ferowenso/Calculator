# импорт всего шо надо
import math, time, re, shelve, sys, random, os.path, json
from sys import platform
try:
    import requests
except ModuleNotFoundError:
    print("У вас не установлен requests!")
    sys.exit()
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
    def vidachaxp(self):
        if self.lvl == 0:
            self.xp = self.xp + random.randint(0, 5)
        elif self.lvl == 1:
            self.xp = self.xp + random.randint(0, 10)
        elif self.lvl == 2:
            self.xp = self.xp + random.randint(0, 15)
        else:
            self.xp = self.xp + random.randint(10, 30)

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
        time.sleep(0.5)
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

    def randomn(self, x=None, y=None):
        print("рандом в заданном диапазоне" )
        while True:
            try:
                if x and y:
                   x  = int(x); y = int(y)
                else:
                    x = int(input("Первое число: "))
                    y = int(input("Второе число: "))
                rand = randomorgmain(x, y)
                print("Число: {}".format(rand))
                self.vidachaxp()
                break
            except ValueError:
                print("Нужны числа!")
                break

    def date(self, event=None):
        print("Тут ты можешь узнать дату какого-либо события")
        if not event:
            event = input("Событие: ")
        day = randomorgmain(0, 31)
        moth = randomorgmain(1, 12)
        year = randomorgmain(2019, 3000)
        print("Дата {}: {}.{}.{}".format(event, day, moth, year))
        self.xp = self.xp + random.randint(1, 10)
    def translit(self, text):
        apikey = "trnsl.1.1.20190508T201810Z.385ebfa1e596baa0.90672cf8655555b1b51ced31b03c2e8bb9bde46c"
        url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
        params = {"key": apikey,
                "text":text,
                "lang":"ru-en"}
        r = requests.get(url, params=params)
        encode = r.json()
        return encode["text"][0]

    def chance(self, argevent):
        print("Тут ты можешь узнать вероятность какого-либо события")
        if argevent:
           event = argevent
        else:
            event = input("Событие: ")
        test = randomorgmain(0, 100)
        print("Шанс {} {}%" .format(event, test))
        self.xp = self.xp + random.randint(1, 10)

    def valute(self):
        api = "https://www.cbr-xml-daily.ru/daily_json.js"
        print("Это курс валют, товарищ {}!" .format(self.name))
        r = requests.get(api)
        encode = r.json()
        usd = encode["Valute"]["USD"]["Value"]
        eur = encode["Valute"]["EUR"]["Value"]
        print("Курс рубля")
        print("Доллар: {}₽, евро: {}₽ \n" .format(usd, eur))
        print("Курс битка")
        r = requests.get("https://blockchain.info/ru/ticker")
        encode = r.json()
        rub = encode["RUB"]["15m"]
        usd1 = encode["USD"]["15m"]
        print("Рубль: {}₽, доллар: {}$" .format(rub, usd))
        self.xp = self.xp + random.randint(1, 10)

    def weather(self, qr=None):
        while True:
            apiurl = "http://api.openweathermap.org/data/2.5/find"
            if not qr:
                print("Введите название города")
                qr = input("город: ")
            qr = qr.lower()
            q = self.translit(qr)
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
                print("что ты черт побери такое несешь? нет такого города, попробуй ввести на английском")
                break
            print("""Город: {}
            Погода: {}
            Температура: {}°
            Влажность: {}
            Скорость ветра: {}м/с""".format(qr, w, temp, vlaga, wind))
            self.xp = self.xp + random.randint(1, 10)
            break
    def calcc(self, x=None, entercalc=None, y=None):
        while True:
            try:
                if x and y:
                   x  = int(x); y = int(y)
                else:
                    x = int(input("Первое значение: "))
                    y = int(input("Второе значение: "))
            except ValueError:
                print("Цифорками!")
                x = None; y = None
            else:
                if entercalc:
                    encalc = entercalc
                else:
                    encalc = input("""Введи что тебе нужно:
• Сложение +
• Вычитание -
• Умножение *
• Деление /
• Степень так же
• Корень так же
• Синус так же
• Косинус так же
• Выход
""")
                    encalc = encalc.lower()
                if encalc == "+":
                    print("Вот твой результат, " + calc.name + ": {}".format(x + y));calc.vidachaxp()
                elif encalc == "-":
                    print("Вот твой результат, " + calc.name + ": {}".format(x - y));calc.vidachaxp()
                elif encalc == "*":
                    print("Вот твой результат, " + calc.name + ": {}".format(x * y));calc.vidachaxp()
                elif encalc == "**":
                    print("Вот твой результат, " + calc.name + ": {}".format(x ** y));calc.vidachaxp()
                elif encalc == "/":
                    try:
                        print("Вот твой результат, " + calc.name + ": {}".format(x / y));calc.vidachaxp()
                    except ZeroDivisionError:
                        print("КАК ТЕБЕ УДАЛОСЬ ЭТО СДЕЛАТЬ? ПОЧЕМУ ЛЮДИ УМИРАЮТ")
                        break
                elif encalc == "корень":
                    print("Вот твой результат, " + calc.name + ": {} и {}".format(math.sqrt(x), math.sqrt(y)));calc.vidachaxp()
                elif encalc == "синус":
                    print("Вот твой результат, " + calc.name + ": {} и {}".format(math.sin(x), math.sin(y)));calc.vidachaxp()
                elif encalc == "косинус":
                    print("Вот твой результат, " + calc.name + " :{} и {}".format(math.cos(x), math.cos(y)));calc.vidachaxp()
            break

    def profile(self):
        print("""Ваше имя: {}
Ваш возраст:{}
Ваш баланс:{}$""".format(self.name, self.age, self.money))
        print("Ваши предметы:")
        for it in self.items:
            print(" •" + it)
        print("""Ваш опыт: {}xp
Ваш уровень:{}  """.format(self.xp, self.lvl))
    def jobmain(self):
        while True:
            print("""Напишите \"Работать\", чтобы работать
\"Выход\", чтобы выйти""")
            jobtest = input()
            if jobtest.lower() == "работать":
                if self.lvl == 0:
                    self.money = self.money + randomorgmain(1, 5)
                    print("Ваш баланс {}".format(self.money))
                elif self.lvl == 1:
                        self.money = self.money + randomorgmain(5, 30)
                        print("Ваш баланс {}".format(self.money))
                elif self.lvl == 2:
                    self.money = self.money + randomorgmain(25, 55)
                    print("Ваш баланс {}".format(self.money))
                elif self.lvl == 3:
                    self.money = self.money + randomorgmain(50, 90)
                    print("Ваш баланс {}".format(self.money))
            elif jobtest.lower() == "выход":
                break
            else:
                print("шо?")
    def prefix(self, selfprefix):
        while 1:
            if self.lvl < 2:
                print("Префикс доступен со второго уровня!")
                break
            else:
                if selfprefix:
                        self.name = selfprefix
                        if not self.name:
                            print("Ну и зачем мне пустой ответ, а?")
                            continue
                        break
                else:
                        self.name = input("Введите префикс: ")
                        if not self.name:
                            print("Ну и зачем мне пустой ответ, а?")
                            continue
                        break
    def bomb(self):
        print("""В этой игре вам нужно угадать верный провод для того чтобы разминировать бомбу
Есть 4 провода:
З - зеленый
Ж - желтый
К - красный
О - оранжевый
Вы должны сделать ставку
Минимум - 50$""")
        while True:
            print("Продолжить? Да/Нет")
            bombyes = input("")
            bombyes = bombyes.lower()
            if bombyes == "да":
                try:
                    stavka = int(input("Ставка: "))
                    if stavka < 50:
                        print("Минимум 50$!")
                        continue
                    if stavka > self.money:
                        print("Меньше!")
                        continue
                except ValueError:
                    print("Число!")
                    continue
                print("""Ваша ставка: {}
Если вы выйграете +{}$
Если проиграете -{}$""".format(stavka, stavka * 2, stavka))
                provod = ["з", "ж", "к", "о"]
                randomprovod = random.choice(provod)
                choiceprovod = input("Выберите провод: ")
                choiceprovod = choiceprovod.lower()
                if not all([choiceprovod in provod]):
                    print("Напишите букву провода!")
                    continue
                elif choiceprovod == "з" or "ж" or "к" or "о":
                    if choiceprovod == randomprovod:
                        print("Вы угадали! +{}$".format(stavka * 2))
                        self.money = self.money + stavka * 2
                    else:
                        print("Вы проиграли! -{}$".format(stavka))
                        self.money = self.money - stavka
            elif bombyes == "нет":
                break
            else:
                print("шо?")
                continue
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
            elif lvbuy.lower() == "выход":
                break
            else:
                print("шо?")
    def luck(self):
        while True:
            print("""Это игра на удачу
1 игра - 100$
Если 2 числа совпадут - +500$
Если 3 числа совпадут - +2500$
Вы хотите продолжить? Да/Нет""")
            entcas = input("")
            if entcas.lower() == "да":
                if self.money >= 100:
                    self.money = self.money -100
                    first = randomorgmain(1, 9)
                    second = randomorgmain(1, 9)
                    third = randomorgmain(1, 9)
                    print("Числа: {}, {}, {}".format(first, second, third))
                    if first == second and first != third:
                        self.money = self.money + 500
                        print("Два числа совпали! +500$")
                        print("Ваш баланс {}".format(self.money))
                    elif first == third and second != third:
                        self.money = self.money + 500
                        print("Два числа совпали! +500$")
                        print("Ваш баланс {}".format(self.money))
                    elif second == third and first != second:
                        self.money = self.money + 500
                        print("Два числа совпали! +500$")
                        print("Ваш баланс {}".format(self.money))
                    elif first == second == third:
                        self.money = self.money + 2500
                        print("Три числа совпали! +2500$")
                        print("Ваш баланс {}".format(self.money))
                    else:
                        print("Вы проиграли D:")
                else:
                    print("Недостаточно денег!")
            elif entcas.lower() == "нет":
                break
            else:
                print("шо?")
    def secret(self):
        self.money = self.money + 99999

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
                        self.money = self.money - 10
                    else:
                        print("Недостаточно денег!")
            elif buy == "2":
                if "Мерч Хесуса" in self.items:
                    print("У тебя есть этот предмет!")
                    continue
                else:
                    if self.money >= 50:
                        print("Вы купили Мерч Хесуса!")
                        calc.items.append("Мерч Хесуса")
                        self.money = self.money -50
                    else:
                        print("Недостаточно денег!")
            elif buy == "3":
                if "Электрогитара" in self.items:
                    print("У тебя есть этот предмет!")
                    continue
                else:
                    if self.money >= 75:
                        print("Вы купили Электрогитару!")
                        self.items.append("Электрогитара")
                        self.money = self.money -75
                    else:
                        print("Недостаточно денег!")
            elif buy == "4":
                if "АААААААААААвтомобиль" in self.items:
                    print("У тебя есть этот предмет!")
                    continue
                else:
                    if self.money >= 150:
                        print("Вы купили АААААААААААвтомобиль!")
                        self.items.append("АААААААААААвтомобиль")
                        self.money = self.money -150
                    else:
                        print("Недостаточно денег!")
            elif buy == "5":
                if "Ракета SpaceX" in self.items:
                    print("У тебя есть этот предмет!")
                    continue
                else:
                    if self.money >= 500:
                        print("Вы купили Ракету SpaceX!")
                        self.items.append("Ракета SpaceX")
                        self.money = self.money -500
                    else:
                        print("Недостаточно денег!")
            elif buy == "6":
                if "Кошкодевочка от Tesla" in self.items:
                    print("У тебя есть этот предмет!")
                    continue
                else:
                    if self.money >= 1500:
                        print("Вы купили Кошкодевочку от Tesla!")
                        self.items.append("Кошкодевочка от Tesla")
                        self.money = self.money -1500
                    else:
                        print("Недостаточно денег!")
            elif buy == "7":
                if "Вейп Братишкина" in self.items:
                    print("У тебя есть этот предмет!")
                    continue
                else:
                    if self.money >= 2500:
                        print("Вы купили Вейп Братишкина!")
                        self.items.append("Вейп Братишкина")
                        self.money = self.money -2250
                    else:
                        print("Недостаточно денег!")
            elif buy == "8":
                if "Футболка \"КиШ\"" in self.items:
                    print("У тебя есть этот предмет!")
                    continue
                else:
                    if self.money >= 300:
                        print("Вы купили Футболку \"КиШ\"!")
                        self.items.append("Футболка \"КиШ\"")
                        self.money = self.money -300
                    else:
                        print("Недостаточно денег!")
            elif buy == "9":
                if "ПК от ZyperPC" in self.items:
                    print("У тебя есть этот предмет!")
                    continue
                else:
                    if self.money >= 1000:
                        print("Вы купили ПК от ZyperPC!")
                        self.items.append("ПК от ZyperPC")
                        self.money = self.money -1000
                    else:
                        print("Недостаточно денег!")
            elif buy.lower() == "выход":
                break
            else:
                print("Не понимаю!")

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
    print("Ты точно хочешь удалить данные?")
    while True:
        yesorno = input("Да или Нет: ")
        if yesorno.lower() == "да":
            if platform == "win32":
                os.remove("log.dat")
                os.remove("log.bak")
                os.remove("log.dir")
            else:
                os.remove("log")
            print("Удаление...")
            time.sleep(0.5)
            sys.exit()
        elif yesorno.lower() == "нет":
            print("Ну и зачем ты тогда сюда заходил?")
            break
        else:
            print("Да/Нет")
            continue
def exit():
    print("Выходим")
    time.sleep(0.5)
    with shelve.open("log") as stat:
        stat["калк"] = calc
    sys.exit()
#фихня нужная для запоминания имени
if platform == "win32":
    memory = os.path.isfile("log.dat")
else:
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
    print(calc.name + ", наш агент фсб уже выслан к вам \n")
#начало хы
def lobby():
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
            12) Хелп
            13) Бомба
            14) Префикс
            (все данные сохраняются только при написании команды "Выход"!) """
    try:
        print("Ладно, начнем-с")
        print(helpme)

        time.sleep(0.5)
        while True:
            enter = input("{}, ваш запрос: ".format(calc.name))
            enter = enter.lower()
            args1 = None
            args2 = None
            args3 = None
            uberargs = None
            zapros = enter.split()[0]
            if not enter:
                continue
            try:
                if enter.split()[1]:
                    args1 = enter.split()[1]
                    args2 = enter.split()[2]
                    args3 = enter.split()[3]
            except IndexError: None
            if zapros == "калькулятор":
                calc.calcc(args1, args2, args3)
            elif enter.split()[0] == "шансы":
                calc.chance(args1)
            elif zapros == "дата":
                calc.date(args1)
            elif enter == "удалить данные":
                delete()
            elif zapros == "число":
                calc.randomn(args1, args2)
            elif zapros == "удалить данные":
                delete()
            elif zapros == "работа":
                calc.jobmain()
            elif zapros == "профиль":
                calc.profile()
            elif zapros == "магазин":
                calc.shopping()
            elif zapros == "уровень":
                calc.levelup()
            elif zapros == "погода":
                calc.weather(args1)
            elif zapros == "курс":
                calc.valute()
            elif zapros  == "удача":
                calc.luck()
            elif zapros == "очистить":
                clrclear()
            elif zapros == "хелп":
                print(helpme)
            elif zapros == "майнкрафт":
                calc.secret()
            elif zapros == "бомба":
                calc.bomb()
            elif zapros == "выход":
                exit()
            elif zapros == "префикс":
                calc.prefix(args1)
            else:
                print("Не понимаю!")

#выход через ctrl+c
    except KeyboardInterrupt:
        print("Выходим")
        with shelve.open("log") as stat:
            stat["калк"] = calc
        sys.exit()
lobby()
