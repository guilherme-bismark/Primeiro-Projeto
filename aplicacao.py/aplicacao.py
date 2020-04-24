from flask import Flask

app = Flask(__name__)


@app.route(‘/Documentos’)

def ola():

    return ‘< h1 > Olá Mundo!< /h1 >’


app.run()
