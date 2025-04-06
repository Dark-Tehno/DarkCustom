import getpass
import time
import itertools
import os
import datetime

def DarkInput(
    prompt: str = "",
    rgb_input: tuple = (255, 255, 255),
    rgb_prompt: tuple = (255, 255, 255),
    data_type: str = "str",
    min_value=None,
    max_value=None,
    type: str = "text"
    ) -> str:
    """
    Запрашивает ввод с заданными цветами и проверкой типа данных.

    Args:
        prompt: Текст запроса.
        rgb_input: Цвет текста ввода в формате RGB.
        rgb_prompt: Цвет текста запроса в формате RGB.
        data_type: Ожидаемый тип данных ('str', 'int', 'float').
        min_value: Минимальное допустимое значение (для числовых типов).
        max_value: Максимальное допустимое значение (для числовых типов).
        type: Тип ввода (text или password).
    Returns:
        Введенное значение.
    """

    color_input = ""
    color_prompt = ""

    if rgb_input != (255, 255, 255):
        color_input = f"\033[38;2;{rgb_input[0]};{rgb_input[1]};{rgb_input[2]}m"

    if rgb_prompt != (255, 255, 255):
        color_prompt = f"\033[38;2;{rgb_prompt[0]};{rgb_prompt[1]};{rgb_prompt[2]}m{prompt}"
    else:
        color_prompt = prompt

    if type == "text":
        if data_type == "int":
            while True:
                try:
                    text = int(input(f"{color_prompt}{color_input}"))
                    if min_value is not None and text < min_value:
                        DarkPrint(f"Значение должно быть не меньше {min_value}", rgb_values=(255, 0, 0))
                        continue
                    if max_value is not None and text > max_value:
                        DarkPrint(f"Значение должно быть не больше {max_value}", rgb_values=(255, 0, 0))
                        continue
                    break
                except ValueError:
                    DarkPrint("Неверный тип данных. Введите целое число.", rgb_values=(255, 0, 0))
        elif data_type == "float":
            while True:
                try:
                    text = float(input(f"{color_prompt}{color_input}"))
                    if min_value is not None and text < min_value:
                        DarkPrint(f"Значение должно быть не меньше {min_value}", rgb_values=(255, 0, 0))
                        continue
                    if max_value is not None and text > max_value:
                        DarkPrint(f"Значение должно быть не больше {max_value}", rgb_values=(255, 0, 0))
                        continue
                    break
                except ValueError:
                    DarkPrint("Неверный тип данных. Введите число.", rgb_values=(255, 0, 0))
        else:
            text = input(f"{color_prompt}{color_input}")
        print("\033[0m", end="")
        return text

    elif type == "password":
        password = getpass.getpass(f"{color_prompt}")
        print("\033[0m", end="")
        return password

def DarkPrint(
    *values: object,
    sep: str = " ",
    end: str = "\n",
    rgb_values: tuple = (255, 255, 255),
    rgb_sep: tuple = (255, 255, 255),
    rgb_end: tuple = (255, 255, 255)
    ) -> None:
    """
    Выводит значения с заданными цветами.

    Args:
        *values: Значения для вывода.
        sep: Разделитель между значениями.
        end: Символ окончания строки.
        rgb_values: Цвет текста значений в формате RGB.
        rgb_sep: Цвет разделителя в формате RGB.
        rgb_end: Цвет символа окончания строки в формате RGB.
    """
    color_values = ""
    color_sep = ""
    color_end = ""

    if rgb_values != (255, 255, 255):
        color_values = f"\033[38;2;{rgb_values[0]};{rgb_values[1]};{rgb_values[2]}m"
    if rgb_sep != (255, 255, 255):
        color_sep = f"\033[38;2;{rgb_sep[0]};{rgb_sep[1]};{rgb_sep[2]}m"
    if rgb_end != (255, 255, 255):
        color_end = f"\033[38;2;{rgb_end[0]};{rgb_end[1]};{rgb_end[2]}m"

    colored_values = []
    for i, value in enumerate(values):
        colored_values.append(f"{color_values}{value}")
        if i < len(values) - 1:
            colored_values.append(f"{color_sep}{sep}")

    print("".join(colored_values) + f"{color_end}{end}", end="")
    print("\033[0m", end="")

def DarkConfirm(
        prompt: str = "Вы уверены? (y/n)",
        rgb_prompt: tuple = (255, 255, 255),
        rgb_yes: tuple = (0,255,0),
        rgb_no: tuple = (255,0,0)
        ) -> bool:
    """
    Запрашивает подтверждение с заданными цветами.

    Args:
        prompt: Текст запроса.
        rgb_prompt: Цвет текста запроса в формате RGB.
        rgb_yes: Цвет текста для варианта "да"
        rgb_no: Цвет текста для варианта "нет"
    Returns:
        True, если подтвержден, иначе False.
    """
    while True:
        DarkPrint(prompt, rgb_values=rgb_prompt, end=" ")
        confim = DarkInput(rgb_input=rgb_yes, type="text").lower()
        if confim == "y" or confim == "yes":
            return True
        elif confim == "n" or confim == "no":
            return False
        else:
            DarkPrint("Неверный ввод. Введите 'y' или 'n'.", rgb_values=(255, 0, 0))

def DarkProgressBar(current, total, length=20, rgb_bar=(0, 255, 0), rgb_empty=(100,100,100)):
    """
    Отображает цветной индикатор прогресса.

    Args:
        current: Текущее значение прогресса.
        total: Максимальное значение прогресса.
        length: Длина индикатора в символах.
        rgb_bar: Цвет заполненной части индикатора.
        rgb_empty: Цвет пустой части индикатора.
    """
    color_bar = ""
    color_empty = ""

    if rgb_bar != (255, 255, 255):
        color_bar = f"\033[38;2;{rgb_bar[0]};{rgb_bar[1]};{rgb_bar[2]}m"
    if rgb_empty != (255, 255, 255):
        color_empty = f"\033[38;2;{rgb_empty[0]};{rgb_empty[1]};{rgb_empty[2]}m"

    percent = int(current / total * 100)
    filled_length = int(length * current // total)
    bar = f"{color_bar}{'█' * filled_length}{color_empty}{'-' * (length - filled_length)}"
    print(f"\r{bar} {percent}%", end="")
    if current == total:
        print("\033[0m", end="\n")

def DarkSpinner(rgb_spinner=(255, 255, 255), delay=0.1):
    """
    Отображает анимированный спиннер.

    Args:
        rgb_spinner: Цвет спиннера в формате RGB.
        delay: Задержка между сменой символов (в секундах).
    """
    color_spinner = ""
    if rgb_spinner != (255, 255, 255):
        color_spinner = f"\033[38;2;{rgb_spinner[0]};{rgb_spinner[1]};{rgb_spinner[2]}m"

    spinner_chars = itertools.cycle(["-", "\\", "|", "/"])
    while True:
        char = next(spinner_chars)
        print(f"\r{color_spinner}{char}", end="")
        time.sleep(delay)
        print("\033[0m", end="")
        yield

def DarkTable(data, header_rgb=(255, 100, 0), row_rgb=(200,200,200), separator_rgb=(150,150,150)):
    """
    Отображает таблицу с заданными цветами.

    Args:
        data: Данные для отображения в виде списка списков.
        header_rgb: Цвет заголовка в формате RGB.
        row_rgb: Цвет строк в формате RGB.
        separator_rgb: Цвет разделителей в формате RGB.
    """
    if not data:
        return

    color_header = ""
    color_row = ""
    color_separator = ""

    if header_rgb != (255, 255, 255):
        color_header = f"\033[38;2;{header_rgb[0]};{header_rgb[1]};{header_rgb[2]}m"
    if row_rgb != (255, 255, 255):
        color_row = f"\033[38;2;{row_rgb[0]};{row_rgb[1]};{row_rgb[2]}m"
    if separator_rgb != (255, 255, 255):
        color_separator = f"\033[38;2;{separator_rgb[0]};{separator_rgb[1]};{separator_rgb[2]}m"

    column_widths = [0] * len(data[0])
    for row in data:
        for i, cell in enumerate(row):
            column_widths[i] = max(column_widths[i], len(str(cell)))

    print(color_separator + "┌" + "┬".join(["─" * (width + 2) for width in column_widths]) + "┐")
    print(color_separator + "│", end="")
    for i, header in enumerate(data[0]):
        print(f" {color_header}{header:<{column_widths[i]}} {color_separator}│", end="")
    print()
    print(color_separator + "├" + "┼".join(["─" * (width + 2) for width in column_widths]) + "┤")

    for row_index, row in enumerate(data[1:]):
        print(color_separator + "│", end="")
        for i, cell in enumerate(row):
            print(f" {color_row}{str(cell):<{column_widths[i]}} {color_separator}│", end="")
        print()
        if row_index < len(data[1:]) - 1:
            print(color_separator + "├" + "┼".join(["─" * (width + 2) for width in column_widths]) + "┤")

    print(color_separator + "└" + "┴".join(["─" * (width + 2) for width in column_widths]) + "┘")
    print("\033[0m", end="")

def DarkLog(text, level="info", rgb_values=(0, 255, 0), log_file=None):
    """
    Выводит лог с заданными цветами и возможностью записи в файл.

    Args:
        text: Текст лога.
        level: Уровень лога (info, warning, error, debug).
        rgb_values: Цвет текста в формате RGB.
        log_file: Путь к файлу для записи логов (по умолчанию None - не записывать в файл).
    """
    color_values = ""
    if rgb_values != (255, 255, 255):
        color_values = f"\033[38;2;{rgb_values[0]};{rgb_values[1]};{rgb_values[2]}m"

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{current_time}] [{level.upper()}] {text}"

    if level == "info":
        print(f"{color_values}{log_message}\033[0m")
    elif level == "warning":
        print(f"{color_values}{log_message}\033[0m")
    elif level == "error":
        print(f"{color_values}{log_message}\033[0m")
    elif level == "debug":
        print(f"{color_values}{log_message}\033[0m")
    else:
        print(f"{color_values}{log_message}\033[0m")

    if log_file:
        try:
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(log_message + "\n")
        except Exception as e:
            print(f"Error writing to log file: {e}")
