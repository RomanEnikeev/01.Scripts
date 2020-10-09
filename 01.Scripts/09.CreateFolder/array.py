import os

shablons = {
    'Семейства': ['00_ID', '01_КП', '02_Договор', '03_ТЗ', '04_Рабочая', '05_Экспорт'],
    'Моделирование': ['00_ID', '01_КП']

}

files = {
    'Семейства': [['00_ID', 'test11.txt'], ['00_ID', 'test21.txt'],
                  ['01_КП', 'test31.txt'], ['01_КП', 'test41.txt']
                  ],
    'Моделирование': [['00_ID', 'test12.txt'], ['00_ID', 'test22.txt'],
                  ['01_КП', 'test32.txt'], ['01_КП', 'test42.txt']
                  ],



}
# print(path)


from tkinter import *

root = Tk()
root.title("Графическая программа на Python")
root.geometry("400x300")

entry = Entry(width=20)
create = Button(text="Создать", command=root.destroy)


variable = StringVar(root)
variable.set(list(files.keys())[0]) # default value
w = OptionMenu(root, variable, *list(files.keys()))


def entrydirectory(event):
    directory = entry.get()
    global path
    path = directory


    # return directory


create.bind('<Button-1>', entrydirectory)
# path = entryDirectory


entry.pack()
create.pack()
w.pack()

root.mainloop()


# print(list(files.keys()))








# path = r'C:\Users\r.enikeev\Desktop\Новая папка'



tag = 'Моделирование'



try:
    for folder in shablons[tag]:
        directory_of_folder = path + '\\' + folder
        os.mkdir(directory_of_folder)



except OSError:
    print("Creation of the directory %s failed" % path)
else:
    print("Successfully created the directory %s " % path)
