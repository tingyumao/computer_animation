#!/usr/bin/env python
import os
import argparse
import random
from math import *
from scene_elements import *

parser = argparse.ArgumentParser(description='Create my scene')
parser.add_argument("-n", "--num_particles", type=int, help="define number of moving particle")
parser.add_argument("-f", "--filename", type=str, help="define the name of output file")

def main():
    args = parser.parse_args()
    print(args)
    num_particles = args.num_particles
    filename = args.filename
    
    scene = init_scene()
    # add moving particles
    for i in range(num_particles):
        # mass
        m = 1.0
        # position and velocity
        px = 0.0
        py = 0.0
        vx = 2*random.gauss(0, 0.5)
        vy = 5*random.uniform(0,1)
        # other info
        fixed = 0
        radius = 0.02
        color = [random.random(), random.random(), random.random()]
        duration = None
        scene += add_particle(i, m, px, py, vx, vy, fixed, radius, color, duration)
        
    # add fixed points and edge to make a cube
    m = 1.0
    fixed = 1
    radius = 0.02
    color = [1.0, 1.0, 1.0]
    """
    scene += add_particle(num_particles, m, -1.0, 1.0, 0.0, 0.0, fixed, radius, color)
    scene += add_particle(num_particles+1, m, -1.0, -1.0, 0.0, 0.0, fixed, radius, color)
    scene += add_particle(num_particles+2, m, 1.0, -1.0, 0.0, 0.0, fixed, radius, color)
    scene += add_particle(num_particles+3, m, 1.0, 1.0, 0.0, 0.0, fixed, radius, color)
    scene += add_edge(num_particles, num_particles+1, radius)
    scene += add_edge(num_particles+1, num_particles+2, radius)
    scene += add_edge(num_particles+2, num_particles+3, radius)
    scene += add_edge(num_particles+3, num_particles, radius)
    """
>>>>>>> 5dce69cccaee8496ec2d75226ccae26b6e6548f7
    
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