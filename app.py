from flask import Flask , render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)

socketio = SocketIO(app)

@app.route("/admin", methods = ['GET', 'POST'])
def admin():
    return render_template("index.html")

@app.route("/", methods = ['GET', 'POST'])
def index():
    return render_template("message.html")

@app.route("/room/<room_no>", methods = ['GET'])
def room(room_no):
    return render_template(f"room{room_no}.html")

@socketio.on('connect')
def connected():
    print('connect')

@socketio.on('message')
def message(json, methods=['GET']):
    #print(json)
    socketio.emit('message_response', json)

@socketio.on('room')
def room(json, methods=['GET']):
    print("dummy")
    print(json)
    room_num = json['room_name']
    print(room_num)
    if (room_num == '1'):
        socketio.emit('room', json)
    elif (room_num == '2'):
        socketio.emit('room2', json)
    else:
        print("error")



if __name__ == '__main__':
    socketio.run(app, debug=True)
