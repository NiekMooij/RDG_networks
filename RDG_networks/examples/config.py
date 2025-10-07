import numpy as np
import os
import sys
import random
import matplotlib.pyplot as plt
from generate_line_segments_thickness import generate_line_segments_thickness

if __name__ == '__main__':
    size = 150
    lamb0 = 0.2
    alpha = 0.52
    thickness_arr = [ lamb0*t**(-alpha) for t in range(1, size+1) ]
    box_size = 1
    angles = [ random.random() * 2*np.pi for _ in range(size)]
    nucleation_points = [ (random.random(), random.random()) for _ in range(size) ]

    # Initial structure
    data_dict = generate_line_segments_thickness(size=size, thickness_arr=thickness_arr, angles=angles, box_size=box_size, nucleation_points=nucleation_points)

    fig, ax1= plt.subplots(nrows=1, ncols=1, figsize=(5,5))

    segment_thickness_dict = data_dict['segment_thickness_dict']
    for key, segment in segment_thickness_dict.items():
        segment.draw(ax1)
        middle_segment = segment.middle_segment
        if middle_segment:
            middle_segment.draw(ax1)

    ax1.set(xlim=(0, 1), ylim=(0, 1))

    ax1.set_xticks([], [])
    ax1.set_yticks([], [])

    plt.show()