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
        self.controller.setTextCenter()
        self.getTextCenter()
        self.exitButton()
        self.portScanButton()
        self.refreshButton()
        # tekstveld en de buttons die op het scherm moeten komen worden met de volgende functies aangemaakt.
        self.root.mainloop()

    def textHeading(self):
        self.topText = tk.Text(self.root, width=115, height=1, bg='green', borderwidth=2, relief="solid")
        self.topText.insert(tk.INSERT, "Number\tID\tHost\t\t\t\topen ports\t\t\t\tService\n\n")
        self.topText.pack()
        self.topText.configure(state='disabled')

    def getTextCenter(self):
        self.centerText = tk.Text(self.root, width=115, height=90, borderwidth=2, relief="sunken")
        self.centerText.configure(state='normal')
        self.centerText.delete(1.0, tk.END)
        number = 0
        for rows in self.controller.host:
            number = number + 1
            self.centerText.insert(tk.INSERT, "{NUM}\t{ID}\t{HOST}\t\t\t\t{OPENPORTS}\t\t\t\t{SERVICE}\n\n".format(NUM=number,
                                                                                                                    ID=rows.getId(),
                                                                                                                    HOST=rows.getHost(),
                                                                                                                    OPENPORTS=rows.getOpenPorts(),
                                                                                                                    SERVICE=rows.getService()))
        self.centerText.update_idletasks()
        self.centerText.pack()
        self.centerText.configure(state='disabled')

    def exitButton(self):
        self.exitButton = tk.Button(self.root, text="Exit", width=8, command=self.root.destroy)
        self.exitButton.place(x=600, y=550)

    def portScanButton(self):
        self.portScanButton = tk.Button(self.root, width=8, text="Portscan", command=lambda: os.system("python3 PortscanMain.py"))
        self.portScanButton.place(x=700, y=550)

    def refreshButton(self):
        self.refreshButton = tk.Button(self.root, width=8, text="refresh", command=lambda: [self.controller.setTextCenter(), self.getTextCenter()])
        self.refreshButton.place(x=800, y=550)
