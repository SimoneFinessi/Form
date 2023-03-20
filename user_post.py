from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def tour():
  return render_template("controllo_post.html")

@app.route('/login', methods=['POST'])
def login():
  nome=request.form["nm"]
  pas=request.form["pas"]
  if nome.lower()=="admin" and pas=="xxx123#":
    return render_template("login.html",testo=nome, testo1=pas)
  else:
    return render_template("sbagliato.html")
 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)