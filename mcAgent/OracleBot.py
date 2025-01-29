import textwrap
import threading
from time import sleep
import mcpi.minecraft as minecraft
import random
from mcAgent.Quests import questions
import google.generativeai as genai
from unidecode import unidecode

genai.configure(api_key='') # Use your api key 
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

class OracleBot: # Hacerlo clase abstracta

    def __init__(self, mc = None):
        self.mc = mc or minecraft.Minecraft.create()
        self.oracle_thread = threading.Thread(target=self.oraclebot)
        self.oraclebotON = 0

    def start(self):
        if(self.oraclebotON == 0):
            #mc.postToChat(unidecode("<OracleBot> hola, bienvenido, ¿Que deseas consultar hoy? Usa MostrarPreguntas para ver las preguntas disponibles. Tambien puedes preguntar a Gemini Flash 1.5 mediante ia<pregunta>!"))
            self.oraclebotON = 1
            self.oracle_thread.start()
        return 0

    def stop(self):
        self.oraclebotON = 0
        self.oracle_thread.join()
        return 0

    def oraclebot(self):
        userActivated = 0
        while(self.oraclebotON):
            chat = self.mc.events.pollChatPosts()
            if(len(chat) != 0):
                print("Mensaje chat detectado!")
                request = chat[0].message
                request = request.lower()
                if request[:1] != "!":
                    if request == "oraclebot!" and userActivated == 0:
                        userActivated = 1
                        self.mc.postToChat(unidecode("<OracleBot> hola, bienvenido, ¿Que deseas consultar hoy? Usa MostrarPreguntas para ver las preguntas disponibles. Tambien puedes preguntar a Gemini Flash 1.5 mediante ia<pregunta>!"))
                        continue #Necesitamos saltar al siguiente ciclo, por que no se va a formular ninguna pregunta, solo encendemos el bot con esta peticion.
                    if userActivated == 1:   
                        if request == "mostrarpreguntas":
                            questions = self.viewquests()
                            i = 1
                            for q, a in questions:
                                self.mc.postToChat(f"<{i}> {unidecode(q)}")
                                i = i + 1
                        elif request[:2] == "ia":
                            answer = self.requestIA(request[2:])
                            cutedAnswer = textwrap.wrap(answer, width=250)
                            for cut in cutedAnswer:
                                self.mc.postToChat(cut)
                        elif request == "adios oraclebot!":
                            userActivated = 0
                            self.mc.postToChat(unidecode("<OracleBot> Hasta pronto ^_^"))
                        else:
                            self.mc.postToChat(self.chat(request))
            sleep(1)
        return 0

    def chat(self, question):
        question = question.lower()
        for q, answer in questions:
            if question == q.lower():
                return unidecode(answer)
        return unidecode("No entiendo esa pregunta. ¿Puedes reformularla?")
    
    def viewquests(self):
        return questions
    
    def requestIA(self, request):
        return unidecode(model.generate_content(request).text)
        

