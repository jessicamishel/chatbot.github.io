import flask
import re
import random
from flask import Flask, render_template, request, jsonify
app=Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('chat.html')

#@app.route('/',methods = ['GET','POST'])
#def result():
#   if request.method == 'POST':        
#       return 
    

#CHAT
@app.route('/send-message', methods=['POST'])
def send_message():
    user_message = request.json['message']
    # Aquí puedes procesar el mensaje del usuario y generar una respuesta del chatbot
    chatbot_response = "Hola, soy un chatbot. Gracias por tu mensaje: " + user_message
    return jsonify({'message': chatbot_response})

if __name__== '__main__':
    app.run(debug=True)