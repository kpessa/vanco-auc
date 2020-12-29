import random as rand
from datetime import datetime as dt

import names

class Diagnosis:
    ConsultingPhysician = ""
    SuspectedIndication = ""
    MIC = ""
    Target = ""
    StartDateTime = None
    
    def __init__(self, random = False, ConsultingPhysician = "", SuspectedIndication = "", MIC = 1, StartDateTime = dt.now()):
        statuses = ['Active','Discharged','Med Discontinued']
        providers = "Hippocrates, Joseph Lister, Edward Jenner, Alexander Fleming, Louis Pasteur, Sigmund Freud, Galen, Adreas Vesalius, Avicenna, Paracelsus, Aton Chekhov, Michael Crichton, Sanjay Gupta".split(", ")
        indications = "Skin and Soft Tissue Infection, Pneumonia, Bacteremia, Osteomyelitis, Meningitis, Intra-abdominal, Sepsis (Unknown Source), Urinary Tract Infection, Non-MRSA Infection, UTI, PNA, SSTI, Sepsis".split(", ")
    
        if random:
            self.ConsultingPhysician = rand.choice(providers)
            self.SuspectedIndication = rand.choice(indications)
        else:
            self.ConsultingPhysician = ConsultingPhysician
            self.SuspectedIndication = SuspectedIndication
        self.MIC = 1
        self.StartDateTime = StartDateTime