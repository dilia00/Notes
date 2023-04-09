import json
import os.path
import view


def saving(id: int, name: str, description: str, datetime: str):
    if (os.path.isfile('data.json')):
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)
    else:
        data = {}
        data['note'] = []

    data['note'].append({
        'id': id,
        'name': name,
        'description': description,
        'datetime': str(datetime)
    })
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)


def get_names():
    if (os.path.isfile('data.json')):
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)
            for item in data['note']:
                print(item['id'], item['name'], item['datetime'])
    else:
        print("База данных пуста")
        return


def editing(id: int):
    if (os.path.isfile('data.json')):
        with open('data.json') as json_file:
            data = json.load(json_file)
            view.select_field()
            field = str(input())
            print("Введите значение, на которое хотите заменить выбранное вами поле: ")
            for item in data['note']:
                if item['id'] == id:
                    if (field == "1"):
                        item['id'] = int(input())
                    elif (field == "2"):
                        item['name'] = input()
                    elif (field == "3"):
                        item['description'] = input()
                    break
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file)
    else:
        print("База данных пуста")
        return


def deleting(id: int):
    if (os.path.isfile('data.json')):
        with open('data.json') as json_file:
            data = json.load(json_file)
            data['note'].pop(id-1)
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file)


def get_description(id: int):
    if (os.path.isfile('data.json')):
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)
            for item in data['note']:
                if item['id'] == id:
                    print(item['description'])
                    return
    else:
        print("База данных пуста")
        return


def find():
    target = input(
        "Введите дату заметки в формате 00.00.2023 (число.месяц.год): ")
    count = 0
    if (os.path.isfile('data.json')):
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)

            for item in data['note']:
                if (item['datetime'] == target):
                    print(item['id'], item['name'], item['datetime'])
                    count += 1
            if (count == 0):
                print("Заметок с такой датой не обнаружено")
    else:
        print("База данных пуста")
        return
