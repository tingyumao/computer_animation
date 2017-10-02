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
    p_r = 1.0
    dist = 10.0
    v_init = 20.0
    num_row = 14
    num_col = 14
    particle_ids = [[num_col*i + j for j in range(num_col)] for i in range(num_row)]
    #print(particle_ids)
    
    # add particles
    for i in range(num_row):
        for j in range(num_col):
            idx = particle_ids[i][j]
            if i == num_row//2-1 and j == num_col//2-1:
                vx, vy = -v_init, v_init
            elif i == num_row//2-1 and j == num_col//2:
                vx, vy = v_init, v_init
            elif i == num_row//2 and j == num_col//2:
                vx, vy = v_init, -v_init
            elif i == num_row//2 and j == num_col//2-1:
                vx, vy = -v_init, -v_init
            else:
                vx, vy = 0.0, 0.0
                
            FIX = 0
            color = [random.random(), random.random(), random.random()]
            duration = None
            scene += add_particle(idx, 1, dist*i, dist*j, vx, vy, FIX, p_r, color, duration)
    # add edge and spring forces
    edge_id = 0
    k = 5
    l0 = dist
    for i in range(num_row):
        for j in range(num_col):
            idx = particle_ids[i][j]
            if i+1 < num_row:
                jdx = particle_ids[i+1][j]
                scene += add_edge(idx, jdx, p_r/2)
                scene += add_springforce(edge_id, k, l0)
                edge_id += 1
            if j+1 < num_col:
                jdx = particle_ids[i][j+1]
                scene += add_edge(idx, jdx, p_r/2)
                scene += add_springforce(edge_id, k, l0)
                edge_id += 1
    #print(edge_id)
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
            
if __name__ == '__main__':
    main()
    
    
    


