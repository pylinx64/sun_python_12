import pyautogui
from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep

# Создаем окно
root = Tk()

# Задаем заголовок окна
root.title('Хакер сало отдай!')

# Получаем ширину и высоту окна
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# Открываем окно на весь экран
root.attributes("-fullscreen", True)

label0 = Label(root, text="╚(•⌂•)╝ Locker by Xakep (╯°□°）╯︵ ┻━┻", font=1)
label0.grid(row=0, column=0) 


root.mainloop()
