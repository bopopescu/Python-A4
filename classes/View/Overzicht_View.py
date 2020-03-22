import tkinter as tk
import os

class Window:

    def __init__(self, controller, model):
        self.controller = controller
        self.model = model
        #
        self.root = tk.Tk()
        self.root.configure()
        self.root.title("MVC applicatie - overzicht poortscanner")
        self.root.geometry("1000x600")
        #
        self.textHeading()
        self.textCenter()
        self.exitButton()
        self.portScanButton()
        # tekstveld en de buttons die op het scherm moeten komen worden met de volgende functies aangemaakt.
        self.root.mainloop()

    def textHeading(self):
        self.topText = tk.Text(self.root, width=115, height=1, bg='green', borderwidth=2, relief="solid")
        self.topText.insert(tk.INSERT, "Number\tID\tHost\t\t\t\topen ports\t\t\t\tService\n\n")
        self.topText.pack()
        self.topText.configure(state='disabled')

    def textCenter(self):
        self.centerText = tk.Text(self.root, width=115, height=90, borderwidth=2, relief="sunken")
        for rows in range(len(self.model.data)):
                self.centerText.insert(tk.INSERT, "{rows}\t{id}\t{host}\t\t\t\t{ports}\t\t\t\t{services}\n\n".format(rows=rows + 1,
                                                                                                          id=self.controller.getId(rows),
                                                                                                          host=self.controller.getHost(rows),
                                                                                                          ports=self.controller.getOpenPorts(rows),
                                                                                                          services=self.controller.getService(rows)))
        self.centerText.pack()
        self.centerText.configure(state='disabled')

    def exitButton(self):
        self.exitButton = tk.Button(self.root, text="Exit", width=8, command=self.root.destroy)
        self.exitButton.place(x=700, y=550)

    def portScanButton(self):
        self.portScanButton = tk.Button(self.root, width=8, text="Portscan", command=lambda: [self.root.destroy(), os.system("python3 PortscanMain.py")])
        self.portScanButton.place(x=800, y=550)
