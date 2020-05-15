import pyautogui
from flask import Flask, request, send_from_directory
import pickle

app = Flask(__name__, static_url_path='')

@app.route('/send-data')
def hello_world():
    #get screen size, to expand x y values
    screenWidth, screenHeight = pyautogui.size()
    #find ratio
    Xmultiplier = float(screenWidth/513)
    Ymultiplier = float(screenHeight/513)
    
    #convert to screen size
    x = float(float(request.args["leftX"])*Xmultiplier)
    y = float(float(request.args["leftY"])*Ymultiplier)

    rightY = float(float(request.args["rightY"])*Ymultiplier)

    lastLeftfile = open("lastLeft.txt", "r")

    # if movement is less that 20 pixels, don't move.
    #if float(request.args["leftX"]) - float(lastLeftfile.read()) > 5:
        #move mouse
    pyautogui.moveTo(x, y)

    #else:
        #print("Jiggle")
    if rightY > float(810):
        isClicked = open("isClicked.txt", "rb")
        if pickle.load(isClicked) != True:
            pyautogui.leftClick()
        isClicked.close()
    else:
        isClicked = open("isClicked.txt", "wb")
        pickle.dump(False, isClicked)
        isClicked.close()
    lastLeftfile.close()

    #save last left x location
    lastLeftfile = open("lastLeft.txt", "w")
    lastLeftfile.write(str(request.args["leftX"]))
    lastLeftfile.close()

    #########
    #REMEMBER TO RETURN!
    #########
    return("200 OK")

@app.route('/<path:path>')
def send_static(path):
    #make web code availible in browser
    return send_from_directory('static', path)