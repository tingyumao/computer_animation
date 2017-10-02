# Initialization section
def init_scene(duration=50.0, integrator="symplectic-euler", dt=0.01, bg_color=[0.0, 0.0, 0.0]):
    ## initial setup
    init = []
    init.append("<!-- Creative Scene -->")
    init.append("<scene>")
    init.append("<duration time=\"{:.2f}\"/>".format(duration))
    init.append("<integrator type=\"{}\" dt=\"{:.2f}\"/>".format(integrator, dt))
    init.append("<maxsimfreq max=\"500.0\"/>")
    ## define background color.
    r, g, b = bg_color
    init.append("<backgroundcolor r=\"{:.2f}\" g=\"{:.2f}\" b=\"{:.2f}\"/>".format(r, g, b))
    return init

def end_scene():
    return ["</scene>"]

# Force section
def add_simplegravity(fx, fy): 
    """
    <simplegravity fx="0.981" fy="0"/>
    """
    simplegravity = "<simplegravity fx=\"{:.3f}\" fy=\"{:.3f}\"/>".format(fx, fy)
    return [simplegravity]
    
def add_springforce(edge_id, k, l0):
    """
    <springforce edge="0" k="1.0" l0="1.0" />
    """
    edge_springforce = "<springforce edge=\"{:d}\" k=\"{:.2f}\" l0=\"{:.2f}\" />".format(edge_id, k, l0)
    return [edge_springforce] 

def add_gravity(i, j, kbs, kvc):
    """
    <gravitationalforce i="0" j="1" G="10.118419"/>
    """
    gravitationalforce = "<gravitationalforce i=\"{:d}\" j=\"{:d}\" G=\"{}\"/>".format(i, j, G)
    return [gravitationalforce]

def add_vortexforce(i, j, kbs, kvc):
    """
    <vortexforce i="0" j="1" kbs="0.8" kvc="1000.0"/>
    """
    vortexforce = "<vortexforce i=\"{:d}\" j=\"{:d}\" kbs=\"{}\" kvc=\"{}\"/>".format(i, j, kbs, kvc)
    return [vortexforce]
    

## Entity section
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

def edit_edgecolor(i, color):
    """
    <edgecolor i="0" r="0.3" g="0.2" b="0.6"/>
    """
    r, g, b = color
    edgecolor = "<edgecolor i=\"{:d}\" r=\"{:.2f}\" g=\"{:.2f}\" b=\"{:.2f}\"/>".format(i, r, g, b)
    return [edgecolor]
    