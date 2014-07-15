# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

import numpy
import matplotlib.pyplot as plt
import sys 

R = 30
#R = sys.argv[1]

def random_walk(R):
       
    x = []
    y = []
    z = []
    N_steps = []
    r = []
        
    x.append(0.0)
    y.append(0.0)
    z.append(0.0)
    N_steps.append(0)
    r.append(0.0)
        
    x_i = x[0]
    y_i = y[0]
    z_i = z[0]
    N_steps_i = N_steps[0]
    r_i = r[0]
    
    while (r_i < R):
                                        
        phi = numpy.random.random()*2*numpy.pi
        cos_theta = numpy.random.random()*2-1        
        theta = numpy.arccos(cos_theta)
        
        delta_x = numpy.sin(theta)*numpy.cos(phi)
        delta_y = numpy.sin(theta)*numpy.sin(phi)
        delta_z = numpy.cos(theta)
        
        x_new = x_i + delta_x
        y_new = y_i + delta_y
        z_new = z_i + delta_z
        N_steps_new = N_steps_i + 1
        r_new = numpy.sqrt(x_new**2 + y_new**2 + z_new**2)
        
        x.append(x_new)
        y.append(y_new)
        z.append(z_new)
        N_steps.append(N_steps_new)
        r.append(r_new)
        
        x_i = x_new
        y_i = y_new
        z_i = z_new
        N_steps_i = N_steps_new
        r_i = r_new
    
    filename = 'marcha-aleatoria.dat'       
    
    out = open(filename, 'w')
        
    for i in range(len(x)):
        line_str = str(x[i])+'\t'+str(y[i])+'\t'+str(z[i])+'\t'+str(N_steps[i])+'\t'+str(r[i])+'\n'
        out.write(line_str)
            
    out.close()
                
random_walk(R)      

