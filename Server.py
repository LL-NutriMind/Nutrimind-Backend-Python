from flask import Flask, request, jsonify  # type: ignore # Importa as bibliotecas necessárias
from flask_cors import CORS  # type: ignore # Permite requisições de outros domínios


app = Flask(__name__)  # Cria uma instância do Flask
app.config["JSON_AS_ASCII"] = False  # Permite caracteres especiais no JSON
CORS(app)  # Permite requisições de outros domínios


@app.route("/", methods=["GET"])  # Rota para a página inicial
def index():
    return jsonify({"message": "Bem-vindo à Primeira aplicação RAG"})


@app.route("/ask", methods=["POST"])  # Rota para receber perguntas
def ask():  # Recebe perguntas via POST
    if not request.is_json:  # Verifica se o conteúdo é JSON
        return jsonify({"error": "Requisição deve ser JSON"}), 400
    data = request.get_json()  # Obtém os dados JSON da requisição
    if "question" not in data:  # Verifica se a pergunta está presente
        return jsonify({"error": "Pergunta não encontrada"}), 400
    pergunta = data.get("question", "")  # Obtém a pergunta do JSON
    if not pergunta.strip():  # Verifica se a pergunta não está vazia
        return jsonify({"error": "Pergunta não pode ser vazia"}), 400
    resposta = f"Você perguntou: {pergunta}"  # Aqui entrará o GPT depois
    return jsonify({"answer": resposta})  # Retorna a resposta em JSON


if __name__ == "__main__":  # Executa o servidor Flask
    app.run(debug=True, port=5000)  # Ajusta a porta conforme necessário
