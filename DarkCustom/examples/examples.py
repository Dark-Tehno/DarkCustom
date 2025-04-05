import time
import threading
from DarkCustom.DarkCustom import DarkInput, DarkPrint, DarkConfirm, DarkProgressBar, DarkSpinner

# Пример использования DarkInput
print("Примеры использования DarkInput:")

# Ввод строки с кастомными цветами
name = DarkInput(prompt="Введите ваше имя: ", rgb_prompt=(0, 255, 0), rgb_input=(255, 255, 0))
DarkPrint(f"Привет, {name}!", rgb_values=(0, 255, 255))

# Ввод целого числа с проверкой диапазона
age = DarkInput(prompt="Введите ваш возраст: ", rgb_prompt=(0, 255, 0), rgb_input=(255, 255, 0), data_type="int", min_value=0, max_value=120)
DarkPrint(f"Вам {age} лет.", rgb_values=(0, 255, 255))

# Ввод числа с плавающей точкой
height = DarkInput(prompt="Введите ваш рост (в метрах): ", rgb_prompt=(0, 255, 0), rgb_input=(255, 255, 0), data_type="float", min_value=0.5, max_value=2.5)
DarkPrint(f"Ваш рост {height} м.", rgb_values=(0, 255, 255))

# Ввод пароля
password = DarkInput(prompt="Введите пароль: ", rgb_prompt=(255, 0, 0), type="password")
DarkPrint("Пароль введен.", rgb_values=(255, 0, 255))

# Пример использования DarkPrint
print("\nПримеры использования DarkPrint:")

# Вывод строки с кастомным цветом
DarkPrint("Это строка с кастомным цветом!", rgb_values=(255, 0, 0))

# Вывод нескольких значений с разными цветами
DarkPrint("Значение 1", "Значение 2", "Значение 3", rgb_values=(0, 255, 0), rgb_sep=(255, 0, 255))

# Вывод с кастомным разделителем и окончанием
DarkPrint("Первая часть", "Вторая часть", sep=" | ", end=" ***\n", rgb_values=(0, 0, 255), rgb_sep=(255, 255, 0), rgb_end=(0, 255, 255))

# Пример использования DarkConfirm
print("\nПримеры использования DarkConfirm:")

# Запрос подтверждения
if DarkConfirm(prompt="Вы хотите продолжить?", rgb_prompt=(255, 165, 0), rgb_yes=(0, 255, 0), rgb_no=(255, 0, 0)):
    DarkPrint("Продолжаем...", rgb_values=(0, 255, 0))
else:
    DarkPrint("Отмена.", rgb_values=(255, 0, 0))

# Пример использования DarkProgressBar
print("\nПримеры использования DarkProgressBar:")

# Прогресс-бар
total_iterations = 100
for i in range(total_iterations + 1):
    DarkProgressBar(i, total_iterations, rgb_bar=(0, 0, 255), rgb_empty=(100,100,100))
    time.sleep(0.05)

# Пример использования DarkSpinner
print("\nПримеры использования DarkSpinner:")

# Спиннер в отдельном потоке
def spinner_task():
    spinner = DarkSpinner(rgb_spinner=(255, 0, 255))
    for _ in range(20):  # Крутим спиннер 20 раз
        next(spinner)
        time.sleep(0.1)
    print("\r", end="")  # Очищаем строку после завершения спиннера

spinner_thread = threading.Thread(target=spinner_task)
spinner_thread.start()

DarkPrint("Выполняется какая-то задача...", rgb_values=(255, 100, 0))
time.sleep(2)  # Имитация выполнения задачи

spinner_thread.join()
DarkPrint("Задача завершена!", rgb_values=(0, 255, 0))
