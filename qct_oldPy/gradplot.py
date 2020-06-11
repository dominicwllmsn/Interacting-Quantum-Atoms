#Less quick plotting tool

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm 
import numpy as np

vdv_diameter = 2.4
F_intra, H_intra = -241.16570052, -0.44486951591
F_T, H_T = 241.18435835, 0.72777814397
F_Vne, H_Vne = -568.27754306, -1.6021263761
F_Vee, H_Vee = 85.927484192, 0.42947871617

#Initial setup
theta_start = 0
theta_max = 0
theta_step = 10
num_angles = (theta_max-theta_start)//theta_step

#Create axes
fig, axarr = plt.subplots(2,2,figsize=(20,20))
for i in range(2):
        for j in range(2):
            axarr[i,j].yaxis.grid()
            axarr[i,j].set(xlabel="Separation (Relative to sum of VdW radii)")
 
axarr[0,0].set(ylabel="$E_{def}$ (kJ mol$^{-1}$)")
axarr[0,1].set(ylabel="$V_{ne}$ (kJ mol$^{-1}$)")
axarr[1,0].set(ylabel="$V_{ee}$ (kJ mol$^{-1}$)")
axarr[1,1].set(ylabel="T (kJ mol$^{-1}$)")
color1=iter(cm.viridis(np.linspace(0.1,0.9,num_angles + 1)))
#color2=iter(cm.magma(np.linspace(0.1,0.9,num_angles + 1)))

#fig = plt.figure()
#ax = fig.gca(projection='3d')
#Z1 = np.zeros((theta_max//theta_step +1, 16))
#Z2 = np.zeros((theta_max//theta_step +1, 16))
#Z3 = np.zeros((theta_max//theta_step +1, 16))
#Z4 = np.zeros((theta_max//theta_step +1, 16))
#Z5 = np.zeros((theta_max//theta_step +1, 16))
#Z6 = np.zeros((theta_max//theta_step +1, 16))

#Process rawdataFULL files and plot results for each angle
max_energies = []
for theta in range(theta_start,theta_max+1,theta_step):
    ind = theta//theta_step
    separations = [];
    Edef, SE1, VNE1, T1, VEE1, SE2, VNE2, T2, VEE2, VEEC1, VEEX1, VEEC2, VEEX2 \
    = [], [], [], [], [], [], [], [], [], [], [], [], [];
    SE3, VNE3, T3, VEE3, SE4, VNE4, T4, VEE4, VEEC3, VEEX3, VEEC4, VEEX4 \
    = [], [], [], [], [], [], [], [], [], [], [], [];
#    #open data file.
#    dataFile = open("rawdataFULL" + str(theta) + "_H2H4.txt", 'r');
#    for line in dataFile:
#        if line.startswith('Separation'):
#            continue
#        temp = line.split();
#        separations.append((float(temp[0]))/vdv_diameter); 
#        SE2.append(float(temp[1])/3.8088E-04); VNE2.append(float(temp[2])/3.8088E-04); 
#        T2.append(float(temp[3])/3.8088E-04);  VEE2.append(float(temp[4])/3.8088E-04); 
#        SE4.append(float(temp[5])/3.8088E-04); VNE4.append(float(temp[6])/3.8088E-04); 
#        T4.append(float(temp[7])/3.8088E-04); VEE4.append(float(temp[8])/3.8088E-04);
#        VEEC2.append(float(temp[9])/3.8088E-04); VEEX2.append(float(temp[10])/3.8088E-04);
#        VEEC4.append(float(temp[11])/3.8088E-04); VEEX4.append(float(temp[12])/3.8088E-04);
#        
    dataFile = open("rawdataFULL" + str(theta) + "_H2H6.txt", 'r');
    for line in dataFile:
        if line.startswith('Separation'):
            continue
        temp = line.split();
        separations.append((float(temp[0]))/vdv_diameter); 
        SE1.append(float(temp[1])/3.8088E-04); VNE1.append(float(temp[2])/3.8088E-04); 
        T1.append(float(temp[3])/3.8088E-04);  VEE1.append(float(temp[4])/3.8088E-04); 
        SE3.append(float(temp[5])/3.8088E-04); VNE3.append(float(temp[6])/3.8088E-04); 
        T3.append(float(temp[7])/3.8088E-04); VEE3.append(float(temp[8])/3.8088E-04);
        VEEC1.append(float(temp[9])/3.8088E-04); VEEX1.append(float(temp[10])/3.8088E-04);
        VEEC3.append(float(temp[11])/3.8088E-04); VEEX3.append(float(temp[12])/3.8088E-04);
    
    Edef = [SE1[i]+SE3[i]-(2*H_intra)/3.8088E-04 for i in range(len(SE1))]
    VEE_rel = [VEE1[i]+VEE3[i]- (2*H_Vee)/(3.8088E-04) for i in range(len(VEE1))]
    VNE_rel= [VNE1[i]+VNE3[i] - (2*H_Vne)/(3.8088E-04) for i in range(len(VNE1))]
    T_rel = [T1[i]+T3[i] - (2*H_T)/(3.8088E-04) for i in range(len(T1))]
#    VEEC_rel = [VEEC1[i]+VEEC3[i] - (2*F_VeeC)/(3.8088E-04) for i in range(len(VEEC1))]
#    VEEX_rel = [VEEX1[i]+VEEX3[i] - (2*F_VeeX)/(3.8088E-04) for i in range(len(VEEX1))]
#    Edef_lists.append(Edef)
#    for j in range(16):
#        l = j+5
#        Z1[ind, j] = Edef[l]
#        Z2[ind, j] = Edef2[l]
#        Z3[ind, j] = Edef3[l]
#        Z4[ind, j] = Edef4[l]
#        Z5[ind, j] = VEEC_rel[l]
#        Z6[ind, j] = VEEX_rel[l]
#        
#    c1 = next(color1)
#c2 = next(color2)
#X = separations[5:21]
#Y = [theta for theta in range(0,theta_max+1,theta_step)]
#X, Y = np.meshgrid(X, Y)
##x, y = np.mgrid[0.7:1.3:0.1176/2.94, 0:180:5]
##from mayavi import mlab
##s = mlab.surf(x, y, Z1)
##mlab.show()

#ax.plot_surface(X, Y, Z1)
#ax.plot_surface(X, Y, Z2)
#ax.plot_surface(X, Y, Z3)
#ax.plot_surface(X, Y, Z4)
#ax.plot_surface(X, Y, Z5, cmap=cm.Oranges_r)
#ax.plot_surface(X, Y, Z6, cmap=cm.Purples)
#ax.plot(X, Y, VEEC_rel[:16], color=c2)
#ax.plot(X, Y, VEE_rel[:16], color=c1)

#ax.set_xlabel("Separation (Relative to sum of VdW radii)")
#ax.set_ylabel("Theta (º)")
#ax.set_zlabel("$E_{def}$ (kJ mol$^{-1}$)")
#ax.set_xlim(0.7,1.3)
#ax.set_xticks(list(np.linspace(0.7,1.3,7)))
#ax.set_ylim(0,180)
#fig.colorbar(plt1, aspect=1,shrink=0.05, ticks=[]).set_label("$V_{ee}$")
#fig.colorbar(plt2, aspect=1,shrink=0.05, ticks=[]).set_label("$V_{ne}$")
#ax.set_zticks(list(range(0,2750,500)))

#plt.show()
#plt.plot([i for i in range(0,181,5)], max_energies, 'b')
#plt.xlabel("Theta (º)")
#plt.ylabel("$E_{def}$ (kJ mol$^{-1}$)")
#plt.title("Maximum $E_{def}$ for varied theta")
#plt.xlim(0,180)

#    plt.plot(separations[5:21], Edef[5:21], color='k', label="$E_{def}$")
#    plt.plot(separations[5:21], VEE_rel[5:21], color='r', label="$V_{ee}$")
#    plt.plot(separations[5:21], VNE_rel[5:21], color='g', label="$V_{ne}$")    
#    plt.plot(separations[5:21], T_rel[5:21], color='b', label="$T$")
#    if theta in [0,45,90,135,180]:
#        plt.plot(separations[5:21], Edef[5:21], color=c1, label=str(theta))
#    else:
#        plt.plot(separations[5:21], Edef[5:21], color=c1)
#    plt.plot(separations[5:21], [0 for i in range(16)], color = 'k', alpha = 0.2)
#    plt.xlim((0.7,1.3))
#    #plt.ylim((-1000,3000))
#    plt.xlabel("Separation (Relative to sum of VdW radii)")
#    plt.ylabel("$E_{def}$ (kJ mol$^{-1}$)")
#    plt.title("Deformation Energy")
#    plt.legend()
#    plt.plot(separations[5:21], Edef[5:21], linestyle="-", marker="^", label="E$_{\mathbf{intra}}$", color="black");
#    plt.plot(separations[5:21], VNE_rel[5:21], linestyle="-", marker="o", label="V$_{\mathbf{ne}}$", color="#FF0000");
#    plt.plot(separations[5:21], T_rel[5:21], linestyle="-", marker="s", label="T", color="#2CFF00");
#    plt.plot(separations[5:21], VEE_rel[5:21], linestyle="-", marker="v", label="V$_{\mathbf{ee}}$", color="#0095FF");
#plt.grid(axis='y', linestyle="-");
#plt.xlabel("Separation (Relative to Sum of vdW Radii)", size=12);
#plt.ylabel("Deformation Energy (kJ/mol)", size=12);
#plt.ylim(1.002, 1.008);
#plt.gca().get_yaxis().get_major_formatter().set_useOffset(False);
#plt.xlim(0.6, 1.4);
#plt.legend(prop={'size': 18});
#plt.ylim(ymin=0);
#plt.ylim(ymax=200);
#plt.xlim(xmin=2.5)
#plt.show();
#plt.close()
    
#
    c1 = next(color1)
    if theta in [0,45,90,135,180]:
        axarr[0,0].plot(separations[5:21], Edef[5:21], label=str(theta)+"º", color=c1)
        axarr[0,1].plot(separations[5:21], VNE_rel[5:21], label=str(theta)+"º", color=c1)
        axarr[1,1].plot(separations[5:21], T_rel[5:21], label=str(theta)+"º", color=c1)
        axarr[1,0].plot(separations[5:21], VEE_rel[5:21], label=str(theta)+"º", color=c1)
    else:
        axarr[0,0].plot(separations[5:21], Edef[5:21], color=c1)
        axarr[0,1].plot(separations[5:21], VNE_rel[5:21], color=c1)
        axarr[1,1].plot(separations[5:21], T_rel[5:21], color=c1)
        axarr[1,0].plot(separations[5:21], VEE_rel[5:21], color=c1)
    
#    c2 = next(color2)
#    Edef = [SE2[i]+SE3[i] - (2*F_intra)/3.8088E-04 for i in range(len(SE1))]
#    VEE_rel = [VEE2[i]+VEE3[i] - (2*F_Vee)/(3.8088E-04) for i in range(len(VEE1))]
#    VNE_rel= [VNE2[i]+VNE3[i] - (2*F_Vne)/(3.8088E-04) for i in range(len(VNE1))]
#    T_rel = [T2[i]+T3[i] - (2*F_T)/(3.8088E-04) for i in range(len(T1))]
#    VEEC_rel = [VEEC2[i]+VEEC3[i] - (2*F_VeeC)/(3.8088E-04) for i in range(len(VEEC1))]
#    VEEX_rel = [VEEX2[i]+VEEX3[i] - (2*F_VeeX)/(3.8088E-04) for i in range(len(VEEX1))]
#    axarr[0,0].plot(separations[5:21], Edef[5:21], label=str(theta)+"º", color=c2)
#    axarr[0,1].plot(separations[5:21], VNE_rel[5:21], label=str(theta)+"º", color=c2)
#    axarr[1,1].plot(separations[5:21], T_rel[5:21], label=str(theta)+"º", color=c2)
#    axarr[1,0].plot(separations[5:21], VEE_rel[5:21], label=str(theta)+"º", color=c2)
#
axarr[0,0].legend()
axarr[0,1].legend()
axarr[1,0].legend()
axarr[1,1].legend()
#
plt.show()
