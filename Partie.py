import pendu


class Partie:
    def __init__(self):
        self.vie = 6
        self.mot = pendu.motAleatoire("fruits")
        self.motLabel = (len(self.mot) - 1) * ["-"]

    def getNbVie(self):
        return self.vie

    def getMot(self):
        return self.mot

    def viePerdue(self):
        self.vie -= 1

    def afficheMot(self):
        text = ""
        for x in range(len(self.motLabel)):
            text += self.motLabel[x]
        return text

    def testerLettre(self, lettreparam):
        if lettreparam in self.mot:
            index = 0
            for letter in self.mot:
                if letter == lettreparam:
                    self.motLabel[index] = lettreparam
                index += 1
        else:
            self.viePerdue()
