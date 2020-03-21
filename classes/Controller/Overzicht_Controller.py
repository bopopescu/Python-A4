
class dataHandler:

    def __init__(self, model):
        self.model = model
        self.data = self.model.data
        #
    def getId(self, id):
        return self.data[id][0]

    def getHost(self, host):
        return self.data[host][1]

    def getOpenPorts(self, ports):
        return self.data[ports][2]

    def getService(self, service):
        return self.data[service][3]


