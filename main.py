from flask import Flask, request, jsonify  # Flask app to handle GPT queries
from gpt_engine import ask_gpt  # Function to interact with OpenAI's GPT model

app = Flask(__name__)  # Initialize Flask app


@app.route("/ask", methods=["POST"])  # Define route for asking questions
def ask():  # Handle POST requests to /ask
    data = request.get_json()  # Get JSON data from the request
    # Extract the 'question' field from the JSON data
    question = data.get("question")

    if not question:  # Check if 'question' is provided
        # Return error if 'question' is missing
        return jsonify({"error": "The 'question' field is required."}), 400

    try:  # Call the GPT engine to get an answer
        answer = ask_gpt(question)  # Get the answer from GPT
        return jsonify({"answer": answer})  # Return the answer in JSON format
    except Exception as e:  # Handle any exceptions that occur
        # Return error if an exception occurs
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":  # Run the Flask app
    app.run(port=5000, host="localhost", debug=True)
