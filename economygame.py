from util import Main
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
                first = self.randomorgmain(1, 9)
                second = self.randomorgmain(1, 9)
                third = self.randomorgmain(1, 9)
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
Main.bomb = bomb
Main.luck = luck
