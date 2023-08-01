from flask import Flask, render_template
import RNA
#from app_rna import app
app = Flask(__name__)

@app.route("/main")
def principal():
    return render_template('main.html')
    RNA.ConstModel()
if __name__ == "__main__":
    app.run(debug=True)