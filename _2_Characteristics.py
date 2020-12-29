import random as rand
import numpy as np
from math import floor

class Characteristics:
    Height = 0
    Weight = 0
    Age = 0
    Gender = ''
    
    def __init__(self, random=False, Height = 0, Weight = 0, Age = 0, Gender = ''):
        def getRandomHeight():
                height = [175, 10]
                return np.random.normal(*height,1)[0]
        def getRandomWeight():
            weight = [80, 20]
            return np.random.normal(*weight,1)[0]
        def getRandomAge():
            age = [55, 10]
            return floor(np.random.normal(*age,1)[0])
        def getRandomGender():
            return rand.choice(['M','F'])
        
        if random:
            self.Height = getRandomHeight()
            self.Weight = getRandomWeight()
            self.Age = getRandomAge()
            self.Gender = getRandomGender()
        else:
            self.Height = Height
            self.Weight = Weight
            self.Age = Age
            self.Gender = Gender
    
    # Different Weights
    def weightRounded(self):
        return round(self.Weight,1)
    def weightRoundedWithDescriptor(self):
        return f"{self.weightRounded()} kg"
    def weightInLbs(self):
        return self.Weight * 2.2
    def weightInLbsRounded(self):
        return round(self.weightInLbs(),1)
    def weightInLbsRoundedWithDescriptor(self):
        return f"{self.weightInLbsRounded()} lbs"
    def setWeightFromLbs(self,wt_lbs):
        self.Weight = wt_lbs / 2.2
        
    # Different Heights
    def heightRounded(self):
        return round(self.Height,1)
    def heightRoundedWithDescriptor(self):
        return f"{self.heightRounded()} cm"
    def heightInInches(self):
        return self.Height / 2.54
    def heightInInchesRounded(self):
        return round(self.heightInInches(),1)
    def heightInInchesRoundedWithDescriptor(self):
        return f"{self.heightInInchesRounded()} in"
    def heightInchesOver5Ft(self):
        return self.heightInInches()-60 
    def heightInFeetAndInches(self):
        htInches = self.heightInInches()
        ft = floor(htInches/12)
        inRemaining = htInches - ft*12
        return f"{ft}'{inRemaining:.0f}\""
    
    # Anthropomorphics
    def TBW(self):
        return self.Weight
    def IBW(self):
        if self.Gender == 'M':
            return 50 + 2.3 * self.heightInchesOver5Ft()
        if self.Gender == 'F':
            return 45.5 + 2.3 * self.heightInchesOver5Ft()
    def AdjBW(self):
        return self.IBW() + 0.4 * (self.TBW() - self.IBW())
    def BMI(self):
        return self.Weight / (self.Height / 100) ** 2
    def TBW_IBW(self):
        return self.TBW()/self.IBW()
    def obeseQ(self):
        if self.BMI() >= 30:
            return True
        else:
            return False
    def TBW_IBW_13Q(self):
        if self.TBW_IBW() >= 1.3:
            return True
        else:
            return False