import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

from ..RDG_networks.Classes import Line, LineSegment, Polygon
from ..RDG_networks.generate_line_segments import generate_line_segments
from ..RDG_networks.draw_segments import draw_segments
from ..RDG_networks.get_intersection_segments import get_intersection_segments

fig, ax1 = plt.subplots()

angles = [-np.pi/4, np.pi/4, np.pi/6, np.pi/2]
segments_dict, polygon_arr = generate_line_segments(20, angles=angles)
segments = list(segments_dict.values())
intersection_segments = get_intersection_segments(segments)

for segment in intersection_segments:
    start = segment.start
    end = segment.end
    ax1.scatter(start[0], start[1], color='red')
    ax1.scatter(end[0], end[1], color='red')

draw_segments(intersection_segments, ax=ax1, fig=fig)

plt.show()