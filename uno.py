from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def tour():
  return render_template("home1.html")

@app.route('/login', methods=['GET'])
def login():
  nome=request.args.get("nm")
  cognome=request.args.get("cm")

  
  return render_template("login.html",testo=nome, testo1=cognome)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)