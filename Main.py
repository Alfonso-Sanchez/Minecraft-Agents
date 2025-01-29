import threading
import time
from mcpi import minecraft
from mcAgent.InsultBot import InsultBot
from mcAgent.OracleBot import OracleBot
from mcAgent.TntBot import TntBot
from unidecode import unidecode


class MainApp:
    def __init__(self):
        try:
            self.mc = minecraft.Minecraft.create()
        except Exception as e:
            print("Error al crear el objeto MCPI")
            print("¿Esta el servidor de Minecraft en ejecución?")
            print("¿Está el usuario en el servidor de Minecraft?")
            print(e)
            exit(1)

        self.insultbot = InsultBot()
        self.oraclebot = OracleBot()
        self.tntbot = TntBot()
        self.running = threading.Event()  # Controla el bucle infinito

    def start(self):
        self.running.set()
        print("Starting main loop...")
        self.run()

    def stop(self):
        self.running.clear()
        print("Stopping main loop...")

    def run(self):
        self.mc.postToChat(unidecode("OracleBot, InsultBot y TntBot listos para ser activados!"))
        self.mc.postToChat(unidecode("Para activar/desactivar OracleBot escribe !oraclebot on/off"))
        self.mc.postToChat(unidecode("Para activar/desactivar InsultBot escribe !insultbot on/off"))
        self.mc.postToChat(unidecode("Para activar/desactivar TntBot escribe !tntbot on/off"))

        while self.running.is_set():
            # Detectamos si hay algún mensaje nuevo en el chat
            chat = self.mc.events.pollChatPosts()
            if len(chat) != 0:
                print("Mensaje chat detectado!")
                request = chat[0].message.lower()
                print(request)
                # Filtramos por comando en el chat
                match request:
                    case "!oraclebot on":
                        self.oraclebot.start()
                        self.mc.postToChat(unidecode("Oraclebot Activado usa oraclebot! para hacerlo aparecer en el chat"))
                    case "!oraclebot off":
                        self.oraclebot.stop()
                        self.mc.postToChat(unidecode("Oraclebot Desactivado"))
                    case "!insultbot on":
                        self.insultbot.start()
                        self.mc.postToChat(unidecode("InsultBot Activado"))
                    case "!insultbot off":
                        self.insultbot.stop()
                        self.mc.postToChat(unidecode("InsultBot Desactivado"))
                    case "!tntbot on":
                        self.tntbot.start()
                        self.mc.postToChat(unidecode("TntBot Activado"))
                    case "!tntbot off":
                        self.tntbot.stop()
                        self.mc.postToChat(unidecode("TntBot Desactivado"))

            time.sleep(0.1)  # Evita un bucle excesivamente rápido


# Punto de entrada del programa
def main(): # pragma: no cover 
    app = MainApp()
    try:
        app.start()
    except KeyboardInterrupt:
        app.stop()
        print("Programa terminado.")

def mainTest(): # Punto de entrada para unittesting y dynimic testing
    app = MainApp()
    return app

if __name__ == "__main__": # pragma: no cover
    main()