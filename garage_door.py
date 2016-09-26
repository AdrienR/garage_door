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
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
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
def close():
    GPIO.output(18, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(18, GPIO.LOW)
    return '200'

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=80)
    except (KeyboardInterrupt, Exception) as e:
        print(e)
    finally:
        print("exiting")
        GPIO.cleanup()
        sys.exit()

