from flask import Flask, render_template

app1 = Flask(__name__)

@app1.route("/")
def home():
    return "<p> Teste home</p>"

@app1.route("/segunda")
def pagina02():
    return "<h1>segunda página</h1>"

if __name__ == "__main__":
    app1.run(debug=True)