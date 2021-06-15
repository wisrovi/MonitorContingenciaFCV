
class Telegram(object):
    import telebot

    def __init__(self, token):
        if len(token)>10:
            self.tb = self.telebot.TeleBot(token)
        else:
            print("token no valido:", token)
        self.echoBucle()

    def echoBucle(self):
        print("Iniciando EchoBucle.")
        self.tb.set_update_listener(self.listener)

    def send(self, Id_group, Mensaje):
        self.tb.send_message(Id_group, Mensaje)

    @staticmethod
    def listener(mensajes):
        print("Iniciando Listener.")
        for m in mensajes:
            chat_id = m.chat.id
            texto = m.text
            print('ID: ' + str(chat_id) + ' - MENSAJE: ' + texto)


if __name__ == '__main__':
    TOKEN = "1710778365:AAFaexosrl1WMec2al5AQ_D45q00dxHHxHQ"

    telegram = Telegram(TOKEN)
    telegram.send(665928084, "Hola mundo")
    telegram.send(622738755, "Hola mundo")
    telegram.send(-510828903, "Hola mundo")

    # https://xabaras.medium.com/sending-a-message-to-a-telegram-channel-the-easy-way-eb0a0b32968
    # https://api.telegram.org/bot1710778365:AAFaexosrl1WMec2al5AQ_D45q00dxHHxHQ/sendMessage?chat_id=665928084&text=hola

    print("mensaje enviado")

    import requests
    id_client_telegram = 665928084
    msnBase64 = "Holitas"
    TOKEN = "1710778365:AAFaexosrl1WMec2al5AQ_D45q00dxHHxHQ"
    url = "https://api.telegram.org/bot" + TOKEN + "/sendMessage?chat_id=" + str(
        id_client_telegram) + "&text=" + str(msnBase64)

    r = requests.get(url)
    print(r.text)
