import shelve
def shopping():
    global money
    global items
    items = []
    while True:
        with shelve.open("log.dat") as stat:
            try:
                items = stat["магаз"]
                money = stat["денюжки"]
            except KeyError:
                stat["магаз"] = items
                stat["денюжки"] = money
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
            if "Шапка-ушанка" in items:
                print("У тебя есть этот предмет!")
                continue
            else:
                if money >= 10:
                    print("Вы купили Шапку-ушанку!")
                    items.append("Шапка-ушанка")
                    money = money -10
                    with shelve.open ("log.dat") as stat:
                        stat["магаз"] = items
                        stat["денюжки"] = money
                else:
                    print("Недостаточно денег!")
        elif buy == "2":
            if "Мерч Хесуса" in items:
                print("У тебя есть этот предмет!")
                continue
            else:
                if money >= 50:
                    print("Вы купили Мерч Хесуса!")
                    items.append("Мерч Хесуса")
                    money = money -50
                    with shelve.open ("log.dat") as stat:
                        stat["магаз"] = items
                        stat["денюжки"] = money
                else:
                    print("Недостаточно денег!")
        elif buy == "3":
            if "Электрогитара" in items:
                print("У тебя есть этот предмет!")
                continue
            else:
                if money >= 75:
                    print("Вы купили Электрогитару!")
                    items.append("Электрогитара")
                    money = money -75
                    with shelve.open ("log.dat") as stat:
                        stat["магаз"] = items
                        stat["денюжки"] = money
                else:
                    print("Недостаточно денег!")
        elif buy == "4":
            if "АААААААААААвтомобиль" in items:
                print("У тебя есть этот предмет!")
                continue
            else:
                if money >= 150:
                    print("Вы купили АААААААААААвтомобиль!")
                    items.append("АААААААААААвтомобиль")
                    money = money -150
                    with shelve.open ("log.dat") as stat:
                        stat["магаз"] = items
                        stat["денюжки"] = money
                else:
                    print("Недостаточно денег!")
        elif buy == "5":
            if "Ракета SpaceX" in items:
                print("У тебя есть этот предмет!")
                continue
            else:
                if money >= 500:
                    print("Вы купили Ракету SpaceX!")
                    items.append("Ракета SpaceX")
                    money = money -500
                    with shelve.open ("log.dat") as stat:
                        stat["магаз"] = items
                        stat["денюжки"] = money
                else:
                    print("Недостаточно денег!")
        elif buy == "6":
            if "Кошкодевочка от Tesla" in items:
                print("У тебя есть этот предмет!")
                continue
            else:
                if money >= 1500:
                    print("Вы купили Кошкодевочку от Tesla!")
                    items.append("Кошкодевочка от Tesla")
                    money = money -1500
                    with shelve.open ("log.dat") as stat:
                        stat["магаз"] = items
                        stat["денюжки"] = money
                else:
                    print("Недостаточно денег!")
        elif buy == "7":
            if "Вейп Братишкина" in items:
                print("У тебя есть этот предмет!")
                continue
            else:
                if money >= 2500:
                    print("Вы купили Вейп Братишкина!")
                    items.append("Вейп Братишкина")
                    money = money -2250
                    with shelve.open ("log.dat") as stat:
                        stat["магаз"] = items
                        stat["денюжки"] = money
                else:
                    print("Недостаточно денег!")
        elif buy == "8":
            if "Футболка \"КиШ\"" in items:
                print("У тебя есть этот предмет!")
                continue
            else:
                if money >= 300:
                    print("Вы купили Футболку \"КиШ\"!")
                    items.append("Футболка \"КиШ\"")
                    money = money -300
                    with shelve.open ("log.dat") as stat:
                        stat["магаз"] = items
                        stat["денюжки"] = money
                else:
                    print("Недостаточно денег!")
        elif buy == "9":
            if "ПК от ZyperPC" in items:
                print("У тебя есть этот предмет!")
                continue
            else:
                if money >= 1000:
                    print("Вы купили ПК от ZyperPC!")
                    items.append("ПК от ZyperPC")
                    money = money -1000
                    with shelve.open ("log.dat") as stat:
                        stat["магаз"] = items
                        stat["денюжки"] = money
                else:
                    print("Недостаточно денег!")
        elif buy.lower() == "Выход".lower():
            break
        else:
            print("Не понимаю!")
