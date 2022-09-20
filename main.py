from tkinter import *
from random import randint

#Создание окна
root = Tk()                   # В переменной root хранится сслыка на окно в памяти
root.resizable(False, False)  # Запрещаем изменение размеров окна
root.title("Угадай слово")    # Устанавливаем заголовок

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

# Метка для вывода слова, которое угадывается
wordLabel = Label(font=", 35")

# Метки для отображения текущих очков и рекорда
scoreLabel = Label(font=", 12")
topScoreLabel = Label(font=", 12")

# Метка оставшихся попыток
userTryLabel = Label(font=", 12")

# Установка меток в окне
scoreLabel.place(x=10, y=165)
topScoreLabel.place(x=10, y=190)
userTryLabel.place(x=10, y=215)

# Переменные для хранения значений
score = 0        # Текущие очки
topScore = 1000  # Рекорд игры
userTry = 10     # Количество попыток

st = ord("А")  # Для определения символа на кнопке по коду
btn = []       # Список кнопок

# Работаем с кнопками
for i in range(32):
    btn.append(Button(text=chr(st + i), width=2, font=", 12"))  # Создаем и добавляем список
    btn[i].place(x=215 + (i % 11) * 35, y=150 + i // 11 * 50)   # Устанавливаем на экране
    btn[i]["command"] = lambda x=i: pressLetter(x)

root.mainloop()