import json
from .Classes import Line, LineSegment, Polygon

def save_to_json(data_dict, file_path):
    data_dict['segments_dict'] = {key: pol.to_dict() for key, pol in data_dict['segments_dict'].items()}
    data_dict['segment_thickness_dict'] = {key: pol.to_dict() for key, pol in data_dict['segment_thickness_dict'].items()}

    with open(file_path, 'w') as json_file:
        json.dump(data_dict, json_file)

def load_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data