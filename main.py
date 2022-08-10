from flask import Flask, render_template, request

from flask_socketio import SocketIO,send,emit

app = Flask(__name__)

app.config['SECRET_KEY']= 'socketapp'
app.config['DEBUG']=True

socketio = SocketIO(app,cors_allowed_origins="*")


messages =['welcome to msger app']

users={}

@socketio.on('message')
def handleMessage(msg):
    print ('msg : '+msg+"  sid : " + users[request.sid])
    #messages.append(msg)
    emit('message',{'msg' :msg, 'sender': users[request.sid]},broadcast=True)

@socketio.on('newUser')
def handle_new_user(username = 'unknown'):
    print(username)
    users[request.sid] = username

@app.route('/')
def index():
    return render_template('index.html',messages = messages)


if __name__ =="__main__":
    socketio.run(app)