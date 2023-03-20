#2 scrivere una web app che permetta di calcolare l'indice di massa corporea di una persona inserendo peso e altezza, l'applicazione dee rispndere con una pagina contenente i valori degli IMC, il respondo(sottopeso,normopeso,sovrappeso) e un immagine relativa alla dieta che deve eseguire

from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def tour():
  return render_template("es2/html1.html")

@app.route('/login', methods=['POST'])
def login():
    alt=float(request.form["al"])
    peso=float(request.form["kg"])
    imc=peso/(alt*2)
    come=""
    if imc>25:
        come="sovrappeso"
    elif imc<24.9 and imc>18.5 :
        come="normopeso"
    elif imc<18.5:
        come="sottopeso"

    return render_template("es2/login.html",IMC=imc,testo=come)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
  