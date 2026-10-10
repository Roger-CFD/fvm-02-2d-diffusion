import numpy as np 
import matplotlib.pyplot as plt


def PureSolver(k,A,h,N):
    #Initialise temperature field
    T=np.zeros((N,N))
    T[0,:]=1
    T[:,0]=1
    #Initialise Iterated temperature field 
    T_new=T.copy()
    #Error Sensitivity 
    epsilon=1.E-8
    num_error=1
    
    #plot error
    plt.figure(10)
    #Iteration number 
    Iterations=0 

    
    #Check the error tolerance 
    while num_error>epsilon:
        #computing for all interior points 
        for i in range(1,N-1):
            for j in range(1,N-1):
                a_E=np.float64(k*A/h)
                a_W=np.float64(k*A/h)
                a_N=np.float64(k*A/h)
                a_S=np.float64(k*A/h)
                a_P=a_E+a_W+a_N+a_S
                T_new[i,j]=(a_E*T[i,j+1]+a_W*T[i,j-1]+a_N*T[i+1,j]+a_S*T[i-1,j])/a_P
        #Resetting the numerical error and recalculate 
        num_error=0
        for i in range(1,N-1):
            for j in range(1,N-1):
                num_error=num_error+abs(T[i,j]-T_new[i,j])
        #calc. new interation 
        Iterations=Iterations+1
        T=T_new.copy()
        #ploting numerical error every 1000 iterations 
        if Iterations%1000 ==0:
            plt.figure(10)
            plt.semilogy(Iterations, num_error, 'ko')
            plt.pause(0.01)
        if num_error<epsilon:  
            plt.figure(10)
            plt.semilogy(Iterations, num_error, 'ko')
            plt.pause(0.01)
    return T_new        