import os
import tkinter

appName = "StyxClient"

optionsDict = {}
optionsPath = os.getenv('APPDATA') + "\\.minecraft\\options.txt"

def loadOptions():
    with open(optionsPath) as optionsFile:
        optionsConfig = optionsFile.readlines()

    lineNum = 0
    for line in optionsConfig:
        optionsDict[line.split(":")[0]] = line.split(":")[1:][0].replace("\n","")
        lineNum += 1

    return optionsDict

def saveOptions():
    optionsWrite = ""
    lineNum = 0
    for key in optionsDict:
        optionsWrite += key + ":" + optionsDict.get(key) + "\n"
        lineNum += 1

    with open(optionsPath, "w") as optionsFile:
        optionsFile.write(optionsWrite)

def fullbright():
    optionsDict["gamma"] = "1000"
    return optionsDict

def fullbrightOff():
    optionsDict["gamma"] = "0.5"
    return optionsDict

def optimize():
    optionsDict["soundCategory_ambient"] = "0.0"
    optionsDict["soundCategory_music"] = "0.0"
    optionsDict["autoJump"] = "false"
    optionsDict["snooperEnabled"] = "false"
    return optionsDict

def optimizeOff():
    optionsDict["soundCategory_ambient"] = "1.0"
    optionsDict["soundCategory_music"] = "1.0"
    optionsDict["autoJump"] = "true"
    optionsDict["snooperEnabled"] = "true"
    return optionsDict

def fastgfx():
    optionsDict["graphicsMode"] = "0"
    optionsDict["maxFps"] = "60"
    optionsDict["entityShadows"] = "false"
    return optionsDict

def fastgfxOff():
    optionsDict["graphicsMode"] = "0"
    optionsDict["maxFps"] = "120"
    optionsDict["entityShadows"] = "true"
    return optionsDict

def togglesneak116():
    optionsDict["toggleCrouch"] = "true"
    return optionsDict

def togglesneak116Off():
    optionsDict["toggleCrouch"] = "false"
    return optionsDict

loadOptions()
saveOptions()

# GUI
win = tkinter.Tk()
win.title(appName)
win.config(bg="#151515")
win.geometry("300x300")

font = ("Yu Gothic Light", 20)

optionsTitle = tkinter.Label(win, text="Options", bg="#151515", font=("Yu Gothic Semibold", 25), fg="white")
optionsTitle.pack()

# Toggle Sneak Vanilla 1.16
togglesneak116Btn = tkinter.Button(win, text="[1.16+] ToggleSneak", bg="#151515", font=font, relief="flat", activebackground="#151515", activeforeground="#6E6E6E")
togglesneak116Btn.pack()
def istogglesneak116():
    if optionsDict["toggleCrouch"] == "true":
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

# FullBright
fullbrightBtn = tkinter.Button(win, text="FullBright", bg="#151515", font=font, relief="flat", activebackground="#151515", activeforeground="#6E6E6E")
fullbrightBtn.pack()
def isFullbright():
    if optionsDict["gamma"] == "1000":
        fullbrightBtn["fg"] = "green"
        return True
    else:
        fullbrightBtn["fg"] = "red"
        return False

fullbrightOn = isFullbright()

def fullBrightClick():
    fullbrightOn = isFullbright()
    if fullbrightOn:
        fullbrightOff()
    else:
        fullbright()
    saveOptions()
    fullbrightOn = isFullbright()

fullbrightBtn.config(command=fullBrightClick)

# FastGFX
fastgfxBtn = tkinter.Button(win, text="FastGFX", bg="#151515", font=font, relief="flat", activebackground="#151515", activeforeground="#6E6E6E")
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

# Optimize
optimizeBtn = tkinter.Button(win, text="Optimize", bg="#151515", font=font, relief="flat", activebackground="#151515", activeforeground="#6E6E6E")
optimizeBtn.pack()
def isOptimize():
    if optionsDict["soundCategory_ambient"] == "0.0" and optionsDict["soundCategory_music"] == "0.0" and optionsDict["autoJump"] == "false" and optionsDict["snooperEnabled"] == "false":
        optimizeBtn["fg"] = "green"
        return True
    else:
        optimizeBtn["fg"] = "red"
        return False

optimizeOn = isOptimize()

def optimizeClick():
    optimizeOn = isOptimize()
    if optimizeOn:
        optimizeOff()
    else:
        optimize()
    saveOptions()
    optimizeOn = isOptimize()

optimizeBtn.config(command=optimizeClick)



win.mainloop()