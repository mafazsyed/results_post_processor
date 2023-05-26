def read_data(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        data = []
        for line in lines:
            split_line = line.split()
            if len(split_line) < 2:
                print(f"Skipping line due to insufficient data: '{line.strip()}'")
                continue
            try:
                node_data = [int(split_line[0]), float(split_line[1])]
                data.append(node_data)
            except ValueError:
                print(f"Skipping line due to a conversion error: '{line.strip()}'")
                continue
    return data

def calculate_average_strains(data):
    strains = {}
    for node_data in data:
        node, strain = node_data
        if node in strains:
            strains[node].append(strain)
        else:
            strains[node] = [strain]

    average_strains = {}
    for node, strain_values in strains.items():
        average_strains[node] = sum(strain_values) / len(strain_values)

    return average_strains

def write_data(file_name, data):
    with open(file_name, 'w') as file:
        for node, average_strain in data.items():
            line = "{:d}\t{:15.10E}\n".format(node, average_strain)
            file.write(line)

import os

def process_files_average_emin(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]

    for file in files:
        input_file_path = os.path.join(input_dir, file)
        output_file_name = f"{os.path.splitext(file)[0]}_averaged.txt"
        output_file_path = os.path.join(output_dir, output_file_name)

        data = read_data(input_file_path)
        average_strains = calculate_average_strains(data)
        write_data(output_file_path, average_strains)

    print(f"Processed {len(files)} files, and saved them to '{output_dir}'.")