import pyautogui
from flask import Flask, request, send_from_directory

app = Flask(__name__, static_url_path='')

@app.route('/send-data')
def hello_world():
    #get screen size, to expand x y values
    screenWidth, screenHeight = pyautogui.size()
    #find ratio
    Xmultiplier = float(480/screenWidth)
    Ymultiplier = float(640/screenHeight)
    
    #convert to screen size
    x = float(float(request.args["leftX"])*Xmultiplier)
    y = float(float(request.args["leftY"])*Ymultiplier)
    #move to calculated position
    pyautogui.moveTo(x, y)
    #########
    #REMEMBER TO RETURN!
    #########
    return(str(x)+" "+str(y))

@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('static', path)