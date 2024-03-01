import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

from ..RDG_networks.Classes import Line, LineSegment, Polygon
from ..RDG_networks.generate_line_segments import generate_line_segments
from ..RDG_networks.draw_segments import draw_segments
from ..RDG_networks.generate_line_network import generate_line_network

angles = [-np.pi/4, np.pi/4, np.pi/6, np.pi/2]
segments_dict, polygon_arr = generate_line_segments(20, angles=angles)
segments = list(segments_dict.values())
G = generate_line_network(segments)
pos=nx.get_node_attributes(G, 'loc')

fig, ax1 = plt.subplots()

draw_segments(segments, ax=ax1, fig=fig)
nx.draw(G, ax=ax1, pos=pos, node_size=100)
plt.show()