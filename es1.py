# modificare lesercizzio precedente in modo da inserire il sesso della persona che acetta il logi e in caso di acesso eseguito rispoddere con benvenuto  o benvenuta
#2 scrivere una web app che permetta di calcolare l'indice di massa corporea di una persona inserendo peso e altezza, l'applicazione dee rispndere con una pagina contenente i valori degli IMC, il respondo(sottopeso,normopeso,sovrappeso) e un immagine relativa alla dieta che deve eseguire
#3 scrivere una web app che permetta di slezionare da una lista di checkbox i propri hobby e cliccando su un bottone avere l'elenco degli obbi selezionati  e il numero di essi
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def tour():
  return render_template("es1/html1.html")

@app.route('/login', methods=['POST'])
def login():
  nome=request.form["nm"]
  pas=request.form["pas"]
  ses=request.form["sesso"]
  if ses=="maschio":
    ciao="benvenuto"
  elif ses=="femmina":
    ciao="benvenuta"
  else:
    ciao="grande bro"
  if nome.lower()=="admin" and pas=="xxx123#":
    return render_template("login.html",testo=ciao)
  else:
    return render_template("sbagliato.html")

 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)