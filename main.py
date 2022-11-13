import os
from tkinter import *
from pendu import listeCaract
from Partie import *


def clearFrame(nomFrame):
    for widgets in nomFrame.winfo_children():
        widgets.destroy()


class LePendu:
    def __init__(self):
        self.window = Tk()
        self.window.title("Le Pendu")
        self.window.geometry("1080x720")

        self.frame = Frame(self.window)
        self.frameDroite = Frame(self.frame)
        self.frameClavier = Frame(self.frameDroite)

        self.createTitle()

        self.frame.pack()
        self.frameDroite.grid(row=0, column=1)
        self.frameClavier.grid(row=0, column=0)

        self.initPartie()

    def createWidgets(self):
        self.creerImage(6)

        rowIndex = 0
        listeBoutons = []
        for index, letter in enumerate(listeCaract()):
            if index % 7 == 0 and index != 0:
                rowIndex += 1
            self.createButtonLetters(self.frameClavier, letter, rowIndex, index - rowIndex * 7)

        self.replayButton = self.createReplayBtton()

    def initPartie(self):
        self.partie = Partie()
        self.labelMot = self.createLabelMot()
        self.labelVies = self.createLabelVies()
        self.createWidgets()

    def creerImage(self, nbVies):
        absolutePath = os.path.dirname(__file__)
        relativePath = f"resources/images/pendu_{nbVies}.png"
        fullPath = os.path.join(absolutePath, relativePath)

        global image
        width = 417
        heigth = 550
        image = PhotoImage(file=fullPath)
        canvas = Canvas(self.frame, width=width, height=heigth, bd=0, highlightthickness=0)
        canvas.create_image(width / 2, heigth / 2, image=image)
        canvas.grid(row=0, column=0, padx=50)

    def createButtonLetters(self, place, lettre, rowIndex, index):
        return Button(place, text=lettre, command=lambda: self.updateGame(lettre)).grid(row=rowIndex, column=index)

    def createTitle(self):
        labelTitle = Label(self.window, text="Le pendu", font=("Lato", 40))
        labelTitle.pack()

    def createLabelVies(self):
        labelVies = Label(self.frameDroite, text=f"Vies restantes : {self.partie.getNbVie()}")
        labelVies.grid(row=2)
        return labelVies

    def createLabelMot(self):
        labelMot = Label(self.frameDroite, text=self.partie.afficheMot(), font=("Lato", 40), bg='#3297a8')
        labelMot.grid(row=1, pady=50)
        return labelMot

    def createReplayBtton(self):
        buttonReplay = Button(self.frameDroite, text='Rejouer', font=("Lato", 40), command=self.replayAction,
                              state=DISABLED)
        buttonReplay.grid(row=5, pady=50)
        return buttonReplay

    def replayAction(self):
        self.labelMot['text'] = ''
        self.initPartie()

    def testFinPartie(self):
        if self.partie.getNbVie() == 0:
            Label(self.frameDroite, text='PERDU', font=("Lato", 40)).grid(row=3)
            Label(self.frameDroite, text=f'Le mot était : {self.partie.getMot()}', font=("Lato", 20)).grid(row=4)
            clearFrame(self.frameClavier)
            self.replayButton['state'] = ACTIVE

        elif '-' not in self.partie.afficheMot():
            Label(self.frameDroite, text='BRAVO', font=("Lato", 40)).grid(row=3)
            clearFrame(self.frameClavier)
            self.replayButton['state'] = ACTIVE

    def updateGame(self, lettre):
        self.partie.testerLettre(lettre)
        self.labelMot['text'] = self.partie.afficheMot()
        self.labelVies['text'] = f"Vies restantes : {self.partie.getNbVie()}"
        self.creerImage(self.partie.getNbVie())
        self.testFinPartie()


appli = LePendu()
appli.window.mainloop()
