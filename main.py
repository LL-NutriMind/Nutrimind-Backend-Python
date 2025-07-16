# type: ignore # Importa as bibliotecas necessárias
from flask import Flask, request, jsonify
from flask_cors import CORS  # type: ignore # Permite requisições de outros domínios
# from waitress import serve  # type: ignore # Servidor WSGI para produção


app_Flask = Flask(__name__)  # Cria uma instância do Flask
# Permite caracteres especiais no JSON
app_Flask.config["JSON_AS_ASCII"] = False
CORS(app_Flask)  # Permite requisições de outros domínios


@app_Flask.route("/", methods=["GET"])  # Rota para a página inicial
def index():
    return jsonify({"message": "Bem-vindo à Primeira aplicação RAG"})


@app_Flask.route("/ask", methods=["POST"])  # Rota para receber perguntas
def ask():  # Recebe perguntas via POST
    data = request.get_json()
    question = data.get("question", "")
    answer = perguntar_ao_gpt(question)  # Chama a função para perguntar ao GPT
    return jsonify({"answer": answer})  # Retorna a resposta em JSON


# Criei a função para perguntar ao GPT (simulada aqui)
def perguntar_ao_gpt(question):
    # Aqui vamos integrar com a API do GPT
    return f"Resposta mocada para a pergunta: {question}"


if __name__ == "__main__":
    app_Flask.run(debug=True, port=5000)
