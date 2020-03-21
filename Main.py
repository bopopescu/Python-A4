from classes.Controller.Overzicht_Controller import *
from classes.Model.Overzicht_Model import *
from classes.View.Overzicht_View import *

class Main:
    def __init__(self):

        self.model = dataObject()
        self.controller = dataHandler(self.model)
        self.view = Window(self.controller, self.model)

Main()