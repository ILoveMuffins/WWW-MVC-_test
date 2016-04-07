from flask import Flask
from flask import request
from flask import jsonify
from Queue import Queue
from logic.Kontroler import Kontroler
from logic.Zdarzenie import *

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/request_oblicz",  methods=['GET', 'POST'])
def request_oblicz():
    global eventQueue
    global mockupQueue
    eventQueue.put(ZdarzenieOblicz(request.json["username"], request.json["password"]))
    mockup = mockupQueue.get()
    dane = mockup.dane

# @TODO jeszcze nie smiga
@app.route("/request_koniec",  methods=['GET', 'POST'])
def request_koniec():
    global eventQueue
    global mockupQueue
    eventQueue.put(ZdarzenieKoniec())
    mockup = mockupQueue.get()
    return jsonify(**dane)


if __name__ == "__main__":
    app.debug = True
    eventQueue = Queue()
    mockupQueue = Queue(1)
    kontroler = Kontroler(eventQueue, mockupQueue)
    kontroler.start()
    app.run()
    kontroler.join()

