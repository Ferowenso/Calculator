#!/usr/bin/env python
import math, time, re, shelve, sys, random, os.path, json, getpass
from main import *
try:
    import requests
except ModuleNotFoundError:
    print("У вас не установлен requests!")
    sys.exit()
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
            time.sleep(setting["timesleep"])
            sys.exit()
        elif yesorno.lower() == "нет":
            print("Ну и зачем ты тогда сюда заходил?")
            break
        else:
            print("Да/Нет")
            continue
def exit(calc):
    print("Выходим")
    time.sleep(setting["timesleep"])
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

def lobby(calc, zapros=None, args1=None, args2=None, args3=None, argvtest=None, logfile=None):
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
            15) Монета
            16) Конфиг
            (все данные сохраняются только при написании команды "Выход"!) """
    try:
        if not zapros:
            print("Здравствуй," , calc.name)
            print("Ладно, начнем-с")
            time.sleep(setting["timesleep"])
            print(helpme)

        while True:
            if zapros == None:
                enter = input("{}, ваш запрос: ".format(calc.name))
                enter = enter.lower()
                args1 = None
                args2 = None
                args3 = None
                if not enter:
                    continue
                zapros = enter.split()[0]
                try:
                    args1 = enter.split()[1]
                    args2 = enter.split()[2]
                    args3 = enter.split()[3]
                except IndexError: None
            if zapros == "калькулятор":
                calc.calcc(args1, args2, args3)
            elif zapros == "шансы":
                calc.chance(args1)
            elif zapros == "дата":
                calc.date(args1)
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
                exit(calc)
            elif zapros == "префикс":
                calc.prefix(args1)
            elif zapros == "монета":
                calc.orelireshka()
            elif zapros == "конфиг":
                editsetting()
            else:
                print("Не понимаю!")
            if argvtest:
                sys.exit()
            zapros = None

#выход через ctrl+c
    except (KeyboardInterrupt, EOFError):
        print("Выходим")
        with shelve.open(logfile) as stat:
            stat["калк"] = calc
        sys.exit()
#фихня нужная для запоминания имени
def run():
    global setting
    if sys.platform == "win32":
        logfile = "log"
        jsonfile = "log.json"
        memory = os.path.isfile("log.dat")
    else:
        logfile = "/home/{}/log".format(getpass.getuser())
        jsonfile = "/home/{}/log.json".format(getpass.getuser())
        memory = os.path.isfile(logfile)
    jsontest = os.path.isfile(jsonfile)
    if all([memory, jsontest]):
        with shelve.open(logfile) as stat:
            calc = stat["калк"]
        with open(jsonfile, "r") as stat:
            setting = json.load(stat)
    else:
        calc = Main()
        setting = {"timesleep": 1}
        with open(jsonfile, "w") as stat:
            json.dump(setting, stat)
        calc.login()
        calc = Main(name=calc.name, age=calc.age)
        with shelve.open(logfile) as stat:
            stat["калк"] = calc
        print(calc.name + ", наш агент фсб уже выслан к вам ")
    key = None
    args1= None
    args2 = None
    args3 = None
    argvtest = False
    try:
        key = sys.argv[1]
        args1 = sys.argv[2]
        args2 = sys.argv[3]
        args3 = sys.argv[4]
    except IndexError: None
    if key == os.path.basename(__file__):
        key = None
    if key:
        argvtest = True
    lobby(calc, key, args1, args2, args3, argvtest, logfile)
if __name__ == "__main__":
    run()
