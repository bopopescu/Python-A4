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
        self.secondRoot.mainloop()

    def backgroundImage(self):
        Image_path = str("images/78ed85ae85ea337b9b524766290f6b7a.gif")
        image1 = tk.PhotoImage(file=Image_path)
        w = image1.width()
        h = image1.height()
        #
        self.secondRoot.geometry("%dx%d+0+0" % (w, h))
        self.panel1 = tk.Label(self.secondRoot, image=image1)
        self.panel1.pack(side='top', fill='both', expand='yes')
        self.panel1.image = image1

    def textHeading(self):
        self.topText = tk.Text(self.panel1, width=40, height=1, font=("Helvetica", 14, 'bold'))
        self.topText.insert(tk.INSERT, "\tPoortscanner Michel Disbergen")
        self.topText.pack()
        self.topText.configure(state='disabled')

    def textCenter(self):
        self.centerText = tk.Text(self.panel1, width=40, height=3)
        self.centerText.insert(tk.INSERT, "1 - voer een IP in \n2 - vink (optioneel) de checkboxes aan \n3 - klik op de button scan now")
        self.centerText.pack()
        self.centerText.configure(state='disabled')

    def inputField(self):
        self.inputBox = tk.Label(self.panel1, text="IP invoeren :", bg="white")
        self.inputBox.place(x=12, y=100)
        inputBoxString = tk.StringVar()
        self.inputBox = tk.Entry(self.panel1, textvariable=inputBoxString, width="20")
        self.inputBox.place(x=12, y=120)

    def checkBoxUdp(self):
        self.checkUdp = tk.IntVar()
        self.checkBoxOne = tk.Checkbutton(self.panel1, text="scan for UDP ports only", variable=self.checkUdp, onvalue=1, offvalue=0, bg="white")
        self.checkBoxOne.pack()
        self.checkBoxOne.place(x=10, y=150)

    def checkBoxService(self):
        self.checkService = tk.IntVar()
        self.checkBoxTwo = tk.Checkbutton(self.panel1, text="Enable service detection", variable=self.checkService, onvalue=1, offvalue=0, bg="white")
        self.checkBoxTwo.pack()
        self.checkBoxTwo.place(x=10, y=170)

    def scanNowButton(self):
        self.scanButton = tk.Button(self.panel1, text="scan now", width=8, command=lambda: [print("Starting scan on host : {host}".format(host=self.inputBox.get())),
                                                                                            self.controller.scanPorts(self.inputBox.get(), self.checkUdp.get(), self.checkService.get(), self.centerText)])
        self.scanButton.place(x=420, y=480)