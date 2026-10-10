import numpy as np 
import matplotlib.pyplot as plt 

"author Stan"
"main script"
import var_2D_pure_diff
import solver_2D_pure_diff


#solve for T
T=PureSolver(k,A,h,N)
#Defining the position vector and the grid from indices 
x_dom=np.arange(N)*h
y_dom=L-np.arange(N)*h
[X,Y]=np.meshgrid(x_dom,y_dom)

#ploting contour 

plt.figure(11)
cs = plt.contourf(X, Y, T, 12) 
cbar = plt.colorbar(cs)
cbar.set_label('T value')

plt.grid(True, color='k')
plt.title("T(x,y)")


"show plot"
plt.show()

