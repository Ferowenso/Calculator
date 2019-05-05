import shelve
class Main2():
    def shopping(self):
        while True:
            with shelve.open("log") as stat:
                try:
                    shop = stat["магаз"]
                    calc = stat["калк"]
                except KeyError:
                    stat["калк"] = calc
                    stat["магаз"] = shop
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
                if "Шапка-ушанка" in calc.items:
                    print("У тебя есть этот предмет!")
                    continue
                else:
                    if calc.money >= 10:
                        print("Вы купили Шапку-ушанку!")
                        items.append("Шапка-ушанка")
                        calc.money = calc.money -10
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
                break
            else:
                print("Не понимаю!")
