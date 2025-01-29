import threading
from time import sleep
import mcpi.minecraft as minecraft
import random
from unidecode import unidecode
from mcAgent.Insults import insults

class InsultBot: # Hacerlo clase abstracta

    def __init__(self, mc = None):
        self.mc = mc or minecraft.Minecraft.create()
        self.insult_thread = threading.Thread(target=self.insultbot)
        self.insultbotON = 0

    def start(self):
        if(self.insultbotON == 0):
            self.insultbotON = 1
            self.insult_thread.start()
        return 0

    def stop(self):
        self.insultbotON = 0
        self.insult_thread.join()
        return 0
    
    def insultbot(self):
        while(self.insultbotON):
            hit = self.mc.events.pollBlockHits()
            if(len(hit) != 0): # Si golpea bloque, insulta el botinsult.
                print("Hit espada detectado!")
                self.Insult()
            sleep(1)
        return 0

    def Insult(self):
       self.mc.postToChat(unidecode(insults[random.randint(0, len(insults)- 1)]))