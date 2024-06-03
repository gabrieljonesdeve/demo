from flask import Flask, request, jsonify

app = Flask(__name__)

message_feed = []

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        update = request.json
        message = update['message']
        text = message.get('text')
        chat_id = message['chat']['id']
        
        # Aggiungi il messaggio al feed
        message_feed.append({'text': text, 'chat_id': chat_id})
        
        # Restituisci una risposta vuota al bot di Telegram
        return jsonify({'success': True})

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/messages')
def get_messages():
    return jsonify(message_feed)

if __name__ == '__main__':
    app.run(port=5000)
