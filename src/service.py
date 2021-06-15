#!/usr/bin/env python3
import requests
from flask import Flask, jsonify, request

from Telegram.Telegram import Telegram
from Util.Util import Util

app = Flask(__name__)


# @app.route('/MonitorContingencia/<topic>/<msg>', methods=['GET'])
# def monitor_contingencia(topic, msg):
#     parametros = dict()
#     try:
#         # BOT = "1710778365:AAFaexosrl1WMec2al5AQ_D45q00dxHHxHQ"
#         BOT = "1796457080:AAEl95krlisiqqta_QbGO5Ytn7d9cIeeEms"
#         parametros['chat_id'] = int(topic)
#         parametros['text'] = str(msg)
#
#         requests.post(f'https://api.telegram.org/bot{BOT}/sendMessage', data=parametros)
#     except:
#         parametros['error'] = 'No se pudo enviar el mensaje a telegram'
#     return jsonify(parametros)

util = None
telegram = None


@app.route('/')
def hola():
    return 'monitor contingencia FCV by Wisrovi'


@app.route('/MonitorContingencia', methods=['GET'])
def monitor_contingencia():
    respuesta = dict()
    if request.method == 'GET':
        id_client_telegram = request.values.get('id')
        msn = request.values.get('msn')

        message_ok = False
        msnBase64 = None
        try:
            msnBase64 = util.decoBase64UrlSafe(msn)
            message_ok = True
        except:
            respuesta["error"] ="message wasn't in base64"

        if message_ok:
            try:
                telegram.send(id_client_telegram, msnBase64)
                respuesta['chat'] = id_client_telegram
                respuesta['text'] = msn
            except:
                respuesta['error'] = "message not sent"
    else:
        respuesta['error'] = "Not method get"
    return jsonify(respuesta)


if __name__ == '__main__':
    from decouple import config

    TOKEN = config('TOKEN', default='')

    # app.run()
    app.run(debug=True, host='172.30.19.88', port=47474)

    util = Util()
    telegram = Telegram(TOKEN)
