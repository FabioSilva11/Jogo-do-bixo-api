from flask import Flask, jsonify
import random
import json

app = Flask(__name__)

animais = {
    "Avestruz": {"numero": [0, 1, 2, 3], "imagem": "link_para_imagem1.jpg"},
    "Águia": {"numero": [4, 5, 6, 7], "imagem": "link_para_imagem2.jpg"},
    "Burro": {"numero": [8, 9, 10, 11], "imagem": "link_para_imagem3.jpg"},
    "Borboleta": {"numero": [12, 13, 14, 15], "imagem": "link_para_imagem4.jpg"},
    "Cachorro": {"numero": [16, 17, 18, 19], "imagem": "link_para_imagem5.jpg"},
    "Cabra": {"numero": [20, 21, 22, 23], "imagem": "link_para_imagem6.jpg"},
    "Carneiro": {"numero": [24, 25, 26, 27], "imagem": "link_para_imagem7.jpg"},
    "Camelo": {"numero": [28, 29, 30, 31], "imagem": "link_para_imagem8.jpg"},
    "Cobra": {"numero": [32, 33, 34, 35], "imagem": "link_para_imagem9.jpg"},
    "Coelho": {"numero": [36, 37, 38, 39], "imagem": "link_para_imagem10.jpg"},
    "Cavalo": {"numero": [40, 41, 42, 43], "imagem": "link_para_imagem11.jpg"},
    "Elefante": {"numero": [44, 45, 46, 47], "imagem": "link_para_imagem12.jpg"},
    "Galo": {"numero": [48, 49, 50, 51], "imagem": "link_para_imagem13.jpg"},
    "Gato": {"numero": [52, 53, 54, 55], "imagem": "link_para_imagem14.jpg"},
    "Jacaré": {"numero": [56, 57, 58, 59], "imagem": "link_para_imagem15.jpg"},
    "Leão": {"numero": [60, 61, 62, 63], "imagem": "link_para_imagem16.jpg"},
    "Macaco": {"numero": [64, 65, 66, 67], "imagem": "link_para_imagem17.jpg"},
    "Porco": {"numero": [68, 69, 70, 71], "imagem": "link_para_imagem18.jpg"},
    "Pavão": {"numero": [72, 73, 74, 75], "imagem": "link_para_imagem19.jpg"},
    "Peru": {"numero": [76, 77, 78, 79], "imagem": "link_para_imagem20.jpg"},
    "Touro": {"numero": [80, 81, 82, 83], "imagem": "link_para_imagem21.jpg"},
    "Tigre": {"numero": [84, 85, 86, 87], "imagem": "link_para_imagem22.jpg"},
    "Urso": {"numero": [88, 89, 90, 91], "imagem": "link_para_imagem23.jpg"},
    "Veado": {"numero": [92, 93, 94, 95], "imagem": "link_para_imagem24.jpg"},
}

@app.route('/sorteio')
def sorteio():
    animal_sorteado = random.choice(list(animais.keys()))
    numero_sorteado = random.choice(animais[animal_sorteado]["numero"])
    return jsonify({
        "numero_sorteado": numero_sorteado,
        "animal_sorteado": animal_sorteado,
        "imagem": animais[animal_sorteado]["imagem"]
    }), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/lista_animais')
def lista_animais():
    # Use json.dumps para garantir que os caracteres especiais sejam tratados corretamente
    return json.dumps(animais, ensure_ascii=False).encode('utf8'), 200, {'Content-Type': 'application/json; charset=utf-8'}

if __name__ == '__main__':
    app.run(debug=True)
