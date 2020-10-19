import shutil
from tkinter import *
import os

shablons = {
    'Семейства': ['00_ID', '01_КП', '02_Договор', '03_ТЗ', '04_Рабочая', '05_Экспорт'],
    'Моделирование': ['00_ID', '01_КП']

}

# files = {
#     'Семейства': [['00_ID', 'test11.txt'], ['00_ID', 'test21.txt'],
#                   ['01_КП', 'test31.txt'], ['01_КП', 'test41.txt']
#                   ],
#     'Моделирование': [['00_ID', 'test12.txt'], ['00_ID', 'test22.txt'],
#                   ['01_КП', 'test32.txt'], ['01_КП', 'test42.txt']
#                   ],
#
#
#
# }

def copy(directory, new_directory):
    # нормализованный путь к файлам
    directory = os.path.abspath(directory)

    # файлы в папке
    object_in_folder = os.listdir(directory)

    # перебираем объекты и проверяем: файл или папка
    for object in object_in_folder:
        way = directory + '\\' + object

        # если путь ведет к файлу:
        if os.path.isfile(way) == True:
            file = object
            try:
                new_directory = path + '\\' + '\\'.join(way.split('\\')[-2:])
                shutil.copyfile(way, new_directory)
            except:
                pass

            # #есть ли файл в списке
            # for i in allNames:
            #     if i[1] == file:
            #         print(file)
            #         name_new = i[0]
            #         try:
            #             os.rename(directory + '\\' + file, directory + '\\' + name_new)
            #             break
            #         except FileExistsError:
            #             break
        #если путь ведет к папке
        else:
            copy(way, new_directory)





source_ways = r"\\dc\Bim\08_Общая\00_BIM_JUNIOR\03_Рабочая\Roma\createfolder"

print(os.listdir(source_ways))




root = Tk()
root.title("Графическая программа на Python")
root.geometry("350x300")


entry = Entry(width=20)                                     # текстовое поле ввода
create = Button(text="Создать", command=root.destroy)       # кнопка создать
variable = StringVar(root)                                  # выскакивающее меню
variable.set(list(shablons.keys())[0])                      # default value
cvar1 = BooleanVar()                                        # флажок
cvar1.set(0)
flag = Checkbutton(text="Копировать шаблоны", variable=cvar1, onvalue=1, offvalue=0)


w = OptionMenu(root, variable, *list(shablons.keys()))
print(w)

def entrydirectory(event):
    directory = entry.get()
    global path
    path = directory


    # return directory




create.bind('<Button-1>', entrydirectory)
# path = entryDirectory



print(cvar1.get())


# entry.place()

# w.place(relx=0.5, rely=0.5)
# flag.place(relx=0.5, rely=0.65) #anchor=W
# create.place(relx=0.7, rely=0.8)


Label(text='Путь:').grid(row=1, column=0, sticky=W, padx=10, pady=10)
Label(text='Тип работ:').grid(row=2, column=0, sticky=W, padx=10, pady=10)
entry.grid(row=1, column=1, sticky=W+E, padx=10, pady=10)
w.grid(row=2, column=1, padx=10, sticky=W+E, pady=10)        # выскакивающее меню
flag.grid(row=3, column=1, padx=10, pady=10) #anchor=W

create.grid(row=4, column=2, padx=10, pady=50)

# create.pack()
root.mainloop()



# print(list(files.keys()))







tag = variable.get()  # забираем из выпадающего меню тег
# path = r'C:\Users\r.enikeev\Desktop\Новая папка'



# tag = 'Моделирование'



try:
    for folder in shablons[tag]:
        directory_of_folder = path + '\\' + folder
        os.mkdir(directory_of_folder)
except OSError:
    print("Creation of the directory %s failed" % path)
else:
    print("Successfully created the directory %s " % path)


print(directory_of_folder)
print(cvar1.get())
if cvar1.get():
    copy(source_ways, path)


