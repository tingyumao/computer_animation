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

## Add arguments
parser = argparse.ArgumentParser(description='Create my scene')
parser.add_argument("-f", "--filename", type=str, help="define the name of output file")

def main():
    
    args = parser.parse_args()
    filename = args.filename
    
    ## initial setup
    duration=10.0; integrator="forward-backward-euler"; dt=0.02; bg_color=[1.0, 1.0, 1.0]
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
    init.append("<viewport cx=\"25\" cy=\"15\" size=\"20.0\"/>")
    ## define collision type
    #init.append("<collision type=\"simple\" COR=\"1.0\"/>")
    init.append("<collision type=\"hybrid\" maxiters=\"10\" k=\"50\" COR=\"0\"/>")
    
    <simtype type="rigid-body"/>
  <description text="Hexagon"/>
  <viewport cx="0.0" cy="0.0" size="10"/>
  <maxsimfreq max="100.0"/>
  <duration time="2.0"/>
 
  <rigidbodyintegrator type="symplectic-euler" dt="0.01"/>

  <rigidbodycollisionhandling detection="all-pairs" response="gr-velocity-projection"/>
    
    
    scene = init
    #############################################################
    # Add content here                                          #
    ############################################################# 
    # load pixel files
    # pixel = np.load("dispicableme.npy")
    
    # pixel = pixel[:,10:34,:]
    
    # add half plane
    scene += add_halfplane([0,0], [1,0])
    scene += add_halfplane([50,0], [-1,0])
    #scene += add_halfplane([0,5], [0,-1])
    scene += add_halfplane([0,-5], [0,1])
    
    # add edge: two boundary of funnel
    fixed = 1
    re = 30
    color = (1.0, 1.0, 1.0)
    l0 = 30
    k = 10000
    m = 10000
    #scene += add_particle(0, m, 0, 45, 0.0, 0.0, fixed, re, color)
    #scene += add_particle(1, m, 20, 20, 0.0, 0.0, fixed, re, color)
    #scene += add_edge(0, 1, re)
    #scene += edit_edgecolor(0, color)
    #scene += add_springforce(0, k, l0)
    
    #scene += add_particle(2, m, 50, 45, 0.0, 0.0, fixed, re, color)
    #scene += add_particle(3, m, 30, 20, 0.0, 0.0, fixed, re, color)
    #scene += add_edge(2, 3, re)
    #scene += edit_edgecolor(1, color)
    #scene += add_springforce(1, k, l0)
    scene += add_particle(0, m, -10, 20, 0.0, 0.0, fixed, re, color)
    scene += add_particle(1, m, 60, 20, 0.0, 0.0, fixed, re, color)
    
    # add particle
    base = 2
    radius = 1.4
    num_col = 27
    num_row = 6
    num_particle = num_row*num_col
    for i in range(num_row):
        for j in range(num_col):
            idx = num_col*i + j
            # mass
            m = 1.0
            # position and velocity
            vx = 0.0
            vy = 0.0
            px = 1*random.uniform(15,35)
            py = 1*random.uniform(50,70)
            # other info
            fixed = 0
            #color = [random.random(), 0.0, 0.0]
            #cr = float(i%num_color)/num_color
            cr = random.random()
            color = [0.8*cr, cr, 1-cr]
            duration = None
            scene += add_particle(idx+base, m, px, py, vx, vy, fixed, radius, color, duration)
    
    # add particle
    fixed = 1
    color = bg_color
    radius = 0.1
    m = 100.0
    scene += add_particle(base+num_particle, m, 25, -8.0, 0.0, 0.0, fixed, radius, color, duration)
    
    # add gravity
    # add_gravity(i, j, G)
    G = 10.118419
    for i in range(num_particle):
        scene += add_gravity(i+base, base+num_particle, G)
    
    # add simple gravity
    scene += add_simplegravity(0.0, -9.81)
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