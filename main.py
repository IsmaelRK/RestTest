from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/somar", methods=["POST"])
def somar():
    dados = request.json

    if "num" in dados and "num2" in dados:
        n = dados["num"]
        n2 = dados["num2"]

        res = n + n2

        return jsonify({"resultado": res})
    return "Erro Ocorrido", 400


if __name__ == "__main__":
    app.run()
