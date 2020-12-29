import math

class PopulationBasedPKParameters:
    
    def __init__(self, pt):
        self.pt = pt
    
    def CLVancoEqnUsed(self):
        if self.pt.char.obeseQ():
            return "Crass"
        else:
            return "Matzke"
    
    def CLVanco(self):
        if self.CLVancoEqnUsed() == 'Matzke':
            return ((self.pt.kidney.CrCl() * 0.689) + 3.66) * 0.06
        if self.CLVancoEqnUsed() == 'Crass':
            if self.pt.char.Gender == 'M':
                correction = 1
            elif self.pt.char.Gender == 'F':
                correction = 0
            return 9.656 - 0.078 * self.pt.char.Age - 2.009 * self.pt.kidney.SCr + 1.09 * correction + 0.04 * (self.pt.char.TBW()) ** 0.75
    
    def Ke(self):
        return self.CLVanco()/self.Vd()
    
    def Vd_kg(self):
        if self.pt.char.obeseQ():
            return 0.55
        else:
            return 0.65
    
    def Vd(self):
        return self.pt.char.Weight * self.Vd_kg()
    
    def t1_2(self):
        return 0.693 / self.Ke()
   
    def Cmax(self, dose, tinf, tau):
        if self.Vd() == 0 or self.Ke() == 0 or tau == 0:
            return 0
        return self.Ceoi(dose,tinf,tau) / math.exp(-self.Ke() * tinf)

    def Ceoi(self, dose, tinf, tau):
        if self.Vd() == 0 or self.Ke() == 0 or tau == 0:
            return 0
        return ( dose / self.Vd() ) / (1 - math.exp(-self.Ke() * tau))
    
    def Cmin(self, dose, tinf, tau):
        if self.Vd() == 0 or self.Ke() == 0 or tau == 0:
            return 0
        return self.Cmax(dose, tinf, tau) * math.exp(-self.Ke() * tau)
    
    def AUC(self, dose, tinf, tau):
        if self.Vd() == 0 or self.Ke() == 0 or tau == 0 or tinf == 0:
            return 0
        Ceoi = self.Ceoi(dose,tinf,tau)
        Cmin = self.Cmin(dose,tinf,tau)
        
        AUCinf = (Ceoi + Cmin) / 2 * tinf
        AUCeli = (Ceoi - Cmin) / self.Ke()
        
        return int((AUCinf + AUCeli) * (24 / tau) / self.pt.diag.MIC)