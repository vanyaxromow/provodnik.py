import tkinter

window = tkinter.Tk()
window.title('Проводник')
window.geometry('350x350')
window.configure(bg='black')
window.resizable(False, False) # запрет изменения окна
text = tkinter.Label(window, text='Файл:', height=5, width=20, background="silver") # текст. поле с инф-ей, какой ф-л откр-т
text.grid(column=1, row=1) # делим окно, получаются колонны и ряды
button_select = tkinter.Button(window, width=20, height=3, text='Выбрать файл')
button_select.grid(column=1, row=2)
window.mainloop() # обновление окна