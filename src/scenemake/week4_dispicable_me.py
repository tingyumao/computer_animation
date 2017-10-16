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

from scenemake.scene_elements import *

## Add arguments
parser = argparse.ArgumentParser(description='Create my scene')
parser.add_argument("-f", "--filename", type=str, help="define the name of output file")

def main():
    
    args = parser.parse_args()
    filename = args.filename
    
    ## initial setup
    duration=200.0; integrator="forward-backward-euler"; dt=0.02; bg_color=[1.0, 1.0, 1.0]
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
    init.append("<viewport cx=\"25\" cy=\"20\" size=\"25.0\"/>")
    ## define collision type
    init.append("<collision type=\"simple\" COR=\"1.0\"/>")
    
    scene = init
    #############################################################
    # Add content here                                          #
    ############################################################# 
    # load pixel files
    pixel = np.load("dispicableme.npy")
    
    pixel = pixel[:,10:34,:]
    
    # add half plane
    scene += add_halfplane([0,0], [1,0])
    scene += add_halfplane([50,0], [-1,0])
    #scene += add_halfplane([0,5], [0,-1])
    #scene += add_halfplane([0,-2], [0,1])
    
    # add edge
    fixed = 1
    re = 0.4
    k = 10000
    l0 = 2.5
    #color = (0.0, 0.0, 0.0)
    nr, nc, _ = pixel.shape
    for i in range(nr):
        for j in range(nc):
            eid = nc*i+j
            py = 1*i - 2
            
            px = (50-nc)//2 + 1*j
            vx = 0.0
            r, g, b = pixel[nr-1-i, j, :]/255.0
            """
            if i%2 == 0:
                px = 25 + 1*j
                vx = 2.0
                r, g, b = pixel[nr-1-i, j, :]/255.0
            if i%2 == 1:
                px = 50-1*j - 25
                vx = -2.0
                r, g, b = pixel[nr-1-i, nc-1-j, :]/255.0
            """
            vy = 0.0
            m = 1
            #print(m)
            #if i==0 and j==0:
            #    vx = 20.0
            # add edges
            color = (r, g, b)
            scene += add_particle(eid, m, px, py, vx, vy, 0, re, color)
            #scene += add_particle(2*eid+1, m, px, py, 0.0, 0.0, fixed, re, color)
            #scene += add_edge(2*eid, 2*eid+1, re)
            #scene += edit_edgecolor(eid, color)
            #scene += add_springforce(eid, k, l0)
    
    # add edge
    re = 15
    color = (1.0, 1.0, 1.0)
    l0 = 30
    k = 10000
    m = 10000
    scene += add_particle(eid+1, m, 25, 60, 0.0, -10.0, 0, re, color)
    
    re = 0.5
    scene += add_particle(eid+2, m, 2, -5, 0.0, 0.0, 0, re, color)
    scene += add_particle(eid+3, m, 48, -5, 0.0, 0.0, 0, re, color)
    scene += add_edge(eid+2, eid+3, re)
    scene += edit_edgecolor(0, color)
    scene += add_springforce(0, k, l0)
    
    # add particle
    """
    for i in range(15):
        # mass
        m = 1.0
        # position and velocity
        vx = 0.0
        vy = 0.0
        px = 1*random.uniform(-1,1)
        py = 1*random.uniform(4,5)
        # other info
        fixed = 0
        radius = 0.2
        color = [random.random(), random.random(), random.random()]
        duration = None
        scene += add_particle(i+base, m, px, py, vx, vy, fixed, radius, color, duration)
    """
    # add force
    #scene += add_simplegravity(0.0, -2.81)
    #############################################################
    # End of content                                            #
    ############################################################# 
    
    # add end mark </scene> into scene
    scene += end_scene()
    
    # write scene into .xml file
    with open(os.path.join("../scenes/", filename), "w") as output:
        for line in scene:
            output.write(line)
            output.write("\n")
    # END OF CODE

    
if __name__ == "__main__":
    main()