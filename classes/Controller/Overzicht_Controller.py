class dataHandler:

    def __init__(self, model):
        self.model = model
        self.host = []
        #

    def setTextCenter(self):
        for rows in range(len(self.model.getDataSource())):
            data = dataHandler(self.model)
            data.setId(self.model.data[rows][0])
            data.setHost(self.model.data[rows][1])
            data.setOpenPorts(self.model.data[rows][2])
            data.setService(self.model.data[rows][3])
            #
            self.host.append(data)

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setHost(self, host):
        self.host = host

    def getHost(self):
        return self.host

    def setOpenPorts(self, ports):
        self.ports = ports

    def getOpenPorts(self):
        return self.ports

    def setService(self, service):
        self.service = service

    def getService(self):
        return self.service


