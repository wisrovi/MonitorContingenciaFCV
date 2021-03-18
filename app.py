#!/usr/bin/env python3
import requests
from flask import Flask

app = Flask(__name__)


@app.route('/MonitorContingencia/<topic>/<msg>')
def monitor_contingencia(topic, msg):
    BOT = "1710778365:AAFaexosrl1WMec2al5AQ_D45q00dxHHxHQ"
    parametros = {'chat_id': int(topic), 'text': str(msg)}
    requests.post(f'https://api.telegram.org/bot{BOT}/sendMessage', data=parametros)
    return msg + 'send to ' + topic


if __name__ == '__main__':
    app.run()
