import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import random
from RDG_networks.thickness.generate_line_segments_thickness import generate_line_segments_thickness
from RDG_networks import save_to_stl

if __name__ == '__main__':
    size = 500                              # Size of the network starts larger because we cut away corners
    size = 15 
    D0 = 0.2                                # Initial thickness  
    alpha = 0.52                            # Exponent for the thickness decay
    thickness_arr = [ D0*t**(-alpha) for t in range(1, size+1) ]    # Thickness array
    box_size = np.sqrt(2)                   # Size of the box
    box_size = 1
    epsilon = 0.001                         # Minimum distance between segments
    angles = 'uniform' 
    angles = [ random.random() * 2*np.pi for _ in range(size)]                     # Possible angles
    config = None                           # Configuration of the network (does not work at the moment)
    
    v1 = (np.sqrt(2)/2-1/2, np.sqrt(2)/2-1/2)   # Box measurements
    v2 = (np.sqrt(2)/2-1/2, np.sqrt(2)/2+1/2)
    v3 = (np.sqrt(2)/2+1/2, np.sqrt(2)/2+1/2)
    v4 = (np.sqrt(2)/2+1/2, np.sqrt(2)/2-1/2)
    box_measurements = [v1, v2, v3, v4]

    # Initial structure
    data_dict = generate_line_segments_thickness(size = size,
                                            thickness_arr =  thickness_arr,
                                            epsilon = epsilon,
                                            config = config,
                                            angles = angles,
                                            box_size = box_size)
    
    fig, ax1= plt.subplots(nrows=1, ncols=1, figsize=(5,5))

    segment_thickness_dict_1 = data_dict['segment_thickness_dict']
    for key, segment in segment_thickness_dict_1.items():
        segment.draw(ax1)
        middle_segment = segment.middle_segment
        if middle_segment:
            middle_segment.draw(ax1)

    ax1.set(xlim=(0, 1), ylim=(0, 1))

    ax1.set_xticks([], [])
    ax1.set_yticks([], [])

    plt.show()