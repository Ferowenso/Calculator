import re, time, sys, json, requests, random, os
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

    def randomorgmain(self, random1, random2):
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

    def randomn(self, x=None, y=None):
        print("рандом в заданном диапазоне" )
        while True:
            try:
                if x and y:
                   x  = int(x); y = int(y)
                else:
                    x = int(input("Первое число: "))
                    y = int(input("Второе число: "))
                rand = self.randomorgmain(x, y)
                print("Число: {}".format(rand))
                self.vidachaxp()
                break
            except ValueError:
                print("Нужны числа!")
                break

    def orelireshka(self):
        print("Подбрасываем монетку..")
        random = self.randomorgmain(0, 2)
        if random == 0:
            print("Орел")
        elif random == 1:
            print("Решка")
        else:
            print("Карась")
    def date(self, event=None):
        print("Тут ты можешь узнать дату какого-либо события")
        if not event:
            event = input("Событие: ")
        day = self.randomorgmain(0, 31)
        moth = self.randomorgmain(1, 12)
        year = self.randomorgmain(2019, 3000)
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
        test = self.randomorgmain(0, 100)
        print("Шанс {} {}%" .format(event, test))
        self.xp = self.xp + random.randint(1, 10)


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
                if encalc == "+" or encalc == "сложение":
                    print("Вот твой результат, " + self.name + ": {}".format(x + y))
                elif encalc == "-" or encalc == "вычитание":
                    print("Вот твой результат, " + self.name + ": {}".format(x - y))
                elif encalc == "*" or encalc == "умножение":
                    print("Вот твой результат, " + self.name + ": {}".format(x * y))
                elif encalc == "**" or encalc == "степень":
                    print("Вот твой результат, " + self.name + ": {}".format(x ** y))
                elif encalc == "/":
                    try:
                        print("Вот твой результат, " + self.name + ": {}".format(x / y))
                    except ZeroDivisionError:
                        print("КАК ТЕБЕ УДАЛОСЬ ЭТО СДЕЛАТЬ? ПОЧЕМУ ЛЮДИ УМИРАЮТ")
                        break
                elif encalc == "корень":
                    print("Вот твой результат, " + self.name + ": {} и {}".format(math.sqrt(x), math.sqrt(y)))
                elif encalc == "синус":
                    print("Вот твой результат, " + self.name + ": {} и {}".format(math.sin(x), math.sin(y)))
                elif encalc == "косинус":
                    print("Вот твой результат, " + self.name + " :{} и {}".format(math.cos(x), math.cos(y)))
            self.vidachaxp()
            break

def clrclear():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
def delete():
    print("Ты точно хочешь удалить данные?")
    while True:
        yesorno = input("Да или Нет: ")
        if yesorno.lower() == "да":
            if sys.platform == "win32":
                os.remove("log.dat")
                os.remove("log.bak")
                os.remove("log.dir")
            else:
                os.remove("log")
            print("Удаление...")
            time.sleep(1)
            sys.exit()
        elif yesorno.lower() == "нет":
            print("Ну и зачем ты тогда сюда заходил?")
            break
        else:
            print("Да/Нет")
            continue
def exit(calc):
    print("Выходим")
    time.sleep(1)
    with shelve.open("log") as stat:
        stat["калк"] = calc
    sys.exit()

def editsetting():
    while 1:
        edit = input("Чтобы изменить задержку - напишите 1: ")
        if edit == "1":
            try:
                test  = float(input("введите новое значение: "))
                if not test:
                    continue
                setting["timesleep"] = test
                with open("log.json", "w") as stat:
                    json.dump(setting, stat)
                break
            except ValueError:
                print("цыфорками!")
                continue
