#Less quick plotting tool

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm 
import numpy as np

vdv_diameter = 2.4

#Initial setup
theta_start = 0
theta_max = 180
theta_step = 5
num_angles = theta_max//theta_step

#Create axes
#fig, axarr = plt.subplots(2,2,figsize=(20,20))
#for i in range(2):
#        for j in range(2):
#            axarr[i,j].yaxis.grid()
#            axarr[i,j].set(xlabel="Separation (Relative to sum of VdW radii)")
# 
#axarr[0,0].set(ylabel="$V_{ee}$ (kJ mol$^{-1}$)")
#axarr[0,1].set(ylabel="$V_{ee}C$ (kJ mol$^{-1}$)")
#axarr[1,0].set(ylabel="$V_{ee}X$ (kJ mol$^{-1}$)")
#axarr[1,1].set(ylabel="T (kJ mol$^{-1}$)")
color1=iter(cm.viridis(np.linspace(0.1,0.9,num_angles + 1)))

#fig = plt.figure()
#ax = fig.gca(projection='3d')
Z1 = np.zeros((theta_max//theta_step +1, 16))
Z2 = np.zeros((theta_max//theta_step +1, 16))
Z3 = np.zeros((theta_max//theta_step +1, 16))
Z4 = np.zeros((theta_max//theta_step +1, 16))
Z5 = np.zeros((theta_max//theta_step +1, 16))
Z6 = np.zeros((theta_max//theta_step +1, 16))

#Process rawdataFULL files and plot results for each angle
max_energies = []
for theta in range(theta_start,theta_max+1,theta_step):
    if theta == 95:
        continue
    ind = theta//theta_step
    separations = [];
    Vol1, Vol2, q1, q2, rho1, rho2 = [], [], [], [], [], []
    #open data file.
    dataFile = open("rawdataFULL" + str(theta) + "_F1F3.txt", 'r');
    for line in dataFile:
        if line.startswith('Separation'):
            continue
        temp = line.split();
        separations.append(float(temp[0])/vdv_diameter); 
        Vol1.append(float(temp[13])); Vol2.append(float(temp[14]));
        q1.append(float(temp[15])); q2.append(float(temp[16]));
    
    rho1 = [q1[i]/Vol1[i] for i in range(len(Vol1))]
    rho2 = [q2[i]/Vol2[i] for i in range(len(Vol2))]
    for j in range(16):
        Z1[ind, j] = Vol1[j]
        Z2[ind, j] = Vol2[j]
        Z3[ind, j] = q1[j]
        Z4[ind, j] = q2[j]
        Z5[ind, j] = rho1[j]
        Z6[ind, j] = rho2[j]

        
    
c1 = next(color1)
#c2 = next(color2)
X = separations[:16]
Y = [theta for theta in range(0,theta_max+1,theta_step)]
X, Y = np.meshgrid(X, Y)
#x, y = np.mgrid[0.7:1.3:0.1176/2.94, 0:180:5]
#from mayavi import mlab
#s = mlab.surf(x, y, Z1)
#mlab.show()

#ax.plot_surface(X, Y, Z1, cmap=cm.Greys_r)
#ax.plot_surface(X, Y, Z2, cmap=cm.Reds_r)
#ax.plot_surface(X, Y, Z3, cmap=cm.Blues_r)
#ax.plot_surface(X, Y, Z4, cmap=cm.Greens_r)
ax.plot_surface(X, Y, Z5, cmap=cm.Oranges_r)
ax.plot_surface(X, Y, Z6, cmap=cm.Purples)
#ax.plot(X, Y, VEEC_rel[:16], color=c2)
#ax.plot(X, Y, VEE_rel[:16], color=c1)

ax.set_xlabel("Separation (Relative to sum of VdW radii)")
ax.set_ylabel("Theta (º)")
ax.set_zlabel(u"U+03C1 (C Å$^{-3}$)")
ax.set_xlim(0.7,1.3)
ax.set_xticks(list(np.linspace(0.7,1.3,7)))
ax.set_ylim(0,180)
#fig.colorbar(plt1, aspect=1,shrink=0.05, ticks=[]).set_label("$V_{ee}$")
#fig.colorbar(plt2, aspect=1,shrink=0.05, ticks=[]).set_label("$V_{ne}$")
#ax.set_zticks(list(range(0,2750,500)))

#plt.show()


#    plt.plot(separations[:16], VEE_rel[:16], color='g', label="$V_{ee}$")
#    plt.plot(separations[:16], VEEC_rel[:16], color='y', label="$V_{ee}C$")
#    plt.plot(separations[:16], VEEX_rel[:16], color='m', label="$V_{ee}X$")
#    plt.plot(separations[:16], Edef[:16], color='k', label="$E_{def}$")
#    plt.plot(separations[:16], [0 for i in range(16)], color = 'k', alpha = 0.2)
#    plt.xlim((0.7,1.3))
#    plt.ylim((-1000,6000))
#    plt.xlabel("Separation (Relative to sum of VdW radii)")
#    plt.ylabel("$V_{ee}$ (kJ mol$^{-1}$)")
#    plt.title("Decomposition of Fluorine $V_{ee}$ - " + str(theta) + "º")
#    plt.legend()
#    plt.savefig("../results/Line_plots/Fluorine/gif/VEE_fixed/HF_relF"+str(theta), dpi = 100)
#    print(theta)
#    plt.close()
    
    #c1 = next(color1)
    #axarr[0,0].plot(separations[:16], VEE_rel[:16], label=str(theta)+"º", color=c1)
    #axarr[0,1].plot(separations[:16], VEEC_rel[:16], label=str(theta)+"º", color=c1)
    #axarr[1,1].plot(separations[:16], T_rel[:16], label=str(theta)+"º", color=c1)
    #axarr[1,0].plot(separations[:16], VEEX_rel[:16], label=str(theta)+"º", color=c1)
    #axarr[1,0].plot(separations[:16], VEEC_rel[:16], color='b', alpha=0.5)
    #axarr[1,0].plot(separations[:16], VEEX_rel[:16], color='r', alpha=0.5)


#axarr[0,0].legend()
#axarr[0,1].legend()
#axarr[1,0].legend()
#axarr[1,1].legend()

#plt.savefig("../results/Line_plots/Fluorine/subplots/HF_relFVEE", dpi=200)

