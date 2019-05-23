from main import Main
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
Main.profile = profile
