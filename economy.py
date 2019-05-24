from util import Main
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
                self.money = self.money + self.randomorgmain(1, 5)
                print("Ваш баланс {}".format(self.money))
            elif self.lvl == 1:
                    self.money = self.money + self.randomorgmain(5, 30)
                    print("Ваш баланс {}".format(self.money))
            elif self.lvl == 2:
                self.money = self.money + self.randomorgmain(25, 55)
                print("Ваш баланс {}".format(self.money))
            elif self.lvl == 3:
                self.money = self.money + self.randomorgmain(50, 90)
                print("Ваш баланс {}".format(self.money))
        elif jobtest.lower() == "выход":
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
# Хезе как по другому это реализовать
Main.profile = profile
Main.shopping = shopping
Main.jobmain = jobmain
