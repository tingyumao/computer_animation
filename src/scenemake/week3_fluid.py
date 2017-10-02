#!/usr/bin/env python
import os
import argparse
import random
from math import *
from scene_elements import *

## Add arguments
parser = argparse.ArgumentParser(description='Create my scene')
parser.add_argument("-f", "--filename", type=str, help="define the name of output file")

## Define mass
Large = 1000000000.0
Small = 1.0

## Main function
def main():
    args = parser.parse_args()
    filename = args.filename
    
    # add header into scene
    duration = 50.0
    integrator="symplectic-euler"
    dt = 0.03
    bg_color = [0.0, 0.0, 0.1]
    scene = init_scene(duration, integrator, dt, bg_color)
    #############################################################
    # Add content here                                          #
    ############################################################# 
    # Part 1: night background
    num_star = 500
    edge_id = 0
    k = 100
    l0 = 0.1
    r = 0.2
    for i in range(num_star):
        p_r = random.uniform(0.01,0.2)
        x = max(min(random.gauss(10, 12), 30),-10)
        y = max(min(random.gauss(-10, 12), 10), -30)
        cr = random.uniform(0,0.8)
        color = [0.8*cr, cr, 1-cr]
        scene += add_particle(2*i, 1.0, x, y, 0.0, 0.0, 0, p_r, color, None)
        ang = random.uniform(0, 2*pi)
        rx, ry = r*cos(ang), r*sin(ang)
        scene += add_particle(2*i+1, 1.0, x+rx, y+ry, 0.0, 0.0, 0, p_r, color, None)
        scene += add_edge(2*i, 2*i+1, p_r/2)
        scene += add_springforce(edge_id, k, l0)
        scene += edit_edgecolor(edge_id, color)
        edge_id += 1
    
    base_id = 2*num_star
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
    num_small = 1000
    num_flow = 6
    delta_ang = 2*pi/num_flow
    offset_ang = 0.0*pi/num_flow
    radius = [2, 3, 4]
    p_r = 0.04
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
        duration = 7
        scene += add_particle(i+num_large+base_id, m, px, py, vx, vy, fixed, p_r, color, duration)
    
    # add vortex force
    kbs = 6
    kvc = 10.0
    for i in range(num_large):
        for j in range(num_large, num_small+num_large):
            scene += add_vortexforce(i+base_id, j+base_id, kbs, kvc)
    
    #############################################################
    # End of content                                            #
    ############################################################# 
    
    # add end mark </scene> into scene
    scene += end_scene()
    
    # write scene into .xml file
    with open(os.path.join("/home/codio/workspace/movie/computer_animation/scenes/", filename), "w") as output:
        for line in scene:
            output.write(line)
            output.write("\n")
    # END OF CODE
            
if __name__ == '__main__':
    main()
    
    
    



