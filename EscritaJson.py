import json


def criar_perfil(identificacao, estressado, ansioso, neutro, feliz, triste):
    perfil = {"id": identificacao, "estressado": estressado, "ansioso": ansioso, "neutro": neutro, "feliz": feliz, "triste": triste}
    return perfil

id = []

novo_perfil = input('Deseja criar um perfil novo? ')
if novo_perfil == 'sim':
    ID = input('Qual a sua ID? ')
    novo_perfil = criar_perfil(ID, 0, 0, 0, 0, 0)
    id.append(novo_perfil)

data = {
    'ID' : {
        "Nome": ID,
        "Estressado": 0,
        "Ansioso" : 0,
        "Neutro": 0,
        "Feliz": 0,
        "Triste": 0,
    }
}


with open("data_file.json", "w") as write_file:
    json.dump(data, write_file, indent=4)