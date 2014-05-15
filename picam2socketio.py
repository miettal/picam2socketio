#!/usr/bin/env python
#
# picam2socketio.py
#
# Author:   Hiromasa Ihara (miettal)
# URL:      http://miettal.com
# License:  MIT License
# Created:  2014-05-15
#
import threading
import picamera
from flask import Flask, render_template, request, Response
from flask.ext.socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

def camera_thread() :
  with picamera.PiCamera() as camera :
    camera.resolution = (480, 270)
    camera.framerate = 5
    time.sleep(2)
    camera.stream = io.BytesIO()
    for foo in camera.capture_continuous(camera.stream, "jpeg", use_video_port=True):
      camera.stream.seek(0)
      socketio.emit('jpeg', base64.b64encode(camera.stream.read()))
      camera.stream.seek(0)
      camera.stream.truncate()

@app.route('/')
def index() :
  return render_template("index.html")

if __name__ == "__main__" :
  t=threading.Thread(target=camera_thread)
  t.setDaemon(True)
  t.start()

  socketio.run(app, host="0.0.0.0")
