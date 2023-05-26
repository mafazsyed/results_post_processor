import math
import os

def read_data(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        data = []
        for line in lines:
            node_data = [float(value) for value in line.split()]
            data.append(node_data)
    return data

def euclidean_distance(coord1, coord2):
    return math.sqrt(sum([(a - b)**2 for a, b in zip(coord1, coord2)]))

def find_nodes_within_distance(data, reference_node, distance):
    nodes_within_distance = []
    ref_node_coord = reference_node[1:4]
    for node in data:
        node_coord = node[1:4]
        if euclidean_distance(ref_node_coord, node_coord) <= distance:
            nodes_within_distance.append(node)
    return nodes_within_distance

def process_data(data):
    distance = 3
    average_min_principal_list = []
    nodes_within_distance_list = []

    for specified_node in data:
        nodes_within_distance = find_nodes_within_distance(data, specified_node, distance)
        nodes_within_distance_list.append(nodes_within_distance)
        
        total_min_principal = sum(node[4] for node in nodes_within_distance)
        average_min_principal = total_min_principal / len(nodes_within_distance)
        average_min_principal_list.append(average_min_principal)

    return average_min_principal_list, nodes_within_distance_list

def write_results_to_file(file_name, data, average_min_principal_list):
    MFS_coefficient = 500 * 0.0104
    with open(file_name, 'w') as file:
        for i, avg_min_principal in enumerate(average_min_principal_list):
            MFS = MFS_coefficient / avg_min_principal
            file.write(f"Node, {int(data[i][0])}, Average E. Min. Principal for 3mm Radius, {avg_min_principal:.6f},     MFS, {MFS:.6f}\n")

def write_nodes_within_distance_to_file(file_name, data, nodes_within_distance_list):
    with open(file_name, 'w') as file:
        MFS_coefficient = 500 * 0.0104
        for i, nodes_within_distance in enumerate(nodes_within_distance_list):
            center_node = data[i]
            file.write(f"Center Node: {int(center_node[0])}\n")
            total_min_principal = 0

            for node in nodes_within_distance:
                line = "{:12d}{:16.6f}{:16.6f}{:16.6f}{:16.6f}\n".format(int(node[0]), node[1], node[2], node[3], node[4])
                file.write(line)
                total_min_principal += node[4]

            if len(nodes_within_distance) > 0:
                average_min_principal = total_min_principal / len(nodes_within_distance)
                MFS = MFS_coefficient / average_min_principal
                file.write(f"Average E. Min. Principal: {average_min_principal:16.6f},\nMFS: {MFS:.6f}\n\n")

import os
import math

def process_files_auto_3mm_radius(input_folder, output_folder_1, output_folder_2):
    # Iterate over the 28 input files
    for file_number in range(1, 29):
        input_file = os.path.join(input_folder, f"{file_number}_averaged_combined.txt")
        data = read_data(input_file)

        # Process the data and find the average E. Min. Principal for each node and the nodes within 3mm distance
        average_min_principal_list, nodes_within_distance_list = process_data(data)

        # Write the average E. Min. Principal results to a text file
        output_file_1 = os.path.join(output_folder_1, f"{file_number}resultsimple.txt")
        write_results_to_file(output_file_1, data, average_min_principal_list)

        # Write the nodes within 3mm distance for each node to a different text file
        output_file_2 = os.path.join(output_folder_2, f"{file_number}resultadvanced.txt")
        write_nodes_within_distance_to_file(output_file_2, data, nodes_within_distance_list)