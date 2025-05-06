from flask import Flask, jsonify

app = Flask(__name__)

# Simulando uma base de opções
opcoes_por_id = {
    "1": ["Cenoura", "Batata", "Tomate"],
    "2": ["Azul", "Amarelo", "Verde"],
    "3": ["Sim", "Não", "Talvez"]
}

@app.route("/")
def home():
    return jsonify({"mensagem": "API está online!"})

@app.route("/opcoes/<id>", methods=["GET"])
def obter_opcoes(id):
    opcoes = opcoes_por_id.get(id)
    if opcoes:
        return jsonify({"id": id, "opcoes": opcoes})
    return jsonify({"erro": "ID não encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)
