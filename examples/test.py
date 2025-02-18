import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import random

from RDG_networks.thickness.orientate_network import orientate_network
from RDG_networks.thickness.generate_line_segments_thickness import generate_line_segments_thickness
# from RDG_networks import save_to_stl

if __name__ == '__main__':
    size = 100                              # Size of the network starts larger because we cut away corners
    size = int(size * 1.9)                  # Size of the network
    D0 = 0.2                                # Initial thickness  
    alpha = 0.52                            # Exponent for the thickness decay
    thickness_arr = [ D0*t**(-alpha) for t in range(1, size+1) ]    # Thickness array
    box_size = np.sqrt(2)                   # Size of the box
    epsilon = 0.001                         # Minimum distance between segments
    angles = [ random.uniform(0, 2*np.pi) for i in range(size) ]        # Possible angles
    config = None                           # Configuration of the network (does not work at the moment)
    
    orientation = [-np.pi/4, 0, np.pi/4]    # Orientations to evaluate (w.r.t to optimal alignment)
    grid_points = 360                       # Number of angles to evaluate
    # director = [0, 1]
    director = [0, 1]

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
    
    # Get different orientations of the initial network.
    output = orientate_network(data_dict,
                               orientation = orientation, 
                               grid_points = grid_points,
                               box_measurements = box_measurements,
                               director = director)
    
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(15,5))

    segment_thickness_dict_1 = output[1]['data_dict']['segment_thickness_dict']
    for key, segment in segment_thickness_dict_1.items():
        segment.draw(ax1)
        middle_segment = segment.middle_segment
        if middle_segment:
            middle_segment.draw(ax1)

    segment_thickness_dict_2 = output[2]['data_dict']['segment_thickness_dict']
    for key, segment in segment_thickness_dict_2.items():
        segment.draw(ax2)
        middle_segment = segment.middle_segment
        if middle_segment:
            middle_segment.draw(ax2)

    segment_thickness_dict_3 = output[3]['data_dict']['segment_thickness_dict']
    for key, segment in segment_thickness_dict_3.items():
        segment.draw(ax3)
        middle_segment = segment.middle_segment
        if middle_segment:
            middle_segment.draw(ax3)

    ax1.set(xlim=(0, 1), ylim=(0, 1))
    ax2.set(xlim=(0, 1), ylim=(0, 1))
    ax3.set(xlim=(0, 1), ylim=(0, 1))

    
    # # Save the networks to an stl file
    # save_to_stl(segment_thickness_dict_1, thickness = 0.2, name=os.path.join(sys.path[0], 'network_1.stl'), frame_thickness = 0.1)
    # save_to_stl(segment_thickness_dict_2, thickness = 0.2, name=os.path.join(sys.path[0], 'network_2.stl'), frame_thickness = 0.1)
    # save_to_stl(segment_thickness_dict_3, thickness = 0.2, name=os.path.join(sys.path[0], 'network_3.stl'), frame_thickness = 0.1)

    plt.show()