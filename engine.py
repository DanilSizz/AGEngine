import time
from anim import *

class Engine:

    def __init__(self, renderer: Anim, fps):

        self.renderer = renderer
        #Интервал обновления экрана
        self.interval = 1 / fps
        #Таймер (объект класса Time)
        self.time = time.time()
        self.object = []

    def startGame(self):
        self.gameCycle()

    def addObject(self, object):
        self.object.append(object)

    def gameCycle(self):

        i = 0
        while True:

            self.renderer.update_animations()
      
            elapsed_time = time.time() - self.time
  
            if elapsed_time < self.interval:
                time.sleep(self.interval - elapsed_time)

            i = i + 1
            #print(i)


    