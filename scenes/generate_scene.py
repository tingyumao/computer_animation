#!/usr/bin/env python
import os
import argparse
import random
from math import *
from scene_elements import *

## Add arguments
parser = argparse.ArgumentParser(description='Create my scene')
parser.add_argument("-f", "--filename", type=str, help="define the name of output file")

## Main function
def main():
    args = parser.parse_args()
    filename = args.filename
    
    # add header into scene
    scene = init_scene()
    #############################################################
    # Add content here                                          #
    ############################################################# 
    vx_init = 1
    vy_init = 0
    v_init = 5.0
    
    scene += add_particle(0, 0.5, 0, 0, 0, 0, 0, 0.4, [0.0,0.5,0.5])
    
    num_particles = 40
    p_r = 0.2
    radius = 8
    delta_ang = 2*pi/num_particles
    # add particles
    for i in range(num_particles):
        m = 1
        x, y = radius*cos(delta_ang*i), radius*sin(delta_ang*i)
        vx, vy = v_init*y/radius, -v_init*x/radius
        scene += add_particle(i+1, m, x, y, vx, vy, 0, p_r, [0.1,0.0,1.0])
    # add edge and spring force
    for i in range(num_particles):
        l0 = radius - 1.0#random.uniform(1.0, 2.0)
        k = 10.0 * random.uniform(0.8, 1.2)
        scene += add_edge(0, i+1, p_r/4)
        scene += add_springforce(i, k, l0)
    
    #scene += add_particle(num_particles+1, 1, 40, -40, 0, 0, 1, 0.5, [0.0,0.0,0.0])
    #scene += add_simplegravity(0.0, -9.81)
    #############################################################
    # End of content                                            #
    ############################################################# 
    
    # add end mark </scene> into scene
    scene += end_scene()
    
    # write scene into .xml file
    with open(os.path.join("./", filename), "w") as output:
        for line in scene:
            output.write(line)
            output.write("\n")
    # END OF CODE
            
if __name__ == '__main__':
    main()
    
    
    

