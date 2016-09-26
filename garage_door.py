import sys
import time

from flask import Flask
from flask import render_template

try:
    import RPi.GPIO as GPIO
except ImportError:
    from unittest.mock import MagicMock
    GPIO = MagicMock()


GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUTPUT)
GPIO.setup(14, GPIO.OUTPUT)
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/open", methods=['POST'])
def open():
    GPIO.output(15, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(15, GPIO.LOW)
    return '200'

@app.route("/close", methods=['POST'])
def open():
    GPIO.output(14, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(14, GPIO.LOW)
    return '200'

if __name__ == "__main__":
    try:
        app.run()
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()

