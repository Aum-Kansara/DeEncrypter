from flask import Flask,request,redirect
from dotenv import load_dotenv
import os

app = Flask(__name__)


load_dotenv()
KEY_X=os.getenv('KEY_X')
KEY_Y=os.getenv('KEY_Y')
KEY_Z=os.getenv('KEY_Z')
KEY_A=os.getenv('KEY_A')
KEY_B=os.getenv('KEY_B')
def equateEncoding(num):
    return ((((num- KEY_X)+KEY_Y+KEY_Z)-KEY_A)+KEY_B)

def equatedecoding(num):
    return ((((num+KEY_X)-KEY_Y-KEY_Z)+KEY_A)-KEY_B)

def encode(msg):
    for i in range(len(msg)):
        msg = msg[:i] + chr(ord(msg[i])+2) + msg[i+1:]
    return msg

def decode(msg):
    for i in range(len(msg)):
        msg = msg[:i] + chr(ord(msg[i])-2) + msg[i+1:]
    return msg

@app.route('/', defaults={'path': ''})
@app.route('/')
def index():
    return '<h1>Welcome to <b>DeEncrypter</b></h1><hr><h2>To Encode Text Use URL: <a href="https://deencrypter.onrender.com/encode?msg=Hello Word">https://deencrypter.onrender.com/encode?msg=Hello Word</a></h2><hr><h2>To Decode Text Use URL:<a href="https://deencrypter.onrender.com/decode?msg=Jgnnq&quot;Yqtf">https://deencrypter.onrender.com/decode?msg=Jgnnq"Yqtf</a></h2><hr>'

@app.route('/encode')
def encodedMsg():
    if request.args.get('msg')==None:
        return redirect('/')
    return encode(request.args.get('msg'))

@app.route('/decode')
def decodedMsg():
    if request.args.get('msg')==None:
        return redirect('/')
    return decode(request.args.get('msg'))



app.run()