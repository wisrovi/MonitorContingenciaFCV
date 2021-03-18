#!/usr/bin/env python3
import requests
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/MonitorContingencia/<topic>/<msg>', methods=['GET'])
def monitor_contingencia(topic, msg):
    parametros = dict()
    try:
        BOT = "1710778365:AAFaexosrl1WMec2al5AQ_D45q00dxHHxHQ"
        parametros['chat_id'] = int(topic)
        parametros['text'] = str(msg)

        requests.post(f'https://api.telegram.org/bot{BOT}/sendMessage', data=parametros)
    except:
        parametros['error'] = 'No se pudo enviar el mensaje a telegram'
    return jsonify(parametros)


if __name__ == '__main__':
    app.run()
