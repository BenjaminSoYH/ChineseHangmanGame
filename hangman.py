import tkinter as tk

stages = 0

mf = "   _____ \n"
ms = "   |      |\n"
mh = "   O     |\n"
mt1 = " /|     |\n"
mt2 = "  /|\    |\n"
mn = "          |\n"
ml1 = "  /      |"
ml2 = "  / \    |"
ss = mf + ms + mh
sg0 = mf + ms + mn * 4
sg1 = ss + mn * 3
sg2 = ss + ms * 2 + mn
sg3 = ss + mt1 + ms + mn
sg4 = ss + mt2 + ms + mn
sg5 = ss + mt2 + ms + ml1
sg6 = ss + mt2 + ms + ml2


def Next():
    global stages
    stages += 1
    labelz.configure(text=globals()["sg" + str(stages)])
    if stages > 6:
        stages = 0


labelz = tk.Label(text=sg0)
labelz.pack()
