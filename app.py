from flask import Flask, render_template, session
import requests
import random

app = Flask(__name__)
app.secret_key = "pokemon"

# rotas serao inseridas aqui
@app.route('/')
def inicio():
    id_sorteado = random.randint(1,1025) 
    url_api = 'https://pokeapi.co/api/v2/pokemon-form/'+str(id_sorteado)
    response = requests.get(url_api)
    dados = response.json()
    print(dados.get("name"))
    
    sprites = dados.get("sprites",{})
    other = sprites.get("other",{})
    showdown = other.get("showdown",{})
    link_imagem = showdown.get("front_default")

    if 'numeros' not in session:
        #criando as listas vazias
        session['numeros'] = []
        session['nomes'] = []
        session['imagens'] = []

    numeros = session['numeros']
    numeros.append(id_sorteado)
    session['numeros'] = numeros

    nomes = session['nomes']
    nomes.append(dados.get("name"))
    session['nomes'] = nomes

    imagens = session['imagens']
    imagens.append(link_imagem)
    session['imagens'] = imagens
    

   
    return render_template('index.html', numeros=session['numeros'],nomes=session['nomes'], imagens=session['imagens'])

if __name__ == '__main__':
    app.run(debug=True)