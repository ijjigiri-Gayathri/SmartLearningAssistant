from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get("question")

    if question.lower() == "what is ai?":
        answer = "Artificial Intelligence is smart computer technology."
    else:
        answer = "I am learning."

    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)