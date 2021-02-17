import numpy as np
import remap
#import matplotlib.pyplot as plt

H=100.;n0=10;z0=-np.linspace(0,H,n0+1);u0=np.linspace(0,1,n0);n1=3;z1=-np.linspace(0,H,n1+1);u1=np.zeros(n1)


dz0 = z0[1:]-z0[:-1]
dz1 = z1[1:]-z1[:-1]

u_in = u0[np.newaxis,np.newaxis,:]
z_in = z0[np.newaxis,np.newaxis,:]
#u_out = u1[np.newaxis,np.newaxis,:]
z_out = z1[np.newaxis,np.newaxis,:]

u_out=remap.remap_mod.remap(u_in,z_in,z_out,method='PCM',bndy_extrapolation=False)
u1=u_out[0,0,:]
print('PCM remapping error (%)=',(np.sum(u1*dz1)-np.sum(u0*dz0))/np.sum(u0*dz0))
u_out=remap.remap_mod.remap(u_in,z_in,z_out,method='PLM',bndy_extrapolation=False)
u1=u_out[0,0,:]
print('PLM remapping error (%)=',(np.sum(u1*dz1)-np.sum(u0*dz0))/np.sum(u0*dz0))
u_out=remap.remap_mod.remap(u_in,z_in,z_out,method='PPM_H4',bndy_extrapolation=False)
u1=u_out[0,0,:]
print('PPM_H4 remapping error (%)=',(np.sum(u1*dz1)-np.sum(u0*dz0))/np.sum(u0*dz0))
u_out=remap.remap_mod.remap(u_in,z_in,z_out,method='PQM_IH4IH3',bndy_extrapolation=False)
u1=u_out[0,0,:]
print('PQM_IH4IH3 remapping error (%)=',(np.sum(u1*dz1)-np.sum(u0*dz0))/np.sum(u0*dz0))
#plt.plot(u0,0.5*(z0[:-1]+z0[1:]))
#plt.plot(u1,0.5*(z1[:-1]+z1[1:]))
#plt.show()
