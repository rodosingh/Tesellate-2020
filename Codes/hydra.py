from math import *
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  
import matplotlib.pyplot as plt   

# required equation...
def rose(theta, x):
    phi = (pi/2)*exp(-theta/(8*pi))
    X = 1 - 0.5*((5/4)*(1-((3.6*theta)%(2*pi))/pi)**2-0.25)**2
    y = (1.95653*x**2)*((1.27689*x-1)**2)*sin(phi)
    r = X*(x*sin(phi)+y*cos(phi))
    return r*sin(theta), r*cos(theta), X*(x*cos(phi)-y*sin(phi))

# build data
def data_maker(rng):
    X, Y, Z = [], [], []
    x = np.linspace(0,1,rng)
    theta = np.linspace(-2*pi, 15*pi, rng)
    for i in x:
        for j in theta:
            xx, yy, zz = rose(j, i)
            X.append(xx)
            Y.append(yy)
            Z.append(zz)
    return np.array(X), np.array(Z), np.array(Z)

# plot the HYDRA
def plotter_3D(X, Y, Z):
    # Creating figure 
    fig = plt.figure(figsize =(20, 20))   
    ax = plt.axes(projection ='3d')   

    # Creating color map 
    my_cmap = plt.get_cmap('ocean_r')#r meaning reverse gradient 

    # Creating plot 
    #sctt = ax.scatter3D(X, Y, Z, c = Z, cmap = my_cmap, alpha = 0.8, marker ='o')
    #fig.colorbar(sctt, ax = ax, shrink = 0.5, aspect = 5)
    trisurf = ax.plot_trisurf(X, Y, Z, 
                             cmap = my_cmap, 
                             edgecolor = None)#'grey') linewidth = 0.2,  antialiased = True,  
                             
    fig.colorbar(trisurf, ax = ax, shrink = 0.5, aspect = 5) 
    ax.set_title('Rose') 

    # Adding labels 
    ax.set_xlabel('X-axis', fontweight ='bold')  
    ax.set_ylabel('Y-axis', fontweight ='bold')  
    ax.set_zlabel('Z-axis', fontweight ='bold') 

    # show plot 
    plt.show() 
    
    
# plot
X, Y, Z = data_maker(150)
plotter_3D(X, Y, Z)
