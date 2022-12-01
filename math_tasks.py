import math
import random


class math_tasks:

    def task1(self, calculation_number: int):
        task1_tasknumber = random.randint(0, 9)
        task1_tasknumber_multiplication = random.randint(0, 4)
        task1_task = task1_tasknumber + calculation_number * task1_tasknumber_multiplication
        answer = int(input(f"\n Udregn: {task1_tasknumber} + {calculation_number} * {task1_tasknumber_multiplication}: "))

        if task1_task == answer:
            print(" Rigtigt svar.")
            return 1
        else:
            print(f" Forkert svar; {task1_task}")
            return 0

    def task2(self, substract_number):
        task2_tasknumber = random.randint(0, 9)
        task2_tasknumber_substract = random.randint(0, 4)
        task2_task = task2_tasknumber - substract_number * task2_tasknumber_substract
        answer = int(input(f"\n Udregn: {task2_tasknumber} - {substract_number} * {task2_tasknumber_substract}: "))

        if task2_task == answer:
            print(" Rigtigt svar.")
            return 1
        else:
            print(f" Forkert svar; {task2_task}")
            return 0

    def task3(self, found_number):
        task3_tasknumber = random.randint(1, 9)
        task3_tasknumber_found_out = random.randint(1, 4)
        task3_task = task3_tasknumber / task3_tasknumber_found_out
        answer = int(input(f"\n Udregn: {task3_tasknumber} / X = {task3_task} | "))
        if task3_tasknumber_found_out == answer:
            print(" Rigtigt svar.")
            return 1
        else:
            print(f" Forkert svar; X={task3_tasknumber_found_out}")
            return 0


    def task4(self, multi_number):
        task4_tasknumber = random.randint(0, 2)
        task4_tasknumber_substract = random.randint(0, 4)
        task4_task = task4_tasknumber * multi_number * task4_tasknumber_substract
        answer = int(input(f"\n Udregn: {task4_tasknumber} * {multi_number} * {task4_tasknumber_substract}: "))

        if task4_task == answer:
            print(" Rigtigt svar.")
            return 1
        else:
            print(f" Forkert svar; {task4_task}")
            return 0


    def task5(self, substract):
        task5_tasknumber = random.randint(0, 2)
        task5_tasknumber_substract = random.randint(0, 4)
        task5_task = task5_tasknumber - substract - task5_tasknumber_substract
        answer = int(input(f"\n Udregn: {task5_tasknumber} - {task5_tasknumber_substract} - {substract}: "))

        if task5_task == answer:
            print(" Rigtigt svar.")
            return 1
        else:
            print(f" Forkert svar; {task5_task}")
            return 0
