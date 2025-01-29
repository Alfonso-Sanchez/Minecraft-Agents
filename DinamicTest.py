from mcpi.minecraft import Minecraft
from mcAgent.InsultBot import InsultBot
from mcAgent.OracleBot import OracleBot
from mcAgent.TntBot import TntBot
from time import sleep
from Main import mainTest as main
import threading

def main_test():
    try:
        mc = Minecraft.create()
        try:
            # Crear la instancia del MainApp
            main_instance = main()
            main_thread = threading.Thread(target=main_instance.start, daemon=True)
            main_thread.start()
            sleep(2)  # Espera para que el MainApp se inicialice completamente
            
            insult_bot = main_instance.insultbot
            oracle_bot = main_instance.oraclebot
            tnt_bot = main_instance.tntbot
                
            def wait_for_specific_action(mc, expected_message, success_message):
                while True:
                    chat_events = mc.events.pollChatPosts()
                    if chat_events:
                        chat_message = chat_events[-1].message.lower()
                        if chat_message == expected_message:
                            mc.postToChat(success_message)
                            break
                    sleep(1)

            # Test de InsultBot
            mc.postToChat("Test: Activa InsultBot escribiendo '!insultbot on'.")
            wait_for_specific_action(mc, "!insultbot on", "InsultBot activado correctamente.")
            sleep(1)
            if insult_bot.insultbotON != 1:
                mc.postToChat("ERROR: InsultBot no se activo correctamente. InsultBot.on = 0")
                raise AssertionError("InsultBot no se activo correctamente. InsultBot.on = 0")
            if insult_bot.insult_thread.is_alive() != True:
                mc.postToChat("ERROR: InsultBot no se activo correctamente. insult_thread.is_alive = False")
                raise AssertionError("InsultBot no se activo correctamente. insult_thread.is_alive = False")

            mc.postToChat("Test: Golpea un bloque con una espada. Escribe 'ok' si el bot te insulto.")
            wait_for_specific_action(mc, "ok", "Bloque golpeado e insulto verificado. Procediendo...")

            mc.postToChat("Test: Desactiva InsultBot escribiendo '!insultbot off'.")
            wait_for_specific_action(mc, "!insultbot off", "InsultBot desactivado correctamente.")
            sleep(1)
            if insult_bot.insultbotON != 0:
                mc.postToChat("ERROR: InsultBot no se desactivo correctamente. InsultBot.on = 1")
                raise AssertionError("InsultBot no se desactivo correctamente. InsultBot.on = 1")
            if insult_bot.insult_thread.is_alive() != False:
                mc.postToChat("ERROR: InsultBot no se desactivo correctamente. insult_thread.is_alive = True")
                raise AssertionError("InsultBot no se desactivo correctamente. insult_thread.is_alive = True")
            mc.postToChat("Test: Golpea un bloque con una espada. Escribe 'ok' si el bot no te insulta.")
            wait_for_specific_action(mc, "ok", "Bloque golpeado y sin insulto verificado. Procediendo...")
            mc.postToChat("Test de InsultBot completado con exito.")


            mc.postToChat("Test: Activa OracleBot escribiendo '!oraclebot on'.")
            wait_for_specific_action(mc, "!oraclebot on", "OracleBot activado correctamente.")
            sleep(1)

            if oracle_bot.oraclebotON != 1:
                mc.postToChat("ERROR: OracleBot no se activo correctamente. OracleBot.on = 0")
                raise AssertionError("OracleBot no se activo correctamente. OracleBot.on = 0")
            if oracle_bot.oracle_thread.is_alive() != True:
                mc.postToChat("ERROR: OracleBot no se activo correctamente. oracle_thread.is_alive = False")
                raise AssertionError("OracleBot no se activo correctamente. oracle_thread.is_alive = False")
            
            
        # Test de OracleBot
            mc.postToChat("Test: Escribe oraclebot! para hacer aparecer al OracleBot en el chat.")
            mc.postToChat("Test: Prueba el OracleBot escribiendo 'mostrarpreguntas'.")
            mc.postToChat("Test: Escribe ia$quest para hacer una pregunta al OracleBot con Gemini 1.5 flash.")
            mc.postToChat("Test: Escribe 'ok' si el bot contesto todas las preguntas correctamente.")
            wait_for_specific_action(mc, "ok", "Preguntas respondidas correctamente. Procediendo...")

            mc.postToChat("Test: Desactiva OracleBot escribiendo 'Adios oraclebot!'.")
            mc.postToChat("Test: Intenta despues de desactivarlo enviar un mensaje al OracleBot.")
            mc.postToChat("Test: Si el OracleBot no responde, se desactivo correctamente.")
            mc.postToChat("Test: Escribe 'ok' si el bot no responde.")
            wait_for_specific_action(mc, "ok", "OracleBot desactivado correctamente.")

            mc.postToChat("Test: Desactiva OracleBot escribiendo '!oraclebot off'.")
            wait_for_specific_action(mc, "!oraclebot off", "OracleBot desactivado correctamente.")
            sleep(1)

            if oracle_bot.oraclebotON != 0:
                mc.postToChat("ERROR: OracleBot no se desactivo correctamente. OracleBot.on = 1")
                raise AssertionError("OracleBot no se desactivo correctamente. OracleBot.on = 1")
            if oracle_bot.oracle_thread.is_alive() != False:
                mc.postToChat("ERROR: OracleBot no se desactivo correctamente. oracle_thread.is_alive = True")
                raise AssertionError("OracleBot no se desactivo correctamente. oracle_thread.is_alive = True")

            mc.postToChat("Test de OracleBot completado con exito.")

        # Test de TntBot
            mc.postToChat("Test: Activa TntBot escribiendo '!tntbot on'.")
            wait_for_specific_action(mc, "!tntbot on", "TntBot activado correctamente.")

            sleep(1)
            if tnt_bot.tntbotON != 1:
                mc.postToChat("ERROR: TntBot no se activo correctamente. TntBot.on = 0")
                raise AssertionError("TntBot no se activo correctamente. TntBot.on = 0")
            if tnt_bot.tnt_thread.is_alive() != True:
                mc.postToChat("ERROR: TntBot no se activo correctamente. tnt_thread.is_alive = False")
                raise AssertionError("TntBot no se activo correctamente. tnt_thread.is_alive = False")

            mc.postToChat("Test: Salta al agua para activar la trampa de TNT.")
            mc.postToChat("Test: Escribe 'ok' si la trampa de TNT se activo.")
            wait_for_specific_action(mc, "ok", "Trampa de TNT activada correctamente. Procediendo...")

            mc.postToChat("Test: Desactiva TntBot escribiendo '!tntbot off'.")
            wait_for_specific_action(mc, "!tntbot off", "TntBot desactivado correctamente.")

            sleep(1)
            if tnt_bot.tntbotON != 0:
                mc.postToChat("ERROR: TntBot no se desactivo correctamente. TntBot.on = 1")
                raise AssertionError("TntBot no se desactivo correctamente. TntBot.on = 1")
            if tnt_bot.tnt_thread.is_alive() != False:
                mc.postToChat("ERROR: TntBot no se desactivo correctamente. tnt_thread.is_alive = True")
                raise AssertionError("TntBot no se desactivo correctamente. tnt_thread.is_alive = True")

            mc.postToChat("Test: Salta al agua para comprobar si la trampa de TNT sigue activa.")
            mc.postToChat("Test: Escribe 'ok' si la trampa de TNT no se activo.")
            wait_for_specific_action(mc, "ok", "Trampa de TNT no activada. Procediendo...")
            mc.postToChat("Test de TntBot completado con exito.")
            mc.postToChat("Todos los tests han sido completados con exito.")

            # Detener el MainApp
            main_instance.stop()
            main_thread.join()
            print("Programa principal detenido.")
            print("Tests completados con exito.")
        except Exception as e:
            print("Error al ejecutar los tests dinamicos. Revisa el chat de Minecraft y la salida de esta consola.")
            print(e)
    except Exception as e:
        if e == KeyboardInterrupt:
            print("Programa terminado mediante teclado.")
        else:
            print("Error al ejecutar el programa principal. Verificaciones: ")
            print("1. Verifica que el servidor de Minecraft este activo.")
            print("2. Verifica que el servidor al menos tenga 1 jugador.")
            print(e)
        
    

if __name__ == "__main__":
    main_test()