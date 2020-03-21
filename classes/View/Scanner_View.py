import tkinter as tk

class Window:

    def __init__(self, controller, model):
        self.controller = controller
        self.model = model
        #
        self.secondRoot = tk.Tk()
        self.secondRoot.title("MVC applicatie - gebruik poortscanner")
        #
        self.backgroundImage()
        self.textHeading()
        self.textCenter()
        self.inputField()
        self.checkBoxUdp()
        self.checkBoxService()
        self.scanNowButton()
        #
        self.secondRoot.geometry("400x400")
        self.secondRoot.mainloop()

    def backgroundImage(self):
        pass

    def textHeading(self):
        self.topText = tk.Text(self.secondRoot, width=90, height=1, font=("Helvetica", 16, 'bold'))
        self.topText.insert(tk.INSERT, "Poortscanner -- Michel Disbergen")
        self.topText.pack()
        self.topText.configure(state='disabled')

    def textCenter(self):
        self.centerText = tk.Text(self.secondRoot, width=90, height=3)
        self.centerText.insert(tk.INSERT, "1 - voer een IP in \n2 - vink (optioneel) de checkboxes aan \n3 - klik op de button scan now")
        self.centerText.pack()
        self.centerText.configure(state='disabled')

    def inputField(self):
        self.inputBox = tk.Label(self.secondRoot, text="IP invoeren :")
        self.inputBox.place(x=10, y=100)
        inputBoxString = tk.StringVar()
        self.inputBox = tk.Entry(self.secondRoot, textvariable=inputBoxString, width="20")
        self.inputBox.place(x=10, y=120)

    def checkBoxUdp(self):
        self.checkUdp = tk.IntVar()
        self.checkBoxOne = tk.Checkbutton(self.secondRoot, text="enable UDP detection", variable=self.checkUdp, onvalue=1, offvalue=0)
        self.checkBoxOne.pack()
        self.checkBoxOne.place(x=10, y=150)

    def checkBoxService(self):
        self.checkService = tk.IntVar()
        self.checkBoxTwo = tk.Checkbutton(self.secondRoot, text="Enable service detection", variable=self.checkService, onvalue=1, offvalue=0)
        self.checkBoxTwo.pack()
        self.checkBoxTwo.place(x=10, y=170)

    def scanNowButton(self):
        self.scanButton = tk.Button(self.secondRoot, text="scan now", width=8, command=lambda: self.controller.scanPorts(self.inputBox.get(), self.checkUdp.get(), self.checkService.get(), self.centerText))
        self.scanButton.place(x=260, y=320)
