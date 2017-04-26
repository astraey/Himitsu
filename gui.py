from tkinter import *
import tkinter.filedialog, tkinter.ttk, time, random, tkinter.simpledialog, tkinter.messagebox, encrypt, decrypt, functions



root = Tk()
root.wm_title("")
root.configure(bg='#ececec')
root.resizable(0,0)
message = StringVar()

topFrame = Frame(root)
topFrame.configure(bg='black')
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.configure(bg='#ececec')
bottomFrame.pack(side=BOTTOM)

title_opt = {'padx': 50, 'pady': 30}
of_opt = {}
of_opt['filetypes'] = [('WAV files','.wav')]
button1_opt = {'pady': (30, 15)}
pb_opt = {'pady': 45}
message_opt = {'pady': (0, 45)}


def openFile():
    filename = tkinter.filedialog.askopenfilename(**of_opt)

    if filename:
        barProgress()
        return filename


def barProgress():
    global mpb
    progress = 0
    while progress < 100:
        progress += random.randint(0,20)
        mpb['value'] = progress
        mpb.update()
        time.sleep(random.uniform(0,0.5))


def callback_b1():
    message.set("")
    textInput = tkinter.simpledialog.askstring("Enter a message", "Text to encrypt", parent = root)
    if textInput:
        name = openFile()
        encrypt.encryptMessage(name, textInput)
        print("[Message Encrypted] " + name)


def callback_b2():
    message.set("")
    name = openFile()
    decryptedMessage = decrypt.decryptMessage(name)
    print("[Message Decrypted] " + decryptedMessage)
    message.set(decryptedMessage)


title = Label(topFrame, text="Himitsu", font=("Helvetica", 48), fg="white", background='black')
title.pack(title_opt)

openButton = Button(root, text='Encrypt message in file', background="#ececec", highlightbackground='#ececec', command=callback_b1)
openButton.pack(button1_opt)

saveButton = Button(root, text='Decrypt message in file', background = "#ececec", highlightbackground='#ececec', command=callback_b2)
saveButton.pack()

mpb = tkinter.ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate", value=0, maximum=100)
mpb.pack(pb_opt)

secretText = Label(bottomFrame, textvariable=message, font=("Helvetica", 12), background='#ececec', highlightbackground='#ececec', wraplengt=200)
secretText.pack(message_opt)

root.mainloop()
