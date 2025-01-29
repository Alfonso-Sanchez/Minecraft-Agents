import threading
from time import sleep

from unidecode import unidecode
from mcpi import minecraft
from mcpi import block

class TntBot:
    def __init__(self, mc = None):
        self.mc = mc or minecraft.Minecraft.create()
        self.tnt_thread = threading.Thread(target=self.tntbot)
        self.tntbotON = 0
    
    def start(self):
        if(self.tntbotON == 0):
            self.tntbotON = 1
            self.tnt_thread.start()
        return 0

    def stop(self):
        self.tntbotON = 0
        self.tnt_thread.join()
        return 0
    
    def tntbot(self):
        while(self.tntbotON):
            if(self.mc.getPlayerEntityIds() != []):
                pos = self.mc.player.getPos()
                actualBlock = self.mc.getBlock(pos.x, pos.y, pos.z)
                if(actualBlock == block.WATER_FLOWING.id or actualBlock == block.WATER_STATIONARY.id):
                    print("Ha caido en la trampa tnt :)")
                    tntPos = (pos.x-2, pos.y - 1, pos.z-2, pos.x+2, pos.y+4, pos.z+2)
                    exploding = (pos.x-1, pos.y - 1, pos.z-1, pos.x+1, pos.y+1, pos.z+1)
                    self.executeTNT(exploding, tntPos)
                sleep(1)
        return 0

    def executeTNT(self, exploding, tntPos):
        self.mc.setBlocks(tntPos, block.TNT)
        self.mc.setBlocks(exploding, block.FIRE)