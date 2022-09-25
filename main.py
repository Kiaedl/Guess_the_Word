from tkinter import *
from tkinter import messagebox
from random import randint

# Метод при нажатии на клавишу
def pressKey(event):
    # print(f"Клавиша: {event.keycode}")

    # CTRL
    if (event.keycode == 17):
        wordLabel["text"] = wordComp

    # Получаем символ с клавиши
    ch = event.char.upper()
    if (len(ch) == 0):
        return 0

    # Определяем порядковый номер нажатого символа в русском алфавите
    codeBtn = ord(ch) - st
    if (codeBtn >= 0 and codeBtn <= 32):
        pressLetter(codeBtn)

# Обновляем информацию об очках и т.п.
def updateInfo():
    scoreLabel["text"] = f"Ваши очки: {score}"
    topScoreLabel["text"] = f"Лучший результат: {topScore}"
    userTryLabel["text"] = f"Осталось попыток: {userTry}"

# Сохраняет в файл очки пользователя
def saveTopScore():
    # Обязательно global, чтобы изменить topScore
    global topScore

    # Изменяем
    topScore = score

    # Открываем файл и записываем
    try:
        f = open("topchik.dat", "w", encoding="utf-8")
        f.write(str(topScore))
        f.close()
    # В случае ошибки создания и записи
    except:
        messagebox.showinfo("Ошибка", "Возникла проблема с файлом при сохранении очков")

#  Возвращает максимальное значение очков из файла
def getTopScore():
    try:
        f = open("topchik.dat", "r", encoding="utf-8")
        m = int(f.readline())
        f.close()
    except:
        m = 0
    return m

# Загружает слов в список
def getWordsFromFile():
    # Переменная-список для возвращаемого результата
    ret = []

    # Ставим блок проверки ошибок
    try:
        # Получаем дескриптор. Обратите внимание на кодировку, должна быть utf-8
        f = open("words.dat", "r", encoding="utf-8")

        # Читаем построчно
        for l in f.readlines():
            # Обязательно убираем последний символ переноса строки
            l = l.replace("\n", "")

            # Добавляем слово в список
            ret.append(l)
        # Не забываем закрывать файл!
        f.close()
    except:
        print("Проблема с файлом. Программа прекращает работу")
        quit(0)

    # Возвращаем список
    return ret

# Начало нового раунда
def startNewRound():
    global wordStar, wordComp, userTry

    # Загадываем слово
    wordComp = dictionary[randint(0, len(dictionary) - 1)]

    # Формируем слово из "*"
    wordStar = "*" * len(wordComp)

    # Устанавливаем текст в метку
    wordLabel["text"] = wordStar

    # Устанавливаем метку по центру для вывода слова
    wordLabel.place(x=WIDTH // 2 - wordLabel.winfo_reqwidth() // 2, y=50)

    # Сбрасываем кнопки
    for i in range(32):
        btn[i]["text"] = chr(st + i)
        btn[i]["state"] = "normal"

    # Сбрасываем попытки
    userTry = 10

    # Обновляем информацию в окне
    updateInfo()

# Сравниваем строки и считаем, сколько символов различаются
def compareWord(s1, s2):
    # Возвращаемый результат
    res = 0

    # Сравниваем s1 и s2 посимвольно
    for i in range(len(s1)):
        if (s1[i] != s2[i]):
            # Если символы разные, то увеличиваем res
            res += 1
    return res

# Возвращаем слово с открытыми символами
def getWordStar(ch):
    # Переменная для результата
    ret = ""

    for i in range(len(wordComp)):
        # Сравниваем символы
        if (wordComp[i] == ch):
            ret += ch
        else:
            ret += wordStar[i]
    return ret

# При нажатии мышкой на кнопку
def pressLetter(n):
    global wordStar, score, userTry

    # Проверяем, если эта буква уже была выбрана, то прерываем метод
    if (btn[n]["text"] == "."):
        return 0

    btn[n]["text"] = "."
    btn[n]["state"] = "disable"

    # Временная переменная
    oldWordStar = wordStar

    # Получаем строку с открытыми символами
    wordStar = getWordStar(chr(st + n))

    # Находим различие между старой и новой строкой
    count = compareWord(wordStar, oldWordStar)

    wordLabel["text"] = wordStar

    # Считаем очки
    if (count > 0):
        score += count * 5
    else:
        score -= 20

        # Проверяем, чтобы очки не свалились в отрицатиельные значения
        if (score < 0):
            score = 0

        # Уменьшаем количество попыток
        userTry -= 1

    # Обновляем информацию в окне
    updateInfo()

    # Сравниваем загаданное слово с содержимым wordStar
    if (wordComp == wordStar):
        # Добавляем 50% очков
        score += score // 2

        # Обновляем информацию, чтобы в окне обновилась текстовая метка с очками
        updateInfo()

        # Если человек заработал больше, чем рекордное количество очков, то сообщаем и записываем рекорд в файл
        if (score > topScore):
            messagebox.showinfo("Поздравляю!", f"Угадано слово {wordComp}!")
            # Метод, который записывает рекорд в файл
            saveTopScore()
        else:
            messagebox.showinfo("Отлично", f"Слово угадано: {wordComp}!")
        # Запускаем новй раунд, новое слово
        startNewRound()
    elif (userTry <= 0):
        messagebox.showinfo("Отведенное количество попыток закончено")
        quit(0)

#Создание окна
root = Tk()                   # В переменной root хранится сслыка на окно в памяти
root.resizable(False, False)  # Запрещаем изменение размеров окна
root.title("Угадай слово")    # Устанавливаем заголовок

# Устанавливаем обработчик клавиш
root.bind("<Key>", pressKey)

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
topScore = getTopScore()  # Рекорд игры
userTry = 10     # Количество попыток

st = ord("А")  # Для определения символа на кнопке по коду
btn = []       # Список кнопок

# Работаем с кнопками
for i in range(32):
    btn.append(Button(text=chr(st + i), width=2, font=", 12"))  # Создаем и добавляем список
    btn[i].place(x=215 + (i % 11) * 35, y=150 + i // 11 * 50)   # Устанавливаем на экране
    btn[i]["command"] = lambda x=i: pressLetter(x)

# Определяем глобально: "загаданное слово"
wordComp = ""
# Определяем глобально: "слвоо со звездочками"
wordStar = ""

# Словарь
dictionary = getWordsFromFile()

# Стартуем
startNewRound()

root.mainloop()