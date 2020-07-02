from gothonweb.ork import Ork
class Kampf(object):

    def initKampf(self):    
        self.ork1 = Ork("feiger Ork")
        self.ork2 = Ork("fetter Ork")
        self.ork3 = Ork("hässl. Ork")
        self.ork4 = Ork("hunriger Ork")
        self.spieler = Ork("Spieler")
        self.curOrk = self.spieler
        self.zuEnde = False
        self.orklist = [self.ork1, self.ork2, self.ork3, self.ork4, self.spieler]

    def __init__(self):
        self.initKampf()

    def getCurrentOrk(self):
        return self.curOrk
    
    def rotateCurrentOrk(self):
        if self.curOrk is not self.spieler:
            index = self.orklist.index(self.curOrk)
            self.curOrk = self.orklist[index + 1]            
        else:
            self.curOrk = self.orklist[0]
        if self.curOrk.amleben is not True:
                self.rotateCurrentOrk()    
                
