from database.Connection import *

class dataObject:

    def __init__(self):
        self.data = self.getDataSource()

    def getDataSource(self):
        query = ("SELECT ID, Host, `Open ports`, Service FROM `Host info`")
        mycursor.execute(query)
        return mycursor.fetchall()

