import tkinter
import os
from tkinter import filedialog # модуль, кот. позволяет вызвать диалог. окна

def file_select():
    filename = filedialog.askopenfilename(initialdir='/', title='Выберите файл',
                                      filetypes=(('Текстовый файл', '.txt'),
                                                 ('Все файлы', '*')))
    text['text'] = text['text'] + "" + filename
    os.startfile(filename)

window = tkinter.Tk()
window.title('Проводник')
window.geometry('450x150')
window.configure(bg='black')
window.resizable(False, False) # запрет изменения окна
text = tkinter.Label(window, text='Файл:', height=5, width=65, background="silver",
                     foreground='blue') # текст. поле с инф-ей, какой ф-л откр-т
text.grid(column=1, row=1) # делим окно, получаются колонны и ряды
button_select = tkinter.Button(window, width=20, height=3, text='Выбрать файл',
                               background='silver', foreground='blue',
                               command=file_select)
button_select.grid(column=1, row=2, pady=5)
window.mainloop() # обновление окна
# д/з: добавить меню к этому блокноту и чтобы был пункт info,
# где будет написано, как работать с блокнотом,
# и пункт about, в котором будет написано имя автора и версия