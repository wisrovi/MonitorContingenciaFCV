
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
    from decouple import config
    TOKEN = config('TOKEN', default='')

    telegram = Telegram(TOKEN)
    telegram.send(665928084, "Hola mundo")
