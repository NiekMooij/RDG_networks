import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

from ..RDG_networks.Classes import Line, LineSegment, Polygon
from ..RDG_networks.generate_line_segments import generate_line_segments_dynamic
from ..RDG_networks.draw_segments import draw_segments

if __name__ == '__main__':
    dt = 0.1 # time step
    epsilon = 0.01 # growing rate
    # time = np.sqrt(2)/2 # time between introduction of lines
    time = 0
    size = 10 # Size of the network
    segments = generate_line_segments_dynamic(size=size, dt=dt, epsilon=epsilon, time=time, angles='uniform')

    fig, ax1 = plt.subplots()
    draw_segments(segments, ax=ax1, fig=fig)
    plt.show()