import function
import view
from datetime import datetime


def notes():
    a = view.menu()
    if (a == '1'):
        id = view.id_input()
        name = view.name_input()
        description = view.description_input()
        current_datetime = str(datetime.now().strftime("%d.%m.%Y"))
        function.saving(id, name, description, current_datetime)

    elif (a == '2'):
        function.get_names()
    elif (a == '3'):
        print("Введите индекс заметки, которую хотите прочитать")
        id_found = int(input())
        function.get_description(id_found)
    elif (a == '4'):
        print("Введите индекс заметки, которую хотите редактировать")
        id_found = int(input())
        function.editing(id_found)
    elif (a == '5'):
        print("Введите индекс заметки, которую хотите удалить")
        id_found = int(input())
        function.deleting(id_found)
    elif (a == '6'):
        function.find()
