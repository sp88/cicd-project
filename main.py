from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO
from nlp_proj.convo_manager import Conversation
from nlp_proj.nlu import nlu

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'myloooongsecretkey12345'
socketio = SocketIO(app)

conversation = Conversation()


@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('templates', path)


@app.route('/')
def sessions():
    return render_template('chat.html')


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    nlu_response = nlu(json["message"])
    socketio.emit('my response', {'message': str(nlu_response)}, callback=messageReceived)


if __name__ == '__main__':
    socketio.run(app, debug=True)
