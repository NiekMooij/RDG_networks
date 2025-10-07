import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import random
from RDG_networks.thickness.generate_line_segments_thickness import generate_line_segments_thickness
from RDG_networks import save_to_stl
from RDG_networks.save_data import save_to_json, load_from_json

if __name__ == '__main__':
    size = 15 
    lamb0 = 0.2
    alpha = 0.52
    thickness_arr = [ lamb0*t**(-alpha) for t in range(1, size+1) ]
    box_size = 1
    angles = [ random.random() * 2*np.pi for _ in range(size)]

    # Initial structure
    data_dict = generate_line_segments_thickness(size=size, thickness_arr=thickness_arr, angles=angles, box_size=box_size)
    
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

    save_to_stl(segment_thickness_dict, thickness=0.2, name=os.path.join(sys.path[0], 'network.stl'), frame_thickness=0.1)

    file_path = os.path.join(sys.path[0], 'data.json')
    save_to_json(data_dict, file_path)
    data = load_from_json(file_path)

    plt.show()