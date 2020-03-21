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
        self.textHeading()
        self.textCenter()
        self.exitButton()
        self.portScanButton()
        # tekstveld en de buttons die op het scherm moeten komen worden met de volgende functies aangemaakt.
        self.root.mainloop()

    def textHeading(self):
        self.topText = tk.Text(self.root, width=115, height=3)
        self.topText.insert(tk.INSERT, "ID\tHost\t\t\topen ports\t\t\t\tService\n\n")
        self.topText.pack()
        self.topText.configure(state='disabled')

    def textCenter(self):
        self.centerText = tk.Text(self.root, width=115, height=90)
        self.centerText.configure(state='normal')
        self.centerText.delete(1.0, tk.END)
        for rows in range(len(self.model.data)):
            self.centerText.insert(tk.INSERT, "{id}\t{host}\t\t\t{ports}\t\t\t\t{services}\n\n".format(id=self.controller.getId(rows),
                                                                                                         host=self.controller.getHost(rows),
                                                                                                         ports=self.controller.getOpenPorts(rows),
                                                                                                         services=self.controller.getService(rows)))
        self.centerText.update_idletasks()
        self.centerText.pack()
        self.centerText.configure(state='disabled')

    def exitButton(self):
        self.exitButton = tk.Button(self.root, text="Exit", width=8, command = self.root.destroy)
        self.exitButton.place(x=600, y=400)

    def portScanButton(self):
        self.portScanButton = tk.Button(self.root, width=8, text="Portscan", command = lambda : [self.root.destroy(), os.system("python3 PortscanMain.py")])
        self.portScanButton.place(x=700, y=400)
