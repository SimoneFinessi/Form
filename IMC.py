#2 scrivere una web app che permetta di calcolare l'indice di massa corporea di una persona inserendo peso e altezza, l'applicazione dee rispndere con una pagina contenente i valori degli IMC, il respondo(sottopeso,normopeso,sovrappeso) e un immagine relativa alla dieta che deve eseguire

from flask import Flask,render_template,request
app = Flask(__name__)
def IMC():
    alt=int(request.form["al"])/100
    peso=float(request.form["kg"])
    return peso/(alt**2)


@app.route('/', methods=['GET'])
def tour():
  return render_template("es2/html1.html")

@app.route('/login', methods=['POST'])
def login():
    imc=IMC()
    come=""
    if imc>25:
        come="sovrappeso"
        immage="../../static/img/sovra.jpg"
    elif imc<24.9 and imc>18.5 :
        come="normopeso"
        immage="../../static/img/normo.jpg"
    elif imc<18.5:
        come="sottopeso"
        immage="../../static/img/sotto.jpg" 
    return render_template("es2/login.html",IMC=imc,testo=come,immagine=immage)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
  