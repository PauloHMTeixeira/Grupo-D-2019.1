import json
d = {}

with open("data_file.json", "r") as f:
    data = json.load(f)

x = input('Como você está se sentindo? ')

if x == 'Triste':
    data['12']['Triste'] += 1

print(data['12']['Triste'])

