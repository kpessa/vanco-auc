import random as rand
import numpy as np
import names
from math import floor

class Identifiers:
    MRN = 0
    LastName = ""
    FirstName = ""
    Service = ""
    Room = ""
    
    def __init__(self, MRN=0, LastName="", FirstName="", Service="", Room="", random = False):
        services = "ICU, ER, ERHD, 2NS1, 2NS2, 3NS1, 3NS2, 3NSD, SICU".split(", ")
        
        def getRandomMRN():
            mrns = [500000, 100000]
            return floor(np.random.normal(*mrns,1)[0])
        def getRandomRoom():
            return rand.randint(1,399)
        
        if random:
            self.random = random
            self.MRN = getRandomMRN()
            self.LastName = names.get_last_name()
            self.FirstName = names.get_first_name()
            self.Service = rand.choice(services)
            self.Room = getRandomRoom()
        else:
            self.random = random
            self.MRN = MRN 
            self.LastName = LastName
            self.FirstName = FirstName
            self.Service = Service
            self.Room = Room
        