"Variables def"
import numpy as np 


N=50 #Number of grid points
L=2 #domain size
#corresponding grid space
h=np.float64(L/(N-1))
k=0.1 #diffusive coefficient , here its the thermal conductivity 
A=0.001 #cross-sectional area
