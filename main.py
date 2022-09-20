from tkinter import *
from random import randint

#Создание окна
root = Tk()                  # В переменной root хранится сслыка на окно в памяти
root.resizable(False, False) # Запрещаем изменение размеров окна
root.title("Угадай слово")   # Устанавливаем заголовок

# Настройка геометрии окна
WIDTH = 810
HEIGHT = 320
# Получение ширины и высоты экрана пользователя
SCR_WIDTH = root.winfo_screenwidth()
SCR_HEIGHT = root.winfo_screenheight()
# Вычисление точки расположения окна на экране
POS_X = SCR_WIDTH // 2 - WIDTH // 2
POS_Y = SCR_HEIGHT // 2 - HEIGHT // 2
# Установка нужных параметров окна
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

root.mainloop()