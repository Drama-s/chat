from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://dramas25.pythonanywhere.com"}})

messages = []  # Храним сообщения в памяти (не для продакшена)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data.get('message', '')
    if message:
        messages.append(message)  # Сохраняем сообщение
    return jsonify({"status": "ok"}), 200

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

if __name__ == '__main__':
    app.run(debug=True)

