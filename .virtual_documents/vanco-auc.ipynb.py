import math
import numpy as np
import matplotlib.pyplot as plt


Dose = 1000 # mgs
t_inf = 1 # hrs
K_e = 0.100 
V_d = 50 # L


def c_inf(t):
    return R_0 / CL_vanco * (1 - math.exp(-K_e * t))


R_0 = Dose / t_inf
CL_vanco = K_e * V_d


cmax = R_0 / CL_vanco * (1 - math.exp(-K_e * t_inf))


def c_post(t):
    return cmax * math.exp(-K_e * (t - t_inf))


def concentration(t):
    if t <= t_inf:
        return c_inf(t)
    else:
        return c_post(t)


def labelPlot():
    plt.xlabel('hrs')
    plt.ylabel('concentration')
    plt.ylim(0,25)
    plt.xlim(0-0.5,tau+0.5)
    plt.title('First-order Concentration Plot')
    
def annotateInterestingPoints():
    plt.annotate(f"Cmax: {cmax:.1f}",xy = (1,cmax),xytext = (0,10),textcoords ='offset points')
    plt.annotate(f"Cpeak: {cpeak:.1f}",(1+1,cpeak),xytext = (5,5),textcoords ='offset points')
    plt.annotate(f"Ctrough: {ctrough:.1f}",(tau-0.5,ctrough),xytext = (-70,-15),textcoords ='offset points')
    plt.annotate(f"Cmin: {cmin:.1f}",(tau,cmin),xytext = (-50,-30),textcoords ='offset points')


X = np.linspace(0,12,100) 
Y = [concentration(t) for t in X]


plt.figure(figsize = (10,6))

plt.plot(X,Y)

#interesting points
tau = 12
cmax = concentration(1)
cpeak = concentration(1+1) # <~ wait 1? hr after infusion
ctrough = concentration(tau-0.5) # <~ 30 min before next dose
cmin = concentration(tau)
plt.scatter(x=[1,1+1,tau-0.5,tau],y=[cmax,cpeak,ctrough,cmin])
annotateInterestingPoints()
labelPlot()



