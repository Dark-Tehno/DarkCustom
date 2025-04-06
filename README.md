# DarkCustom

DarkCustom - это библиотека Python, предоставляющая набор инструментов для работы с цветным вводом, выводом, подтверждением, индикатором прогресса и спиннером в консоли.

## Описание

Библиотека DarkCustom позволяет:

*   **DarkInput:** Запрашивать ввод с заданными цветами и проверкой типа данных (строка, целое число, число с плавающей точкой).
*   **DarkPrint:** Выводить текст с заданными цветами, разделителями и символами окончания строки.
*   **DarkConfirm:** Запрашивать подтверждение с цветным выводом вариантов "да" и "нет".
*   **DarkProgressBar:** Отображать цветной индикатор прогресса.
*   **DarkSpinner:** Отображать анимированный спиннер.
*   **DarkTable:** Отображает таблицу с заданными цветами.
*   **DarkLog:** Выводит лог с заданными цветами и возможностью записи в файл.


## Установка

```bash
pip install git+https://github.com/Dark-Tehno/DarkCustom.git
```

Или, если вы хотите установить из исходного кода:

```bash
git clone https://github.com/Dark-Tehno/DarkCustom.git
cd DarkCustom
pip install .
```

## Использование
```python
from DarkCustom import DarkInput, DarkPrint, DarkConfirm, DarkProgressBar, DarkSpinner
import time
import threading

# Пример использования DarkInput
name = DarkInput(prompt="Введите ваше имя: ", rgb_prompt=(0, 255, 0), rgb_input=(255, 255, 0))
DarkPrint(f"Привет, {name}!", rgb_values=(0, 255, 255))

# Пример использования DarkPrint
DarkPrint("Это строка с кастомным цветом!", rgb_values=(255, 0, 0))

# Пример использования DarkConfirm
if DarkConfirm(prompt="Вы хотите продолжить?", rgb_prompt=(255, 165, 0), rgb_yes=(0, 255, 0), rgb_no=(255, 0, 0)):
    DarkPrint("Продолжаем...", rgb_values=(0, 255, 0))
else:
    DarkPrint("Отмена.", rgb_values=(255, 0, 0))

# Пример использования DarkProgressBar
total_iterations = 100
for i in range(total_iterations + 1):
    DarkProgressBar(i, total_iterations, rgb_bar=(0, 0, 255), rgb_empty=(100,100,100))
    time.sleep(0.05)

# Пример использования DarkSpinner
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
```

### Запуск примеров:
```python
import DarkCustom.examples.examples
```

## Описание функций

### DarkInput
Запрашивает ввод с заданными цветами и проверкой типа данных.

* **prompt**: Текст запроса.
* **rgb_input**: Цвет текста ввода в формате RGB.
* **rgb_prompt**: Цвет текста запроса в формате RGB.
* **data_type**: Ожидаемый тип данных ('str', 'int', 'float').
* **min_value**: Минимальное допустимое значение (для числовых типов).
* **max_value**: Максимальное допустимое значение (для числовых типов).
* **type**: Тип ввода (text или password).

### DarkPrint
Выводит значения с заданными цветами.

* **values**: Значения для вывода.
* **sep**: Разделитель между значениями.
* **end**: Символ окончания строки.
* **rgb_values**: Цвет текста значений в формате RGB.
* **rgb_sep**: Цвет разделителя в формате RGB.
* **rgb_end**: Цвет символа окончания строки в формате RGB.

### DarkConfirm
Запрашивает подтверждение с заданными цветами.

* **prompt**: Текст запроса.
* **rgb_prompt**: Цвет текста запроса в формате RGB.
* **rgb_yes**: Цвет текста для варианта "да"
* **rgb_no**: Цвет текста для варианта "нет"

### DarkProgressBar
Отображает цветной индикатор прогресса.

current: Текущее значение прогресса.
total: Максимальное значение прогресса.
length: Длина индикатора в символах.
rgb_bar: Цвет заполненной части индикатора.
rgb_empty: Цвет пустой части индикатора.

* **current**: Текущее значение прогресса.
* **total**: Максимальное значение прогресса.
* **length**: Длина индикатора в символах.
* **rgb_bar**: Цвет заполненной части индикатора.
* **rgb_empty**: Цвет пустой части индикатора.

### DarkSpinner
Отображает анимированный спиннер.

* **rgb_spinner**: Цвет спиннера в формате RGB.
* **delay**: Задержка между сменой символов (в секундах).

### DarkTable
Отображает таблицу с заданными цветами.

* **data**: Данные для отображения в виде списка списков.
* **header_rgb**: Цвет заголовка в формате RGB.
* **row_rgb**: Цвет строк в формате RGB.
* **separator_rgb**: Цвет разделителей в формате RGB.

### DarkLog
Выводит лог с заданными цветами и возможностью записи в файл.

* **text**: Текст лога.
* **level**: Уровень лога (info, warning, error, debug).
* **rgb_values**: Цвет текста в формате RGB.
* **log_file**: Путь к файлу для записи логов (по умолчанию None - не записывать в файл).
    
---

**Dark.Tehno - Вперед к технологическому будущему!**
