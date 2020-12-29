class LoadDose:
    
    def __init__(self, pt,  default = False):
        self.pt = pt
        
        if pt.diag.SuspectedIndication in "Urinary Tract Infection, Cellulitis, UTI, SSTI, Skin and Soft Tissue Infection".split(", "):
            self.givenQ = False
        else:
            self.givenQ = True
        
    def CalculatedLD(self):
        return int(self.pt.char.Weight * 25)
    
    def LDDose(self):
        temp = self.CalculatedLD()
        if temp >= 2000:
            return 2000
        else:
            return int(round(temp/250,0)*250)
        
    def LDTinf(self):
        if self.LDDose() in [500]:
            return 0.5
        if self.LDDose() in [750, 1000]:
            return 1
        if self.LDDose() in [1250, 1500]:
            return 1.5
        if self.LDDose() in [1750, 2000]:
            return 2
            