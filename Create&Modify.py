import json
d = {}

with open("data_file.json", "r+") as f:
    data = json.load(f)


y = input('Qual a sua ID? ')

if y in data:
    x = input('Como você está se sentindo? ')
    if x == 'Estressado':
        data[y]['Estressado'] += 1
    if x == 'Ansioso':
        data[y]['Ansioso'] += 1
    if x == 'Neutro':
        data[y]['Neutro'] += 1
    if x == 'Triste':
        data[y]['Triste'] += 1
    if x == 'Feliz':
        data[y]['Feliz'] += 1

else:
    data[y] = {
        "Estressado": 0,
        "Ansioso": 0,
        "Neutro": 0,
        "Feliz": 0,
        "Triste": 0,
    }
    if y in data:
        x = input('Como você está se sentindo? ')
        if x == 'Estressado':
            data[y]['Estressado'] += 1
        if x == 'Ansioso':
            data[y]['Ansioso'] += 1
        if x == 'Neutro':
            data[y]['Neutro'] += 1
        if x == 'Triste':
            data[y]['Triste'] += 1
        if x == 'Feliz':
            data[y]['Feliz'] += 1

    with open("data_file.json", "a") as jsonFile:
        json.dump(data, jsonFile, indent=4)



print(data[y])


with open("data_file.json", "w") as jsonFile:
    json.dump(data, jsonFile, indent=4)
