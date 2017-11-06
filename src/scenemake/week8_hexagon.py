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

def add_hexagon(idx, center, velocity, color, r, m):
    hexagon = []
    cx, cy = center
    vx, vy = velocity
    for i in range(10):
        a = 360.0/10.0
        b = 180.0/10.0
        ang = 2*pi*(i*a+b)/360.0
        tmp = "<rigidbodyvertex x=\"{}\" y=\"{}\" m=\"{}\"/>".format(cx+r*cos(ang), cy+r*sin(ang), m)
        hexagon.append(tmp)
    
    
    tmp = "<rigidbody p=\"{}\" p=\"{}\" p=\"{}\" p=\"{}\" p=\"{}\" p=\"{}\" p=\"{}\" p=\"{}\" p=\"{}\" p=\"{}\" vx=\"{}\" vy=\"{}\" omega=\"0.0\" r=\"{}\"/>".format(10*idx, 10*idx+1, 10*idx+2, 10*idx+3, 10*idx+4, 10*idx+5, 10*idx+6, 10*idx+7, 10*idx+8, 10*idx+9, vx, vy, r)
    hexagon.append(tmp)
    
    r, g, b = color
    tmp = "<rigidbodycolor body=\"{}\" r=\"{}\" g=\"{}\" b=\"{}\"/>".format(idx, r, g, b)
    hexagon.append(tmp)
    
    return hexagon 
    
    
def main():
    
    args = parser.parse_args()
    filename = args.filename
    
    ## initial setup
    duration=20.0; integrator="forward-backward-euler"; dt=0.02; bg_color=[0.0, 0.0, 0.0]
    init = []
    init.append("<!-- Creative Scene -->")
    init.append("<scene>")
    
    init.append("<simtype type=\"rigid-body\"/>")
    init.append("<description text=\"Hexagon\"/>")
    init.append("<rigidbodyintegrator type=\"symplectic-euler\" dt=\"0.01\"/>")
    init.append("<rigidbodycollisionhandling detection=\"all-pairs\" response=\"gr-velocity-projection\"/>")
    
    init.append("<duration time=\"{:.2f}\"/>".format(duration))
    init.append("<maxsimfreq max=\"100.0\"/>")
    ## define background color.
    r, g, b = bg_color
    init.append("<backgroundcolor r=\"{:.2f}\" g=\"{:.2f}\" b=\"{:.2f}\"/>".format(r, g, b))
    ## define viewpoint
    init.append("<viewport cx=\"-1.0\" cy=\"0.0\" size=\"15.0\"/>")
    
    scene = init
    #############################################################
    # Add content here                                          #
    #############################################################
    # add triangle structure
    idx = 0
    for i in range(9):
        for j in range(i):
            if i == 1:
                continue
            center = [2.0*j-2.0*(i/2.0), -i*2*cos(pi/6.0)]
            velocity = [0.0, 0.0]
            r = 0.5
            m = 0.04
            color = [0.0, 0.0, 1.0 - i/9.0]
            scene += add_hexagon(idx, center, velocity, color, r, m)
            idx += 1
    
    center = [-2.0*(1.0/2.0), 2.0]
    velocity = [0.0, -5.0]
    r = 0.5
    m = 0.1
    color = [0.0, 0.0, 1.0]
    scene += add_hexagon(idx, center, velocity, color, r, m) 
    idx += 1
    
    scene.append("<!--bounding box-->")
    scene.append("<rigidbodyvertex x=\"-16\" y=\"15\" m=\"0.25\"/>")
    scene.append("<rigidbodyvertex x=\"14\" y=\"15\" m=\"0.25\"/>")
    scene.append("<rigidbodyvertex x=\"14\" y=\"-15\" m=\"0.25\"/>")
    scene.append("<rigidbodyvertex x=\"-16\" y=\"-15\" m=\"0.25\"/>")
    scene.append("<rigidbody p=\"{}\" p=\"{}\" p=\"{}\" p=\"{}\" vx=\"0\" vy=\"0\" omega=\"0\" r=\"0.01\" fixed=\"1\" />".format(10*idx, 10*idx+1, 10*idx+2, 10*idx+3))
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