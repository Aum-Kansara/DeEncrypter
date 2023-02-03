from flask import Flask,request
from dotenv import load_dotenv
import os

app = Flask(__name__)

# 49      --> ((((49- 3)+22+46865)-33554)+586857) --> 
# 600236  --> ((((600236+3)-22-46865)+33554)-586857)
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
    # count=587356
    for i in range(len(msg)):
        msg = msg[:i] + chr(ord(msg[i])+2) + msg[i+1:]
    return msg

def decode(msg):
    for i in range(len(msg)):
        # msg[i]=ord(msg[i])<<2
        msg = msg[:i] + chr(ord(msg[i])-2) + msg[i+1:]
    return msg

@app.route('/')
def index():
    return '<h1>Welcome to <b>DeEecrypter</b></h1><hr><h2>To Encode Text Use URL: 127.0.0.1:5000/encode?msg=msg_to_be_encoded</h2><hr><h2>To Decode Text Use URL: 127.0.0.1:5000/decode?msg=encoded_msg</h2><hr>'

@app.route('/encode')
def encodedMsg():
    return encode(request.args.get('msg'))

@app.route('/decode')
def decodedMsg():
    return decode(request.args.get('msg'))


app.run()