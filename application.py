from flask import Flask, request, jsonify
from chatbot import ChatBot

app = Flask(__name__)
bot = ChatBot()

@app.route('/')
def home():
    return "Chatbot is up and running!"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    response = bot.get_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
