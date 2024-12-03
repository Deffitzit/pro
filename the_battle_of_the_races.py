# Задание №1




# myname = input("Введите своё имя:")
# print("Здравствуйте,", myname)




# Задание №2




# a = int(input("Введите первое число:"))
# b = int(input("Введите второе число:"))

# print("Сложение: ", a + b)
# print("Вычитание: ", a - b)
# print("Умножение: ", a * b)
# print("Возведение в степень: ", a ** b)

# if b == 0:
#     print ("деление на 0 запрещено")
# else:
#     print("Деление: ", a / b)
#     print("Деление без остатка: ", a // b)
#     print("Остаток от деления: ", a % b)




# Задание №3




# import random
# from random import randint

# a = []

# for i in range(30):
#     a.append(randint(1,30))

# print(a)
# print(sorted(a))
# a = sorted(a)
# print("минимальное значение", a[0])
# print("максимальное значение", a[-1])




# Задание №4




# import random
# from random import randint
# from tkinter import filedialog

# def create(count):
#     i = 0
#     while i < count:
#         filename = "name" + str(i)
#         a = []
#         file = open(filename, "w+")
#         for c in range(10):
#             a_num = randint(1, 100)
#             a.append(a_num)
#         for k in range(len(a)):
#             file.write(str(a[k]) + " ")
#         file.close()
#         i += 1
# create(10)

# file = filedialog.askopenfilename()
# if file != "":
#     file_r = open(file, "r")
#     data = file_r.read()
#     print("\n", ">>>>>", data)
#     data_l = data.split(" ")
#     data_s = 0
#     for y in range(len(data_l)-1):
#         data_s = data_s + int(data_l[y])
#     data_arifmet = data_s / (len(data_l)-1)
#     print ("\n", "среднее арифметическое - ", data_arifmet, "\n")
#     file_r.close()


# Задание №5

import tkinter as tk
from tkinter import messagebox
from tkinter import *

class Storage:
    def __init__(self, *, level: int) -> None:
        self.level = level
        self.health_points = self.race_health_points * level 
        self.attack_power = self.race_attack_power * level 

    def attack(self, *, target: "Storage") -> None: 
        target.health_points -= self.attack_power

    def is_alive(self) -> bool: 
        return self.health_points > 0

    def __str__(self) -> str: 
        return f"{self.race_name} >>> (уровень: {self.level}, HP: {self.health_points})"

class Ork(Storage):
    race_health_points = 90
    race_attack_power = 10
    race_name = "Орк"

class Elf(Storage):
    race_health_points = 40
    race_attack_power = 30
    race_name = "Эльф"

class Dwarf(Storage):
    race_health_points = 65
    race_attack_power = 20
    race_name = "Дворф"

class Goblin(Storage):
    race_health_points = 35
    race_attack_power = 40
    race_name = "Гоблин"

def fight(*, race_1: Storage, race_2: Storage) -> str:
    results = []
    while race_1.is_alive() and race_2.is_alive():
        race_1.attack(target=race_2)
        results.append(f"{race_1.race_name} (HP: {race_1.health_points}) +-|=====- {race_2.race_name} (HP: {race_2.health_points})")
        if race_2.is_alive():
            race_2.attack(target=race_1)
            results.append(f"{race_2.race_name} (HP: {race_2.health_points}) +-|=====- {race_1.race_name} (HP: {race_1.health_points})")

    winner = race_1 if race_1.is_alive() else race_2
    results.append(f"Победитель: {winner}")
    return "\n".join(results)

def start_fight():
    race_1_name = race_1_var.get()
    race_2_name = race_2_var.get()
    level_1 = level_1_var.get()
    level_2 = level_2_var.get()
    
    races = {
        "Орк": Ork,
        "Эльф": Elf,
        "Дворф": Dwarf,
        "Гоблин": Goblin
    }
    
    race_1 = races[race_1_name](level=level_1)
    race_2 = races[race_2_name](level=level_2)
    
    result = fight(race_1=race_1, race_2=race_2)
    messagebox.showinfo("Результат битвы", result)

root = tk.Tk()
root.title("Битва Рас")
root.geometry('800x600')
root.resizable(width=False, height=False)

# bg = PhotoImage(file='fone.png')
# bg_logo = Label(root, image=bg)
# bg_logo.place(x=0, y=0, relwidth=1, relheight=1)

race_1_var = tk.StringVar(value="Орк")
race_2_var = tk.StringVar(value="Эльф")
level_1_var = tk.IntVar(value=1)
level_2_var = tk.IntVar(value=1)


tk.Label(root, text="Выберите первого война:").pack()
tk.OptionMenu(root, race_1_var, "Орк", "Эльф", "Дворф", "Гоблин").pack()

tk.Label(root, text="Выберите уровень для первого война:").pack()
tk.Scale(root, from_=1, to=100, variable=level_1_var, orient="horizontal").pack()

tk.Label(root, text="Выберите второго война:").pack()
tk.OptionMenu(root, race_2_var, "Орк", "Эльф", "Дворф", "Гоблин").pack()

tk.Label(root, text="Выберите уровень для второго война:").pack()
tk.Scale(root, from_=1, to=100, variable=level_2_var, orient="horizontal").pack()

tk.Button(root, text="Начать битву", command=start_fight).pack()

root.mainloop()
