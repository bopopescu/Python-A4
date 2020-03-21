from classes.Controller.Scanner_Controller import *
from classes.View.Scanner_View import *
from classes.Model.Scanner_Model import *

class PortscanMain:
    def __init__(self):

        self.model = dataObject()
        self.controller = dataHandler(self.model)
        self.view = Window(self.controller, self.model)

PortscanMain()