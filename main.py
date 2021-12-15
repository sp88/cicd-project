from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'myloooongsecretkey12345'
socketio = SocketIO(app)


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
    socketio.emit('my response', json, callback=messageReceived)


if __name__ == '__main__':
    socketio.run(app, debug=True)
