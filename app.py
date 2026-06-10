from flask import Flask, render_template, request
import numpy as np




app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        numeros = request.form.get("numeros", "")

        if numeros.strip() == "":
            return render_template("index.html", error="Debe ingresar numeros separados por comas.")

        try:
            lista = [float(n) for n in numeros.split(",")]
        except:
            return render_template("index.html", error="Solo se permiten numeros separados por comas.")

        suma = np.sum(lista)
        media = np.mean(lista)
        mediana = np.median(lista)
        desviacion = np.std(lista)

        return render_template(
            "index.html",
            lista=lista,
            suma=suma,
            media=media,
            mediana=mediana,
            desviacion=desviacion
        )

    return render_template("index.html")
if __name__ == "__main__":    
    app.run(debug=True)