import tkinter as tk
from Jeu import Jeu as jeudebase
from JeuMinmax import Jeu as jeuminmax
from JoueurAI import JoueurAI
from OrdiAI import OrdiAI
from Afficher import Afficher
from JoueurAI import JoueurAI
from Test import Test
from Minmax import Minmax

# lancement du jeu fontionnant toujours avec le même patern


def lancement_jeu0():
    jeu0 = Test()
    ordiAI = OrdiAI()
    afficher = Afficher()
    jeu0.setOrdiAI(ordiAI)
    jeu0.setAfficher(afficher)

    jeu0.start()

# lancement du jeu minmax avec élagage


def lancement_jeu1():
    jeu1 = jeudebase()
    joueurAI = JoueurAI()
    ordiAI = OrdiAI()
    afficher = Afficher()
    jeu1.setAfficher(afficher)
    jeu1.setJoueurAI(joueurAI)
    jeu1.setOrdiAI(ordiAI)
    jeu1.start()

# lancement du jeu minmax sans élagage


def lancement_jeu2():
    jeu2 = jeuminmax()
    joueurAI = Minmax()
    ordiAI = OrdiAI()
    afficher = Afficher()
    jeu2.setAfficher(afficher)
    jeu2.setJoueurAI(joueurAI)
    jeu2.setOrdiAI(ordiAI)
    jeu2.start()


def main():

    # création de la fenêtre d'acceuil
    global win_start

    win_start = tk.Tk()
    win_start.title("2048")
    win_start.geometry('500x500+50+10')

    labrl = tk.Label(win_start, text='Choix du mode de jeu',
                     fg='#000', font='Arial 18 bold', height=5)
    labrl.pack()
    btn0 = tk.Button(win_start, text='Test patern', command=lancement_jeu0,
                     font='Arial 18 bold', bg='#000', fg='#FFF', width=100)
    btn0.pack()

    btn1 = tk.Button(win_start, text='MinMax avec élagage', command=lancement_jeu1,
                     font='Arial 18 bold', bg='#000', fg='#FFF', width=100)
    btn1.pack()

    btn2 = tk.Button(win_start, text=' MinMax', command=lancement_jeu2,
                     font='Arial 18 bold', bg='#000', fg='#FFF', width=100)
    btn2.pack()
    win_start.mainloop()


if __name__ == '__main__':
    main()
