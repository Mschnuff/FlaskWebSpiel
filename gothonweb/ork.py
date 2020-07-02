class Ork(object):

    def __init__(self, name):
        self.name = name
        self.hitpoints = 100
        self.hp_inverse = (100 - self.hitpoints)
        self.checked = False
        self.amleben = True
        #self.hp_inverse = (100 - self.hitpoints)

    def erleideSchaden(self, schaden):
        self.hitpoints = self.hitpoints - schaden
        self.hp_inverse = (100 - self.hitpoints)
        if self.hitpoints <= 0:
            self.amleben = False
            print(self.name + " stirbt.")   