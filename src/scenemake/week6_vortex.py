#!/usr/bin/env python
import os
import argparse
import random
from math import *
import numpy as np
# add path
import sys

cwd = os.getcwd()
sys.path.append(cwd)

from scene_elements import *

## Define mass
Large = 1000000000.0
Small = 1.0

## Add arguments
parser = argparse.ArgumentParser(description='Create my scene')
parser.add_argument("-f", "--filename", type=str, help="define the name of output file")

def main():
    
    args = parser.parse_args()
    filename = args.filename
    
    ## initial setup
    duration=20.0; integrator="forward-backward-euler"; dt=0.005; bg_color=[0.0, 0.0, 0.1]
    init = []
    init.append("<!-- Creative Scene -->")
    init.append("<scene>")
    init.append("<duration time=\"{:.2f}\"/>".format(duration))
    init.append("<integrator type=\"{}\" dt=\"{:.2f}\"/>".format(integrator, dt))
    init.append("<maxsimfreq max=\"500.0\"/>")
    ## define background color.
    r, g, b = bg_color
    init.append("<backgroundcolor r=\"{:.2f}\" g=\"{:.2f}\" b=\"{:.2f}\"/>".format(r, g, b))
    ## define viewpoint
    init.append("<viewport cx=\"0.0\" cy=\"0.0\" size=\"25.0\"/>")
    ## define collision type
    init.append("<collision type=\"simple\" COR=\"1.0\"/>")
    #init.append("<collision type=\"penalty\" k=\"1000\" thickness=\"0\"/>")
    init.append("<collisiondetection type=\"contest\"/>")
    
    scene = init
    #############################################################
    # Add content here                                          #
    ############################################################# 
    # load pixel files
    # pixel = np.load("dispicableme.npy")
    
    # pixel = pixel[:,10:34,:]
    
    # add half plane
    #scene += add_halfplane([0,0], [1,0])
    #scene += add_halfplane([50,0], [-1,0])
    #scene += add_halfplane([0,50], [0,-1])
    #scene += add_halfplane([0,0], [0,1])
    
    base_id = 2*0
    # Part 2: starry night
    # add static large particles
    num_large = 6
    p_r = 0.2
    radius = 0.5
    delta_ang = 2*pi/num_large
    offset_ang = 1.0*pi/num_large
    # add particles
    for i in range(num_large):
        m = Large
        x, y = radius*cos(delta_ang*i+offset_ang), radius*sin(delta_ang*i+offset_ang)
        vx, vy = 0.0, 0.0##v_init*y/radius, -v_init*x/radius
        duration = None
        scene += add_particle(i+base_id, m, x, y, vx, vy, 0, p_r, bg_color, duration)
    
    # add random distributed small particles
    num_small = 1500
    num_flow = 6
    delta_ang = 2*pi/num_flow
    offset_ang = 0.0*pi/num_flow
    radius = [2, 3, 4]
    p_r = 0.2
    num_color = 7
    colors = [(0.4, 0.6, 0.6), (0.6, 0.4, 0.4), (0.8, 0.2, 0.2), (0.5, 0.5, 0.5), (0.3, 0.7, 0.7)]
    for i in range(num_small):
        m = Small
        r = random.uniform(1.0,2)#radius[rand_idx]
        px, py = r*cos(delta_ang*i+offset_ang), r*sin(delta_ang*i+offset_ang)
        vx, vy = 0.0, 0.0
        # other info
        fixed = 0
        cr = float(i%num_color)/num_color
        color = [0.8*cr, cr, 1-cr]
        duration = None
        scene += add_particle(i+num_large+base_id, m, px, py, vx, vy, fixed, p_r, color, duration)
    
    # add vortex force
    kbs = 6
    kvc = 10.0
    for i in range(num_large):
        for j in range(num_large, num_small+num_large):
            scene += add_vortexforce(i+base_id, j+base_id, kbs, kvc)
    
    # add particles
    
    base_id = num_small + num_large
    num_row = 100
    num_col = 100
    idx = 0
    for i in range(num_row):
        for j in range(num_col):
            px = i - 50
            py = j - 50
            m = 1
            duration = None
            cr = 1-0.8*random.random()#float(i%num_color)/num_color
            color = [0.8*cr, cr, 1-cr]
            if (px < -1 or px > 1) and (py<-1 or py>1):
                scene += add_particle(idx+base_id, m, px, py, 0.0, 0.0, 0, 0.25, color, duration)
                idx += 1
            
    
    # add gravity
    # add_gravity(i, j, G)
    #G = 10.118419
    #for i in range(num_particle):
    #    scene += add_gravity(i+base, base+num_particle, G)
    
    # add simple gravity
    # scene += add_simplegravity(0.0, -1.0)
    #############################################################
    # End of content                                            #
    ############################################################# 
    
    # add end mark </scene> into scene
    scene += end_scene()
    
    # write scene into .xml file
    with open(os.path.join("../../scenes/", filename), "w") as output:
        for line in scene:
            output.write(line)
            output.write("\n")
    # END OF CODE

    
if __name__ == "__main__":
    main()