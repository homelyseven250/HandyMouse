import pyautogui
from flask import Flask, request, send_from_directory

app = Flask(__name__, static_url_path='')

@app.route('/send-data')
def hello_world():
    #get screen size, to expand x y values
    screenWidth, screenHeight = pyautogui.size()
    #find ratio
    Xmultiplier = float(screenWidth/1280)
    Ymultiplier = float(screenHeight/720)
    
    #convert to screen size
    x = float(float(request.args["leftX"])*Xmultiplier)
    y = float(float(request.args["leftY"])*Ymultiplier)

    lastLeftfile = open("lastLeft.txt", "r")

    # if movement is less that 20 pixels, don't move.
    if x - int(lastLeftfile.read()) > 21:
        #move mouse
        pyautogui.moveTo(x, y)

    else:
        print("Jiggle")

    lastLeftfile.close()

    #save last left x location
    lastLeftfile = open("lastLeft.txt", "w")
    lastLeftfile.write(str(x))
    lastLeftfile.close()

    #########
    #REMEMBER TO RETURN!
    #########
    return("200 OK")

@app.route('/<path:path>')
def send_static(path):
    #make web code availible in browser
    return send_from_directory('static', path)