#1.Scrivere un programma per la conversione delle temperature, l'utente deve inserire un valore (float) e scegliere da una lista 
#di radio button quale conversione effettuare, una volta selezionata una scelta, clicca su un bottone e ottiene un risultato, 
#utilizzare le funzioni per effettuare la conversione.

#2. Modificare l'esercizio precedente per far scegliere la conversione da un menù a tendinafrom flask import Flask,render_template,request
from flask import Flask,render_template,request
app = Flask(__name__)

def tranf(a,b):
  if b=="F":
    ciao=""
  elif b=="cent":
    ciao=""
  elif b=="K":
    ciao=""
  elif b=="C":

@app.route('/', methods=['GET'])
def tour():
  return render_template("conv/html1.html")

@app.route('/login', methods=['POST'])
def login():
  gradi= request.form["GR"]
  cosa= request.form["fav_language"]
  risultato=tranf(gradi,cosa)
  return render_template("sbagliato.html")

 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)