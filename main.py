import json # библиотека для работы с JSON файлами

with open("dump.json", "r", encoding="utf-8") as file: # открываем файл dump.json в режиме чтения с указанием кодировки UTF-8
    data = json.load(file)  # загружаем содержимое файла в переменную data

operation_count = 0 # переменная для количества операций
while True:
    print("-----------------Меню-----------------") # выводим главное меню с доступными опциями
    print("-------1. Вывести все записи----------")
    print("-------2. Вывести запись по ID----------")
    print("-------3. Добавить запись----------")
    print("-------4. Удалить запись по ID----------")
    print("-------5. Выйти из программы----------")

    while True:
        option = input("Введите номер пункта: ")  # запрашиваем у пользователя номер пункта меню
        try:
            search_option = int(option)
            if search_option < 1 or search_option > 5:
                print("Введите корректный номер от 1 до 5.")
                continue
        except ValueError:
            print("Введите число.")
            continue
        break

    if search_option == 1: # опция 1: вывести все записи
        print("Все записи:") # выводим
        for entry in data: # перебираем все записи
            print(f"Код: {entry['id']}")
            print(f"Имя рыбы: {entry['name']}")
            print(f"Латинское имя рыбы: {entry['latin_name']}")
            print(f"Является ли соленоводной: {entry['is_salt_water_fish']}")
            print(f"Количество подвидов: {entry['sub_type_count']}") # выводим каждую запись
            operation_count += 1 # увеличиваем счётчик операций

    elif search_option == 2: # опция 2: вывести запись по ID
        while True:
            str_search = input("Введите ID записи для поиска: ") # запрашиваем ID для поиска
            search_id = -1
            try:
                search_id = int(str_search)
            except ValueError:
                print("Введите число!")
                continue
            found = False # флаг для отслеживания, была ли найдена запись
            for entry in data: # перебираем все записи
                if entry["id"] == search_id: # если запись по id равна введенному id
                    print(f"Код: {entry['id']}")
                    print(f"Имя рыбы: {entry['name']}")
                    print(f"Латинское имя рыбы: {entry['latin_name']}")
                    print(f"Является ли соленоводной: {entry['is_salt_water_fish']}")
                    print(f"Количество подвидов: {entry['sub_type_count']}")
                    found = True # запись найдена
                    break # прерываем цикл
            if found:
                break # выходим из цикла, если запись найдена
            print("Запись не найдена. Попробуйте еще раз.") # выводим, если запись не найдена
        operation_count += 1 # увеличиваем счётчик операций

    elif search_option == 3: # опция 3: добавить запись
        while True:
            str_add = input("Введите ID: ") # вводим ID
            add_id = -1
            try:
                add_id = int(str_add)
            except ValueError:
                print("Введите число!")
                continue
            exist = False
            for entry in data: # проверяем, существует ли ID
                if entry["id"] == add_id:
                    print("Такое id уже существует. Попробуйте что-то другое.")
                    exist = True
                    break
            if not exist:
                break
        name_add = input("Введите общее название рыбы: ") # вводим название
        latin_name = input("Введите латинское название рыбы: ") # вводим латинское название
        is_salt_water_fish = input("Является ли рыба соленоводной? ") # вводим тип рыбы
        while True:
            sub_type_count1 = (input("Введите количество подвидов: ")) # вводим количество подвидов
            try:
                sub_type_count = int(sub_type_count1)
                if sub_type_count < 0:
                    print("Количество подвидов должно быть положительным числом.")
                    continue
                break
            except ValueError:
                    print("Введите корректное число.")


        new_record = { # создаём словарь для новой записи
            "id": add_id,
            "name": name_add,
            "latin_name": latin_name,
            "is_salt_water_fish": is_salt_water_fish,
            "sub_type_count": sub_type_count
        }
        data.append(new_record) # добавляем новую запись в список

        with open("dump.json", 'w', encoding='utf-8') as file: # открываем файл для записи
            json.dump(data, file) # записываем данные
        operation_count += 1 # увеличиваем счётчик операций


    elif search_option == 4: # опция 4: удалить запись по ID
        while True:
            str_delete = input("Введите ID для удаления: ") # запрашиваем ID для удаления
            delete_id = -1
            try:
                delete_id = int(str_delete)
            except ValueError:
                print("Введите число!")
                continue
            for index, entry in enumerate(data): # используем enumerate для получения индекса
                if entry["id"] == delete_id: # если запись найдена
                    del data[index] # удаляем запись
                    print("Запись удалена.")
                    break
            else:
                print("Запись не найдена. Попробуйте еще раз.")
                continue # запрашиваем ID снова
            break # выходим из цикла, если запись удалена
        operation_count += 1 # увеличиваем счётчик операций

    elif search_option == 5: # опция 5: выйти из программы
        print(f"Количество выполненных операций с записями: {operation_count}") # выводим
        break
