togglesneak116Btn = tkinter.Button(win, text="togglesneak116", bg="#151515", font=20, relief="flat", activebackground="#151515", activeforeground="#6E6E6E")
togglesneak116Btn.pack()
def istogglesneak116():
    if optionsDict["graphicsMode"] == "0" and optionsDict["maxFps"] == "60" and optionsDict["entityShadows"] == "false":
        togglesneak116Btn["fg"] = "green"
        return True
    else:
        togglesneak116Btn["fg"] = "red"
        return False

togglesneak116On = istogglesneak116()

def togglesneak116Click():
    togglesneak116On = istogglesneak116()
    if togglesneak116On:
        togglesneak116Off()
    else:
        togglesneak116()
    saveOptions()
    togglesneak116On = istogglesneak116()

togglesneak116Btn.config(command=togglesneak116Click)