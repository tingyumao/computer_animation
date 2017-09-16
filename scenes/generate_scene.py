#!/usr/bin/env python
import os
import argparse
import random

def init_scene():
    ## initial setup
    init = []
    init.append("<!-- Creative Scene -->")
    init.append("<scene>")
    init.append("<duration time=\"5.0\"/>")
    init.append("<integrator type=\"explicit-euler\" dt=\"0.01\"/>")
    init.append("<maxsimfreq max=\"500.0\"/>")
    init.append("<simplegravity fx=\"0.0\" fy=\"-9.81\"/>")
    init.append("<backgroundcolor r=\"0.0\" g=\"0.0\" b=\"0.0\"/>")
    return init

def end_scene():
    return ["</scene>"]
    
def add_particle(i, m, x, y, vx, vy, fixed, radius, color, duration=None):
    # add position and velocity
    particle = "<particle m=\"{:.2f}\" px=\"{:.2f}\" py=\"{:.2f}\" vx=\"{:.2f}\" vy=\"{:.2f}\" fixed=\"{:d}\" radius=\"{:.2f}\"/>".format(m, x, y, vx, vy, fixed, radius)
    # add color
    r, g, b = color
    particle_color = "<particlecolor i=\"{:d}\" r=\"{:.2f}\" g=\"{:.2f}\" b=\"{:.2f}\"/>".format(i, r, g, b)
    
    ## <particlepath i="23" duration="10.0" r="1.0" g="0.469387755102" b="0.530612244898"/>
    if duration is None:
        return [particle, particle_color]
    else:
        particle_path = "<particlepath i=\"{:d}\" duration=\"{:.2f}\" r=\"{:.2f}\" g=\"{:.2f}\" b=\"{:.2f}\"/>".format(i, duration, r, g, b)
        return [particle, particle_color, particle_path] 

def add_edge(i, j, radius):
    edge = "<edge i=\"{:d}\" j=\"{:d}\" radius=\"{:.2f}\"/>".format(i, j, radius)
    return [edge]


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
    
    
    
