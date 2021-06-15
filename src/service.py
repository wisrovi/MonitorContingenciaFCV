#!/usr/bin/env python3
import requests
from flask import Flask, jsonify, request

from Telegram.Telegram import Telegram
from Util.Util import Util

TOKEN = "1710778365:AAFaexosrl1WMec2al5AQ_D45q00dxHHxHQ"


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


@app.route('/help')
def help():
    return 'monitor contingencia FCV by Wisrovi'


@app.route('/MonitorContingencia', methods=['GET'])
def monitor_contingencia():
    respuesta = dict()
    if request.method == 'GET':
        id_client_telegram = request.values.get('id')
        msn = request.values.get('msn')

        message_ok = False
        msnBase64 = None

        if id_client_telegram is None:
            id_client_telegram = 66598084
        try:
            # msnBase64 = util.decoBase64UrlSafe(msn)
            
            msnBase64 = Util().decodeBase64(msn).decode('utf-8')
            print(msnBase64)
            message_ok = True
        except:
            print("ERROR")
            respuesta["error"] = "message wasn't in base64"

        if message_ok:
            try:
                print(id_client_telegram, msnBase64)

                # https://api.telegram.org/bot1710778365:AAFaexosrl1WMec2al5AQ_D45q00dxHHxHQ/sendMessage?chat_id=665928084&text=hola

                url = "https://api.telegram.org/bot" + TOKEN + "/sendMessage?chat_id=" + str(
                    id_client_telegram) + "&text=" + str(msnBase64)
                r = requests.get(url)

                # telegram.send(id_client_telegram, msnBase64)
                respuesta['chat'] = id_client_telegram
                respuesta['text'] = msn
            except:
                respuesta['error'] = "message not sent"
    else:
        respuesta['error'] = "Not method get"
    return jsonify(respuesta)


if __name__ == '__main__':
    # app.run()
    # app.run(debug=True, host='172.30.19.88', port=47474)
    app.run(debug=True, host='0.0.0.0', port=47475)

    util = Util()
    telegram = Telegram(TOKEN)
