
from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "É Nois na Fita!!! E vamos lá"

if __name__ == '__main__':
    app.run(debug=True)
