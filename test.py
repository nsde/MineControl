fastgfxBtn = tkinter.Button(win, text="fastgfx", bg="#151515", font=20, relief="flat", activebackground="#151515", activeforeground="#6E6E6E")
fastgfxBtn.pack()
def isfastgfx():
    if optionsDict["graphicsMode"] == "0" and optionsDict["maxFps"] == "60" and optionsDict["entityShadows"] == "false":
        fastgfxBtn["fg"] = "green"
        return True
    else:
        fastgfxBtn["fg"] = "red"
        return False

fastgfxOn = isfastgfx()

def fastgfxClick():
    fastgfxOn = isfastgfx()
    if fastgfxOn:
        fastgfxOff()
    else:
        fastgfx()
    saveOptions()
    fastgfxOn = isfastgfx()

fastgfxBtn.config(command=fastgfxClick)