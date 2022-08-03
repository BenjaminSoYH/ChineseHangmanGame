import random
import tkinter as tk

opem = open("Chinesechar.txt", encoding="utf8")
read = open.read()
list = []
for i in read:
    if i != '\n':
        list.append(i)

ran = random.randrange(0, 14127)
answer = list[ran]
print(answer)

text = "Guess the 中文字!!!"
chances = 6

running = True
while running:
    def check():
        global text
        global chances
        xe = x.get()
        if xe == answer:
            text = "you win"
        else:
            hm.Next()
            chances -= 1
            if chances == 0:
                over = True
                text = "you Lose, you word was: " + answer
                running = False
            else:
                text = ("你有 " + str(chances) + " chances left")

        label.configure(text=text)


    x = tk.Entry()
    xe = x.get()

    label = tk.Label(text=text, font=25)
    button = tk.Button(text="done", command=check)
    label.pack()
    x.pack()
    button.pack()
    import hangman as hm

    window = tk.Tk()
    window.withdraw()
    window.geometry("800x800")
    window.resizable(False, False)
    window.mainloop()
