#!/usr/bin/env python
import shelve, sys, os.path
from main import *
from economika import *
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

def lobby(calc, zapros=None, args1=None, args2=None, args3=None, argvtest=None):
    #начало хы
    helpme = """Функции этой прекрасной программы:
             •  Очистить | clear
             •  Калькулятор | calc
             •  Шансы
             •  Дата | data
             •  Число
             •  Удалить данные
             •  Работа | job
             •  Профиль
             •  Магазин
             •  Уровень
             •  Погода
             •  Курс
             •  Хелп
             •  Бомба
             •  Префикс
             •  Монета
             •  Конфиг
                (все данные сохраняются только при написании команды "Выход"!) """
    try:
        if not zapros:
            print("Здравствуй," , calc.name)
            time.sleep(1)
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
            if zapros == "калькулятор" or zapros == "calc":
                calc.calcc(args1, args2, args3)
            elif zapros == "шансы":
                calc.chance(args1)
            elif zapros == "дата" or zapros == "data":
                calc.date(args1)
            elif zapros == "число":
                calc.randomn(args1, args2)
            elif zapros == "удалить данные":
                delete()
            elif zapros == "работа" or zapros == "job":
                calc.jobmain()
            elif zapros == "профиль":
                calc.profile()
            elif zapros == "магазин" or zapros ==  "shop":
                calc.shopping()
            elif zapros == "уровень" or zapros == "lvl":
                calc.levelup()
            elif zapros == "погода" or zapros == "weather":
                calc.weather(args1)
            elif zapros == "курс":
                calc.valute()
            elif zapros  == "удача":
                calc.luck()
            elif zapros == "очистить" or zapros == "clear":
                clrclear()
            elif zapros == "хелп" or zapros == "help":
                print(helpme)
            elif zapros == "майнкрафт":
                calc.secret()
            elif zapros == "бомба":
                calc.bomb()
            elif zapros == "выход" or zapros == "exit":
                exit(calc)
            elif zapros == "префикс":
                calc.prefix(args1)
            elif zapros == "монета":
                calc.orelireshka()
            elif zapros == "конфиг":
                print("временно вырезал из калькулятора")
            else:
                print("Не понимаю!")
            if argvtest:
                sys.exit()
            zapros = None

#выход через ctrl+c
    except (KeyboardInterrupt, EOFError):
        print("Выходим")
        with shelve.open("log") as stat:
            stat["калк"] = calc
        sys.exit()
#фихня нужная для запоминания имени
def run():
    if sys.platform == "win32":
        memory = os.path.isfile("log.dat")
    else:
        memory = os.path.isfile("log")
    jsontest = os.path.isfile("log.json")
    if all([memory, jsontest]):
        with shelve.open("log") as stat:
            calc = stat["калк"]
        with open("log.json", "r") as stat:
            setting = json.load(stat)
    else:
        calc = Main()
        setting = {"timesleep": 1}
        with open("log.json", "w") as stat:
            json.dump(setting, stat)
        calc.login()
        calc = Main(name=calc.name, age=calc.age)
        with shelve.open("log") as stat:
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
    lobby(calc, key, args1, args2, args3, argvtest)
if __name__ == "__main__":
    run()
