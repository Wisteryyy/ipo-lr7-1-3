import json
with open("dump.json", "r", encoding="utf-8") as file:
    s = json.load(file)

print("-----------------Меню-----------------")
print("-------1. Вывести все записи----------")
print("-------2. Вывести запись по полю----------")
print("-------3. Добавить запись----------")
print("-------4. Удалить запись по полю----------")
print("-------5. Выйти из программы----------")

a=int(input("Введите номер пункта: "))

C=0
if a <=0 or a>5 :
    print("Введите корректный номер.")

elif a == 1:
    print("Все записи:")
    for d in s:
        print(json.dumps(d))
        C += 1

elif a == 2:
    idd = int(input("Введите id записи для поиска: "))
    find = False
    for index, d in enumerate(s):
        if d["id"] == idd:
            print(json.dumps(d, indent=4))
            find = True
            break
    if not find:
        if d["id"] != idd:
            print("Запись не найдена.")

elif a==3:
    new = {
        "id": int(input("Введите id: ")),
        "name": input("Введите общее название рыбы: "),
        "latin_name": input("Введите латинское название рыбы: "),
        "is_salt_water_fish": str(input("Является ли рыба соленоводной (yes/no)? ")),
        "sub_type_count": int(input("Введите количество подвидов: "))
    }
    s.append(new)
    with open("dump.json", 'w', encoding='utf-8') as file:
        json.dump(s, file, indent=4)
    C += 1

elif a == 4:
    iddd=int(input("Введите id: "))
    find = False
    for index, d in enumerate(s):
        if d["id"] == iddd:
            del s[index]
            find = True
            break
    if not find:
        if d["id"] != iddd:
            print("Запись не найдена.")

elif a == 5:
    print("Количество выполненных операций с записями: {C}")