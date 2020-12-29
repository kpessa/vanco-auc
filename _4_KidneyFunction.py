import numpy as np

class KidneyFunction:
    pt = None
    SCr = 0
    SCrDateTime = None
    ManuallyEnteredCrCl = 0
    OtherNephrotoxicDrugs = ""
    ManuallyEnteredQ = None
    RoundedUpSCrQ = None
    UsedAdjBWQ = None
    
    def __init__(self, pt, random=False, SCr = 0):
        def getRandomSCr():
            SCr = [0.85, 0.1]
            return np.random.normal(*SCr,1)[0]
        
        self.pt = pt
        if random:
            self.SCr = getRandomSCr()
        else:
            self.SCr = SCr
    
    def WeightUsed(self):
        if self.pt.char.TBW() < self.pt.char.IBW():
            return self.pt.char.TBW()
        elif self.pt.char.TBW_IBW_13Q():
            return self.pt.char.AdjBW()
        else:
            return self.pt.char.IBW()
    
    def CrCl(self):
        if self.pt.char.Gender == 'M':
            correction = 1
        if self.pt.char.Gender == 'F':
            correction = 0.85
        
        CrCl = ((140 - self.pt.char.Age)*self.WeightUsed()) / ( self.SCr * 72 ) * correction
        
        return CrCl