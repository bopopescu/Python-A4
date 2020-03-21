from database.Connection import *

class dataObject:

    def insertData(self, host, ports, services):
        self.host = host
        self.ports = ports
        self.services = services
        #
        print(host, ports, services)
        query = "INSERT INTO `host info` (`Host`, `Open ports`, `Service`) VALUES (%s,%s,%s)"
        data = (str(self.host), str(self.ports), str(self.services))
        self.submitQuery(query, data)

    def submitQuery(self, query, data):
        mycursor.execute(query, data)
        mydb.commit()