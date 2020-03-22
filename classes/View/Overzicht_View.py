import tkinter as tk
import os

class Window:

    def __init__(self, controller, model):
        self.controller = controller
        self.model = model
        #
        self.root = tk.Tk()
        self.root.title("MVC applicatie - overzicht poortscanner")
        self.root.geometry("1000x600")
        #
        self.backgroundImage()
        self.textHeading()
        # self.textCenter()
        self.exitButton()
        self.portScanButton()
        # tekstveld en de buttons die op het scherm moeten komen worden met de volgende functies aangemaakt.
        self.root.mainloop()

    def backgroundImage(self):
        Image_path = "images/confetti-png-gif.gif"
        image1 = tk.PhotoImage(file=Image_path)
        w = image1.width()
        h = image1.height()
        self.root.geometry("%dx%d+0+0" % (w, h))

        self.panel1 = tk.Label(self.root, image=image1, text=[self.textHeading(), self.textCenter()], compound=tk.CENTER)
        self.panel1.pack(side='top', fill='both', expand='yes')

        self.panel1.image = image1

    def textHeading(self):
        self.topText = tk.Text(self.root, width=115, height=3)
        self.topText.insert(tk.INSERT, "Number\tID\tHost\t\t\topen ports\t\t\t\tService\n\n")
        self.topText.pack()
        self.topText.configure(state='disabled')

    def textCenter(self):
        self.centerText = tk.Text(self.root, width=115, height=90)
        self.centerText.configure(state='normal')
        self.centerText.delete(1.0, tk.END)
        for rows in range(len(self.model.data)):
            self.centerText.insert(tk.INSERT, "{rows}\t{id}\t{host}\t\t\t{ports}\t\t\t\t{services}\n\n".format(rows=rows+1,
                                                                                                                id=self.controller.getId(rows),
                                                                                                                host=self.controller.getHost(rows),
                                                                                                                ports=self.controller.getOpenPorts(rows),
                                                                                                                services=self.controller.getService(rows)))
        self.centerText.pack()
        self.centerText.configure(state='disabled')

    def exitButton(self):
        self.exitButton = tk.Button(self.panel1, text="Exit", width=8, command=self.root.destroy)
        self.exitButton.place(x=320, y=500)

    def portScanButton(self):
        self.portScanButton = tk.Button(self.panel1, width=8, text="Portscan",
                                        command=lambda: [self.root.destroy(), os.system("python3 PortscanMain.py")])
        self.portScanButton.place(x=420, y=500)
