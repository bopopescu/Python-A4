import nmap
import tkinter as tk

class dataHandler:
    def __init__(self, model):
        self.model = model
        #

    def scanPorts(self, host, udp, service, centerText):
        self.host = host
        self.udp = udp
        self.service = service
        self.centerText = centerText
        #
        self.portsFound = []
        self.servicesFound = []
        #
        self.nm = nmap.PortScanner()
        self.nm.scan(self.host, '1-1024')
        # scanned de host (IP) vanaf poort 1 t/m 65535 (In dit geval heb ik het tot 1024 gedaan zodat het niet al te lang duurt).
        self.appendPorts()

    def appendPorts(self):
        if self.udp == 0 and self.service == 0:
            self.portsFound = self.nm[self.host].all_tcp()
        # Append alle gevonden TCP poorten naar de array self.portsFound
        elif self.udp == 1 and self.service == 0:
            self.portsFound = self.nm[self.host].all_udp()
        # Append alle gevonden UDP poorten naar de array self.portsFound
        elif self.udp == 0 and self.service == 1:
            for port in range(len(self.nm[self.host].all_tcp())):
                self.portsFound.append(self.nm[self.host].all_tcp()[port])
                self.servicesFound.append(self.nm[self.host]['tcp'][self.nm[self.host].all_tcp()[port]]['name'])
        # append alle gevonden TCP poorten
        # append alle gevonden services van poorten
        else:
            for port in range(len(self.nm[self.host].all_udp())):
                self.portsFound.append(self.nm[self.host].all_udp()[port])
                self.servicesFound.append(self.nm[self.host]['udp'][self.nm[self.host].all_udp()[port]]['name'])
        # append alle gevonden UDP poorten
        # append alle gevonden services van poorten
        if len(self.portsFound) == 0:
            self.centerText.configure(state='normal')
            self.centerText.insert(tk.INSERT, "\n\nscan on host {} COMPLETED, no open ports!".format(self.host))
            self.centerText.configure(state='disabled')
        else:
            self.centerText.configure(state='normal')
            self.centerText.insert(tk.INSERT, "\n\nscan on host {} COMPLETED!".format(self.host))
            self.centerText.configure(state='disabled')
            print("The following services were found \nHOST: {} \nPORTS: {} \nSERVICES: {}".format(self.host, str(self.portsFound,), str(self.servicesFound) ))
            if len(self.servicesFound) == 0:
                self.model.createQuery(self.host, self.portsFound, None)
            else:
                self.model.createQuery(self.host, self.portsFound, self.servicesFound)
